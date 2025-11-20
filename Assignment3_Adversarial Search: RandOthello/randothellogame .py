import random
import copy

WHITE = 1
BLACK = -1
EMPTY = 0
BLOCKED = -2
SIZE = 8
SKIP = "SKIP"

class OthelloPlayerTemplate:
    '''Template class for an Othello Player

    An othello player *must* implement the following methods:

    get_color(self) - correctly returns the agent's color

    make_move(self, state) - given the state, returns an action that is the agent's move
    '''
    def __init__(self, mycolor):
        self.color = mycolor

    def get_color(self):
        return self.color

    def make_move(self, state):
        '''Given the state, returns a legal action for the agent to take in the state
        '''
        return None

class HumanPlayer(OthelloPlayerTemplate):
    def __init__(self, mycolor):
        self.color = mycolor

    def get_color(self):
        return self.color

    def make_move(self, state):
        curr_move = None
        legals = actions(state)
        while curr_move == None:
            display(state)
            if self.color == 1:
                print("White ", end='')
            else:
                print("Black ", end='')
            print(" to play.")
            print("Legal moves are " + str(legals))
            move = input("Enter your move as a r,c pair:")
            if move == "":
                return legals[0]

            if move == SKIP and SKIP in legals:
                return move

            try:
                movetup = int(move.split(',')[0]), int(move.split(',')[1])
            except:
                movetup = None
            if movetup in legals:
                curr_move = movetup
            else:
                print("That doesn't look like a legal action to me")
        return curr_move

class RandOthelloState:
    '''A class to represent an othello game state'''

    def __init__(self, currentplayer, otherplayer, board_array = None, num_skips = 0):
        if board_array != None:
            self.board_array = board_array
        else:
            self.board_array = [[EMPTY] * SIZE for i in range(SIZE)]
            self.board_array[3][3] = WHITE
            self.board_array[4][4] = WHITE
            self.board_array[3][4] = BLACK
            self.board_array[4][3] = BLACK
            x1 = random.randrange(8)
            x2 = random.randrange(8)
            self.board_array[x1][0] = BLOCKED
            self.board_array[x2][7] = BLOCKED
        self.num_skips = num_skips
        self.current = currentplayer
        self.other = otherplayer


def player(state):
    return state.current

def actions(state):
    '''Return a list of possible actions given the current state
    '''
    legal_actions = []
    for i in range(SIZE):
        for j in range(SIZE):
            if result(state, (i,j)) != None:
                legal_actions.append((i,j))
    if len(legal_actions) == 0:
        legal_actions.append(SKIP)
    return legal_actions

def result(state, action):
    '''Returns the resulting state after taking the given action

    (This is the workhorse function for checking legal moves as well as making moves)

    If the given action is not legal, returns None

    '''
    # first, special case! an action of SKIP is allowed if the current agent has no legal moves
    # in this case, we just skip to the other player's turn but keep the same board
    if action == SKIP:
        newstate = RandOthelloState(state.other, state.current, copy.deepcopy(state.board_array), state.num_skips + 1)
        return newstate

    if state.board_array[action[0]][action[1]] != EMPTY:
        return None

    color = state.current.get_color()
    # create new state with players swapped and a copy of the current board
    newstate = RandOthelloState(state.other, state.current, copy.deepcopy(state.board_array))

    newstate.board_array[action[0]][action[1]] = color
    
    flipped = False
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    for d in directions:
        i = 1
        count = 0
        while i <= SIZE:
            x = action[0] + i * d[0]
            y = action[1] + i * d[1]
            if x < 0 or x >= SIZE or y < 0 or y >= SIZE:
                count = 0
                break
            elif newstate.board_array[x][y] == -1 * color:
                count += 1
            elif newstate.board_array[x][y] == color:
                break
            else:
                count = 0
                break
            i += 1

        if count > 0:
            flipped = True

        for i in range(count):
            x = action[0] + (i+1) * d[0]
            y = action[1] + (i+1) * d[1]
            newstate.board_array[x][y] = color

    if flipped:
        return newstate
    else:  
        # if no pieces are flipped, it's not a legal move
        return None

def terminal_test(state):
    '''Simple terminal test
    '''
    # if both players have skipped
    if state.num_skips == 2:
        return True

    # if there are no empty spaces
    empty_count = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if state.board_array[i][j] == EMPTY:
                empty_count += 1
    if empty_count == 0:
        return True
    return False

def display(state):
    '''Displays the current state in the terminal window
    '''
    print('  ', end='')
    for i in range(SIZE):
        print(i,end='')
    print()
    for i in range(SIZE):
        print(i, '', end='')
        for j in range(SIZE):
            if state.board_array[j][i] == WHITE:
                print('W', end='')
            elif state.board_array[j][i] == BLACK:
                print('B', end='')
            elif state.board_array[j][i] == BLOCKED:
                print('X', end='')
            else:
                print('-', end='')
        print()

def display_final(state):
    '''Displays the score and declares a winner (or tie)
    '''
    wcount = 0
    bcount = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if state.board_array[i][j] == WHITE:
                wcount += 1
            elif state.board_array[i][j] == BLACK:
                bcount += 1

    print("Black: " + str(bcount))
    print("White: " + str(wcount))
    if wcount > bcount:
        print("White wins")
    elif wcount < bcount:
        print("Black wins")
    else:
        print("Tie")

# ---------- Helpers for AI ----------

INF = 10**9

def count_discs(board, color):
    c = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == color:
                c += 1
    return c

WEIGHTS = [
    [ 20, -3,  2,  2,  2,  2, -3, 20],
    [ -3, -8, -1, -1, -1, -1, -8, -3],
    [  2, -1,  1,  0,  0,  1, -1,  2],
    [  2, -1,  0,  1,  1,  0, -1,  2],
    [  2, -1,  0,  1,  1,  0, -1,  2],
    [  2, -1,  1,  0,  0,  1, -1,  2],
    [ -3, -8, -1, -1, -1, -1, -8, -3],
    [ 20, -3,  2,  2,  2,  2, -3, 20],
]

def eval_weighted_frontier(state, me):
    if terminal_test(state):
        myc = count_discs(state.board_array, me)
        opc = count_discs(state.board_array, -me)
        if myc > opc: return 100000
        if myc < opc: return -100000
        return 0

    board = state.board_array
    pos = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == me:
                pos += WEIGHTS[x][y]
            elif board[x][y] == -me:
                pos -= WEIGHTS[x][y]

    mobility = len(actions_for_eval(state, me)) - len(actions_for_eval(state, -me))

    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    def frontier_count(color):
        f = 0
        for x in range(8):
            for y in range(8):
                if board[x][y] == color:
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny] == EMPTY:
                            f += 1
                            break
        return f

    my_f = frontier_count(me)
    op_f = frontier_count(-me)
    return pos + 3*mobility - 2*(my_f - op_f)

def actions_for_eval(state, as_color):
    fake_me = OthelloPlayerTemplate(as_color)
    fake_opp = OthelloPlayerTemplate(-as_color)
    temp = RandOthelloState(fake_me, fake_opp, copy.deepcopy(state.board_array), state.num_skips)
    return actions(temp)

TT = {}
def board_key(board, to_move_color, depth):
    flat = []
    for x in range(8):
        for y in range(8):
            flat.append(str(board[x][y]))
    return f"{to_move_color}|{depth}|" + ''.join(flat)

EVAL = eval_weighted_frontier

# ---------- Random player ----------

class RandomPlayer(OthelloPlayerTemplate):
    def __init__(self, mycolor):
        self.color = mycolor
    def get_color(self):
        return self.color
    def make_move(self, state):
        legals = actions(state)
        return random.choice(legals)

# ---------- Minimax player (depth-limited) ----------

class MinimaxPlayer(OthelloPlayerTemplate):
    def __init__(self, mycolor, depth_limit=3):
        self.color = mycolor
        self.depth_limit = depth_limit
    def get_color(self):
        return self.color
    def make_move(self, state):
        legals = actions(state)
        best_move = legals[0]
        best_val = -INF
        for mv in legals:
            s2 = result(state, mv)
            if s2 is None:
                continue
            val = self.min_value(s2, self.depth_limit - 1)
            if val > best_val:
                best_val = val
                best_move = mv
        return best_move
    def max_value(self, state, depth):
        if terminal_test(state) or depth == 0:
            k = board_key(state.board_array, state.current.get_color(), depth)
            if k in TT: return TT[k]
            v = EVAL(state, self.color); TT[k] = v; return v
        v = -INF
        for mv in actions(state):
            s2 = result(state, mv)
            if s2 is None: continue
            v = max(v, self.min_value(s2, depth - 1))
        return v
    def min_value(self, state, depth):
        if terminal_test(state) or depth == 0:
            k = board_key(state.board_array, state.current.get_color(), depth)
            if k in TT: return TT[k]
            v = EVAL(state, self.color); TT[k] = v; return v
        v = INF
        for mv in actions(state):
            s2 = result(state, mv)
            if s2 is None: continue
            v = min(v, self.max_value(s2, depth - 1))
        return v

# ---------- Alpha-Beta player (iterative deepening) ----------

import time

class AlphabetaPlayer(OthelloPlayerTemplate):
    def __init__(self, mycolor, depth_limit=4):
        self.color = mycolor
        self.depth_limit = depth_limit
    def get_color(self):
        return self.color
    def make_move(self, state):
        start = time.time()
        time_budget = 1.5
        legals_root = actions(state)
        if not legals_root: return SKIP
        best_move = legals_root[0]
        best_val = -INF
        for d in range(2, self.depth_limit + 1):
            alpha, beta = -INF, INF
            cur_best, cur_val = best_move, -INF
            for mv in legals_root:
                s2 = result(state, mv)
                if s2 is None: continue
                val = self.min_value(s2, d - 1, alpha, beta)
                if val > cur_val:
                    cur_val = val
                    cur_best = mv
                if time.time() - start > time_budget:
                    break
            if cur_val > best_val:
                best_val, best_move = cur_val, cur_best
            if time.time() - start > time_budget:
                break
        return best_move
    def max_value(self, state, depth, alpha, beta):
        if terminal_test(state) or depth == 0:
            k = board_key(state.board_array, state.current.get_color(), depth)
            if k in TT: return TT[k]
            v = EVAL(state, self.color); TT[k] = v; return v
        v = -INF
        for mv in actions(state):
            s2 = result(state, mv)
            if s2 is None: continue
            v = max(v, self.min_value(s2, depth - 1, alpha, beta))
            if v >= beta: return v
            if v > alpha: alpha = v
        return v
    def min_value(self, state, depth, alpha, beta):
        if terminal_test(state) or depth == 0:
            k = board_key(state.board_array, state.current.get_color(), depth)
            if k in TT: return TT[k]
            v = EVAL(state, self.color); TT[k] = v; return v
        v = INF
        for mv in actions(state):
            s2 = result(state, mv)
            if s2 is None: continue
            v = min(v, self.max_value(s2, depth - 1, alpha, beta))
            if v <= alpha: return v
            if v < beta: beta = v
        return v

# ---------- Advanced player: alpha-beta + improved move ordering ----------

class AdvancedPlayer(OthelloPlayerTemplate):
    def __init__(self, mycolor, depth_limit=5):
        self.color = mycolor
        self.depth_limit = depth_limit
    def get_color(self):
        return self.color
    def order_moves(self, state, legals):
        if len(legals) <= 1:
            return legals
        corners = {(0,0),(0,7),(7,0),(7,7)}
        def opp_mobility_after(move):
            s2 = result(state, move)
            if s2 is None: return 999
            return len(actions(s2))
        no_skip = [m for m in legals if m != SKIP]
        corner_moves = [m for m in no_skip if m in corners]
        others = [m for m in no_skip if m not in corners]
        others.sort(key=opp_mobility_after)
        ordered = corner_moves + others
        return ordered if ordered else legals
    def make_move(self, state):
        legals = actions(state)
        if not legals: return SKIP
        legals = self.order_moves(state, legals)
        best_move = legals[0]
        alpha = -INF
        beta = INF
        best_val = -INF
        for mv in legals:
            s2 = result(state, mv)
            if s2 is None: continue
            val = self.min_value(s2, self.depth_limit - 1, alpha, beta)
            if val > best_val:
                best_val = val
                best_move = mv
            if best_val > alpha:
                alpha = best_val
        return best_move
    def max_value(self, state, depth, alpha, beta):
        if terminal_test(state) or depth == 0:
            k = board_key(state.board_array, state.current.get_color(), depth)
            if k in TT: return TT[k]
            v = EVAL(state, self.color); TT[k] = v; return v
        v = -INF
        legals = self.order_moves(state, actions(state))
        for mv in legals:
            s2 = result(state, mv)
            if s2 is None: continue
            v = max(v, self.min_value(s2, depth - 1, alpha, beta))
            if v >= beta: return v
            if v > alpha: alpha = v
        return v
    def min_value(self, state, depth, alpha, beta):
        if terminal_test(state) or depth == 0:
            k = board_key(state.board_array, state.current.get_color(), depth)
            if k in TT: return TT[k]
            v = EVAL(state, self.color); TT[k] = v; return v
        v = INF
        legals = self.order_moves(state, actions(state))
        for mv in legals:
            s2 = result(state, mv)
            if s2 is None: continue
            v = min(v, self.max_value(s2, depth - 1, alpha, beta))
            if v <= alpha: return v
            if v < beta: beta = v
        return v


# ---------- Runner ----------

def play_game(p1 = None, p2 = None, show=False):
    if p1 == None:
        p1 = HumanPlayer(BLACK)
    if p2 == None:
        p2 = HumanPlayer(WHITE)

    s = RandOthelloState(p1, p2)
    while True:
        action = p1.make_move(s)
        if action not in actions(s):
            print("Illegal move made by Black")
            print("White wins!")
            return
        s = result(s, action)
        if show:
            display(s)
        if terminal_test(s):
            print("Game Over")
            display(s)
            display_final(s)
            return
        action = p2.make_move(s)
        if action not in actions(s):
            print("Illegal move made by White")
            print("Black wins!")
            return
        s = result(s, action)
        if show:
            display(s)
        if terminal_test(s):
            print("Game Over")
            display(s)
            display_final(s)
            return

def auto_match():
    print("Match 1: AlphaBeta(BLACK) vs Random(WHITE)")
    p_black = AlphabetaPlayer(BLACK, depth_limit=4)
    p_white = RandomPlayer(WHITE)
    play_game(p_black, p_white, show=False)

    print("\nMatch 2: Random(BLACK) vs AlphaBeta(WHITE)")
    p_black = RandomPlayer(BLACK)
    p_white = AlphabetaPlayer(WHITE, depth_limit=4)
    play_game(p_black, p_white, show=False)

def main():
    auto_match()
   
    # play_game(HumanPlayer(BLACK), HumanPlayer(WHITE), show=True)

     # To play manually, comment auto_match() and uncomment the above line

if __name__ == '__main__':
    main()
