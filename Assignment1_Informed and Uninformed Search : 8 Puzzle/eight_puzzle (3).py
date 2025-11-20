"""
CSCI 5511- Assignment 1 – 8-Puzzle (Uninformed + Informed Search)

This code covers:
  - State representation (Tuple of 9 ints; Blank is 0)
  - Visualize State
  - Solvability-check using Parity
  - Neighbors with action names: "Right", "Left", "Down", "Up"
  - Path reconstruction function
  - BFS (uninformed, optimal in #moves)
  - DLS + IDDFS (uninformed)
  - Heuristics: num_wrong_tiles, manhattan_distance
  - A* with either heuristic
  - Timing + reporting for all four methods
"""


import sys
import time
from collections import deque
import heapq


# Goal State
GOAL = (1, 2, 3, 8, 0, 4, 7, 6, 5)

# For fast Manhattan-distance
GOAL_POS = {tile: divmod(i, 3) for i, tile in enumerate(GOAL)}

############ Input & String to Tuple Conversion 
def parse_state_from_int_string(s: str):

    if len(s) != 9 or not s.isdigit():
        sys.exit("Error: initial state must be 9 digits number, like 120843765 (0 = blank).")
    digits = [int(ch) for ch in s]
    if sorted(digits) != list(range(9)):
        sys.exit("Error: initial state must contain digits 0 to 8 exactly once.")
    return tuple(digits)



############ Visualising TUpple as a table of 3*3

def visualize(state):
    for i in range(0, 9, 3):
        row = state[i:i+3]
        print(" ".join("_" if x == 0 else str(x) for x in row))
    print()


############ Solvability Check - To check if the initial sequnce in solvable to goal sequence or not

    #For odd-width boards (3*3), initial sate is solvable to goal iff inversion parity matches.
    #Implementation:
    # - Build goal index of each tile (ignore blank 0).
    # - Map the intial state's tile order to the goal indices (except 0).
    # - Count inversions in that sequence; solvable iff inv count is even.

def is_solvable_with_goal(start, goal):
    
    goal_index = {tile: i for i, tile in enumerate(goal) if tile != 0}
    seq = [goal_index[t] for t in start if t != 0]

    inv = 0
    # Count pairs (i < j) where seq[i] > seq[j]
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if seq[i] > seq[j]:
                inv += 1
    return (inv % 2) == 0



############ Defining Neighbor states and Actions : Up, Down, Left, Right

    #Generate (action, next_state) pairs by sliding a neighbor tile into the blank.
    #         Actions are named by the tile's motion into the blank

def neighbors(state):
    i = state.index(0)              # index of blank
    r, c = divmod(i, 3)
    result = []

    def swap(a, b):
        s = list(state)
        s[a], s[b] = s[b], s[a]
        return tuple(s)

    if c > 0:
        result.append(("Right", swap(i, i - 1)))      # Right

    if c < 2:
        result.append(("Left", swap(i, i + 1)))      # Left

    if r > 0:
        result.append(("Down", swap(i, i - 3)))

    if r < 2:
        result.append(("Up", swap(i, i + 3)))

    return result


######## Contructing the List of actions takenfrom start state to goal state

def reconstruct_actions(parent, end_state):

    actions = []
    s = end_state
    while True:
        prev, act = parent[s]  #parent[state] = (prev_state, action_taken_to_reach_state)
        if prev is None: 
            break
        actions.append(act)
        s = prev
    actions.reverse()
    return actions


###############  UnInformed Search


##### BFS ( Uses a queue, a visited set, and a parent map )

def breadth_first(initial_state):

    if initial_state == GOAL:
        return []

    q = deque([initial_state])
    visited = {initial_state}
    parent = {initial_state: (None, None)}  # initial state has no parent/action

    while q:
        s = q.popleft()

        for action, ns in neighbors(s):
            if ns in visited:
                continue
            parent[ns] = (s, action)
            if ns == GOAL:
                return reconstruct_actions(parent, ns)
            visited.add(ns)
            q.append(ns)


    return None


##### DLS
def depth_limited_search(state, limit, path_set):

    if state == GOAL:
        return []

    if limit == 0:
        return "cutoff"

    cutoff_happened = False

    for action, ns in neighbors(state):
        if ns in path_set:  # avoid cycles on present path
            continue

        path_set.add(ns)
        result = depth_limited_search(ns, limit - 1, path_set)
        path_set.remove(ns)

        if result == "cutoff":
            cutoff_happened = True
        elif result is not None:
            return [action] + result          # Found a solution below; prepend the move we took to get there

    return "cutoff" if cutoff_happened else None



##### IDDFS   :  Repeatedly run DLS with increasing limit: 0, 1, 2, ...

def iterative_deepening(initial_state):

    # Taking limit cap as 50
    for limit in range(0, 50):
        result = depth_limited_search(initial_state, limit, {initial_state})
        if result != "cutoff":  # either found a solution (list) or failed (None)
            return result
    return None


########     HEURISTICS (FOR A*)

def num_wrong_tiles(state):   ## Heuristic h1: number of tiles out of place.
    wrong = 0
    for i, tile in enumerate(state):
        if tile != 0 and tile != GOAL[i]:
            wrong += 1
    return wrong


def manhattan_distance(state):    ##Heuristic h2: sum of |row - goal_row| + |col - goal_col| for tiles 1..8.
    total = 0
    for i, tile in enumerate(state):
        if tile == 0:
            continue
        r, c = divmod(i, 3)
        gr, gc = GOAL_POS[tile]
        total += abs(r - gr) + abs(c - gc)
    return total


###############  Informed Search

##### A* SEARCH (WITH EITHER HEURISTIC)   : Priority queue items are (f, g, tie, state)


def astar(initial_state, heuristic_fn):

    if initial_state == GOAL:
        return []

    open_heap = []
    tie = 0

    g_cost = {initial_state: 0}
    parent = {initial_state: (None, None)}

    h0 = heuristic_fn(initial_state)
    heapq.heappush(open_heap, (h0, 0, tie, initial_state))

    closed = set()  # expanded states

    while open_heap:
        f, g, _, s = heapq.heappop(open_heap)

        if s in closed:
            continue
        closed.add(s)

        if s == GOAL:
            return reconstruct_actions(parent, s)

        for action, ns in neighbors(s):
            newg = g + 1  # each move costs 1
            # If ns not seen before, or we found a cheaper path to it, update
            if ns not in g_cost or newg < g_cost[ns]:
                g_cost[ns] = newg
                parent[ns] = (s, action)
                h = heuristic_fn(ns)
                tie += 1
                heapq.heappush(open_heap, (newg + h, newg, tie, ns))

    return None


########### Returning Results with time taken

def run_and_report(name, solver_fn, *args):

    t0 = time.perf_counter()
    actions = solver_fn(*args)
    t1 = time.perf_counter()

    if actions is None:
        print(f"{name}: no solution found | time: {t1 - t0:.4f}s")
    elif actions == "cutoff":
        print(f"{name}: cutoff at depth | time: {t1 - t0:.4f}s")
    else:
        moves = ", ".join(actions)
        print(f"{name}: {len(actions)} moves | {moves} | time: {t1 - t0:.4f}s")


#####   Main

def main():
    # Expect exactly one argument: 9-digit initial state, 0 = blank
    if len(sys.argv) != 2:
        print("Usage: python eight_puzzle.py <initial_state_as_integer>")
        sys.exit(1)

    initial = parse_state_from_int_string(sys.argv[1])

    
    visualize(initial)    ##it will print the 3×3 grid of the start state

    # UNSOLVABLE filter (saves time for impossible pairs)
    if not is_solvable_with_goal(initial, GOAL):
        print("This start → goal pair is UNSOLVABLE (different inversion parity).")
        return

    # Run Required Searches
    run_and_report("BFS", breadth_first, initial)
    run_and_report("IterativeDeepening", iterative_deepening, initial)
    run_and_report("A* (num_wrong_tiles)", astar, initial, num_wrong_tiles)
    run_and_report("A* (manhattan_distance)", astar, initial, manhattan_distance)


if __name__ == "__main__":
    main()
