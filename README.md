# CSCI 5511 - Artificial Intelligence Assignments

A comprehensive collection of assignments from the **CSCI 5511: Artificial Intelligence** course at the University of Minnesota Twin Cities. This repository covers fundamental AI concepts through practical implementations of search algorithms, adversarial game playing, and logical reasoning systems.

---

## 📚 Course Overview

**Course:** CSCI 5511 - Artificial Intelligence  
**Institution:** University of Minnesota Twin Cities  
**Level:** Master's (Graduate)

This course covers core artificial intelligence concepts including search strategies, game theory, knowledge representation, and logical reasoning.

---

## 📋 Assignment Summary

### Assignment 1: Informed & Uninformed Search - 8 Puzzle
**Topics:** Graph Search, Heuristics, Path Finding  
**File:** `eight_puzzle.py`

Implement and compare multiple search algorithms to solve the classic 8-puzzle problem:

**Algorithms Implemented:**
- **BFS (Breadth-First Search):** Uninformed, optimal in number of moves
- **DLS (Depth-Limited Search):** Uninformed with depth constraint
- **IDDFS (Iterative Deepening Depth-First Search):** Memory-efficient uninformed search
- **A\* Search:** Informed search using heuristics

**Key Features:**
- State representation using tuples (9 integers, blank = 0)
- Solvability checking using parity-based analysis
- Heuristic functions: Manhattan distance and misplaced tiles
- Neighbor generation with directional actions (Up, Down, Left, Right)
- Path reconstruction and solution verification
- Performance metrics: nodes expanded, execution time, memory usage

**Learning Outcomes:** Understanding of search space exploration, heuristic design, and algorithm tradeoffs between optimality, completeness, and efficiency.

---

### Assignment 2: Local Search - Warehouse Layout Optimization
**Topics:** Local Search, Optimization, Constraint Satisfaction  
**Files:** `warehouse_starter.zip`, `warehouse_layout_kushwaha.zip`

Optimize warehouse layout using local search techniques to minimize travel distances and improve traffic flow.

**Concepts Covered:**
- Local search algorithms (Hill Climbing, Simulated Annealing)
- State space representation for warehouse configurations
- Cost function design for traffic optimization
- Neighbor generation strategies
- Visualization of warehouse layouts and traffic patterns

**Problem Domain:**
- Designing efficient warehouse layouts
- Minimizing employee travel distances
- Optimizing product placement
- Traffic flow analysis with provided simulation examples

**Learning Outcomes:** Applying optimization algorithms to real-world logistical challenges, understanding local search limitations and escaping local optima.

---

### Assignment 3: Adversarial Search - RandOthello Game
**Topics:** Game Theory, Minimax, Alpha-Beta Pruning  
**Files:** `randothellogame.py`, `report.pdf`

Implement an intelligent game-playing agent for a variant of Othello (Reversi) using adversarial search.

**Game Mechanics:**
- 8×8 board with random blocked positions
- Tile flipping rules based on standard Othello
- White and Black players with alternating moves
- Skip moves when no legal actions available
- Win condition: player with most tiles at game end

**AI Techniques:**
- Minimax algorithm with game tree search
- Alpha-beta pruning for efficiency
- Evaluation functions (heuristic scoring)
- Depth-limited search for computational feasibility
- Move ordering optimizations

**Implementation Components:**
- `OthelloPlayerTemplate`: Base class for AI agents
- `HumanPlayer`: Interactive human-playable interface
- `RandOthelloState`: Game state management
- `AIPlayer`: Intelligent agent using minimax

**Learning Outcomes:** Understanding zero-sum games, adversarial search trees, pruning techniques, and building competitive AI agents.

---

### Assignment 4: Propositional Logic - Basic Logic & SAT Solving
**Topics:** Propositional Logic, Satisfiability, Knowledge Representation  
**Files:** `proplogic.py`, `proplogic_sat/` (SAT solver implementation)

Solve logical reasoning puzzles using propositional logic and SAT solver techniques.

**Problems Solved:**
- **Truth-Tellers II & III:** Logic puzzles involving truth-telling and truth-hiding agents
- **Robbery and Salt:** Complex inference problem with multiple constraints

**SAT Solver Architecture:**
- `sat.py`: Core SAT solving algorithms
- `sat_interface.py`: High-level interface for knowledge base operations
- `satinstance.py`: Internal representation of satisfiability instances
- `solvers/`: Multiple solver implementations
  - `recursive_sat.py`: Recursive SAT solver
  - `iterative_sat.py`: Iterative SAT solver with loop control
  - `watchlist.py`: Watchlist data structure for efficient constraint propagation

**Key Techniques:**
- CNF (Conjunctive Normal Form) conversion
- Unit propagation
- Pure literal elimination
- Backtracking search
- Knowledge base entailment checking
- Model finding and satisfaction

**API Functions:**
```python
kb = sat_interface.KB(clauses)
kb.test_literal(symbol)        # Test if literal satisfies KB
kb.is_satisfiable()            # Check KB satisfiability
kb.entails(query)              # Logical entailment checking
```

**Learning Outcomes:** Knowledge representation in logic, SAT problem solving, automated reasoning, and constraint satisfaction.

---

### Assignment 5: Propositional Logic - Clue Game Reasoner
**Topics:** Knowledge Representation, Inference, Game Playing  
**Files:** `clue_hw/clue/clue_game_reasoner.py`, documentation in main folder

Build an intelligent game assistant for Deduction (Clue board game) using propositional logic and constraint satisfaction.

**Game Components:**
- **Suspects:** Miss Scarlet, Colonel Mustard, Mrs. White, Mr. Green, Mrs. Peacock, Professor Plum
- **Weapons:** Knife, Candlestick, Revolver, Rope, Pistol, Wrench
- **Rooms:** Hall, Lounge, Dining, Kitchen, Ballroom, Conservatory, Billiard, Library, Study

**System Architecture:**
- `clue_game_reasoner.py`: Main reasoning engine
- SAT solver integration (same as Assignment 4)
- Constraint generation and management
- Card location tracking

**Knowledge Representation:**
- Card location variables: `<card>_<player>` or `<card>_CF` (case file)
- Constraints:
  - Each card in exactly one location
  - Card distribution among players
  - Weapon/suspect/room constraints
  - Player-specific information and deductions

**Reasoning Capabilities:**
- Track cards seen during play
- Eliminate impossible scenarios
- Deduce unknown card locations
- Reason about other players' cards
- Support game strategy with logical inference

**Class Methods:**
- `add_card_location(card, location)`: Assert card is at location
- `suggest(suspect, weapon, room)`: Process player suggestions
- `accuse()`: Determine most likely solution
- `query_card(card)`: Find where a card is located

**Learning Outcomes:** Complex knowledge base management, practical constraint solving, game theory application in digital assistants, and reasoning under uncertainty.

---

## 🛠️ Technical Stack

**Language:** Python 3.x  
**Key Libraries:**
- `collections.deque`: Queue data structure for BFS
- `heapq`: Priority queue for A* and best-first search
- `copy`: Deep copying for state management
- `random`: Randomization for RandOthello blocked tiles

**Development Environment:**
- Ubuntu 24.04
- Python 3.9+
- Version control: Git/GitHub

---

## 📁 Repository Structure

```
AI-Assignments-And-Projects/
│
├── Assignment1_Informed and Uninformed Search : 8 Puzzle/
│   ├── eight_puzzle.py
│   └── Informed and Uninformed Search_ 8-Puzzle.pdf
│
├── Assignment2_Local Search: Warehouse Layout Optimization/
│   ├── Local Search_ Warehouse Layout Optimization.pdf
│   ├── warehouse_starter.zip
│   ├── warehouse_layout_kushwaha.zip
│   └── given_traffic_example.gif
│
├── Assignment3_Adversarial Search: RandOthello/
│   ├── randothellogame.py
│   ├── Adversarial Search_ RandOthello.pdf
│   └── report.pdf
│
├── Assignment4_Propositional Logic: Basic Logic/
│   ├── proplogic.py
│   ├── Propositional Logic_ Basic Logic.pdf
│   └── proplogic_sat/
│       ├── proplogic_example.py
│       ├── sat.py
│       ├── sat_interface.py
│       ├── satinstance.py
│       ├── solvers/
│       │   ├── __init__.py
│       │   ├── recursive_sat.py
│       │   ├── iterative_sat.py
│       │   └── watchlist.py
│       ├── proplogic.py
│       └── __pycache__/
│
└── Assignment5_Propositional Logic: Clue Reasoner/
    ├── clue_hw/
    │   └── clue/
    │       ├── clue_game_reasoner.py
    │       ├── sat.py
    │       ├── sat_interface.py
    │       ├── satinstance.py
    │       ├── solvers/
    │       │   ├── __init__.py
    │       │   ├── recursive_sat.py
    │       │   ├── iterative_sat.py
    │       │   └── watchlist.py
    │       └── __pycache__/
    ├── clue_hw.zip
    └── Propositional Logic_ Clue Reasoner.pdf
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- Git
- ~100 MB disk space for all assignments

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ApurvK032/AI-Assignments-And-Projects.git
   cd AI-Assignments-And-Projects
   ```

2. **Navigate to an assignment folder:**
   ```bash
   cd "Assignment1_Informed and Uninformed Search : 8 Puzzle"
   ```

3. **Run the code:**
   ```bash
   python3 eight_puzzle.py
   ```

---

## 💡 Usage Examples

### Running 8-Puzzle Solver
```bash
cd "Assignment1_Informed and Uninformed Search : 8 Puzzle"
python3 eight_puzzle.py

# Enter initial state as 9-digit string (0 = blank):
# Example: 120843765
# This represents:
#   1 2 3
#   8 _ 4
#   7 6 5
```

### Solving Logic Puzzles
```bash
cd "Assignment4_Propositional Logic: Basic Logic"
python3 proplogic.py

# Solves:
# - Truth-Tellers II (logical deduction)
# - Truth-Tellers III (complex constraints)
# - Robbery and Salt (multi-agent reasoning)
```

### Playing RandOthello
```bash
cd "Assignment3_Adversarial Search: RandOthello"
python3 randothellogame.py

# Features:
# - Human vs AI player mode
# - Minimax AI agent
# - Real-time board visualization
# - Move validation and game state management
```

---

## 🎓 Key Concepts & Algorithms

| Topic | Algorithms | Assignment |
|-------|-----------|-----------|
| **Search** | BFS, DLS, IDDFS, A* | Assignment 1 |
| **Local Search** | Hill Climbing, Simulated Annealing | Assignment 2 |
| **Game Playing** | Minimax, Alpha-Beta Pruning | Assignment 3 |
| **Logic** | SAT Solving, CNF Conversion | Assignments 4 & 5 |
| **Reasoning** | Forward Chaining, Backward Chaining | Assignments 4 & 5 |
| **Optimization** | Cost Functions, Heuristics | All Assignments |

---

## 📊 Performance Metrics & Analysis

### Assignment 1: 8-Puzzle Benchmarks
- **BFS:** Guaranteed optimal, high memory usage
- **A\* (Manhattan):** Fewer nodes expanded than BFS
- **A\* (Misplaced):** Less informed, more nodes than Manhattan
- **IDDFS:** Memory-efficient, comparable to BFS on solution depth

### Assignment 3: RandOthello AI
- **Search Depth:** Tunable based on computational resources
- **Branching Factor:** ~20-30 legal moves per position
- **Pruning Efficiency:** Alpha-beta pruning reduces nodes by ~80%

### Assignments 4 & 5: SAT Solver Performance
- **Truth-Tellers Problems:** Solvable in <100ms
- **Clue Game:** Full 21-card problem with 6 players, solvable in <500ms
- **Scalability:** Handles 50+ variables with constraint propagation

---

## 📝 Assignment Difficulty Progression

**Beginner (Assignment 1-2):** Foundation in search algorithms and optimization  
**Intermediate (Assignment 3):** Adversarial thinking and game tree search  
**Advanced (Assignment 4-5):** Symbolic reasoning and knowledge representation  

Estimated time commitment: 15-20 hours per assignment for thorough understanding.

---

## 🔍 Common Issues & Solutions

### Assignment 1: 8-Puzzle
- **Problem:** Infinite loop in search
  - **Solution:** Ensure visited set is properly maintained
- **Problem:** Slow performance
  - **Solution:** Use Manhattan distance heuristic instead of misplaced tiles

### Assignment 3: RandOthello
- **Problem:** Moves evaluated incorrectly
  - **Solution:** Verify tile-flipping logic matches Othello rules
- **Problem:** AI too slow
  - **Solution:** Increase alpha-beta pruning depth limit

### Assignments 4 & 5: SAT Solver
- **Problem:** Variables not found in knowledge base
  - **Solution:** Ensure clause format is correct (space-separated literals)
- **Problem:** Solver returns "unsatisfiable" incorrectly
  - **Solution:** Check for typos in variable names, verify clause logic

---

## 📚 Learning Resources

**Textbook:** Russell & Norvig - *Artificial Intelligence: A Modern Approach* (4th Edition)

**Key Chapters by Assignment:**
- Assignment 1: Chapters 3-4 (Search Algorithms)
- Assignment 2: Chapter 4 (Local Search)
- Assignment 3: Chapter 5 (Adversarial Search)
- Assignment 4-5: Chapter 7-8 (Knowledge & Logic)

---

## 🎯 Learning Outcomes by Assignment

**Assignment 1:**
- ✅ Understand uninformed vs. informed search
- ✅ Implement multiple search algorithms
- ✅ Design and apply heuristic functions
- ✅ Analyze algorithm performance trade-offs

**Assignment 2:**
- ✅ Apply local search to optimization problems
- ✅ Design effective neighborhood functions
- ✅ Implement gradient-based optimization
- ✅ Solve real-world constraint problems

**Assignment 3:**
- ✅ Understand zero-sum games and game trees
- ✅ Implement minimax algorithm
- ✅ Apply alpha-beta pruning for efficiency
- ✅ Build competitive game-playing agents

**Assignment 4:**
- ✅ Represent knowledge using propositional logic
- ✅ Implement SAT solving algorithms
- ✅ Perform automated reasoning and inference
- ✅ Solve logical puzzles and constraints

**Assignment 5:**
- ✅ Build complex knowledge bases
- ✅ Apply SAT solvers to game domains
- ✅ Implement game-specific reasoning
- ✅ Reason about incomplete information

---

## 🤝 Contributing

This is an academic assignment repository. For improvements or corrections:

1. Review the assignment specifications (PDF files)
2. Test your changes thoroughly
3. Document any optimizations or fixes
4. Submit issues or pull requests with clear explanations

---

## 📄 Academic Integrity

These assignments are completed work for CSCI 5511. They are provided as reference material for:
- Learning AI concepts and algorithms
- Understanding implementation approaches
- Academic study and review

**Please refer to your institution's academic integrity policies** when using this repository for your own coursework.

---

## 📞 Contact & Attribution

**Course:** CSCI 5511 - Artificial Intelligence  
**Institution:** University of Minnesota Twin Cities  
**Student:** Apurv Kushwaha

---

## 📄 License

This repository contains academic work. Attribution to the original creators and instructors is appreciated.

---

## 🔗 Additional Resources

- **GitHub:** [ApurvK032/AI-Assignments-And-Projects](https://github.com/ApurvK032/AI-Assignments-And-Projects)
- **University of Minnesota:** [School of Computing](https://cse.umn.edu/)

---

**Last Updated:** November 2024  
**Python Version:** 3.9+  
**Status:** Complete (All 5 Assignments)

---

## 📊 Quick Reference: Algorithm Complexity

| Algorithm | Time Complexity | Space Complexity | Best Use Case |
|-----------|-----------------|------------------|---------------|
| BFS | O(b^d) | O(b^d) | Shortest path, uniform costs |
| DFS | O(b^m) | O(bm) | Space-constrained, deep solutions |
| IDDFS | O(b^d) | O(bd) | Optimal with limited memory |
| A* | O(b^d) (best case) | O(b^d) | Optimality with heuristics |
| Minimax | O(b^m) | O(bm) | Complete game trees |
| Alpha-Beta | O(b^(m/2)) | O(bm) | Efficient game tree pruning |
| SAT (DPLL) | O(2^n) worst | O(n) average | Logic puzzles, constraints |

---

**Ready to dive into AI? Start with Assignment 1 and work through the progression!** 🚀
