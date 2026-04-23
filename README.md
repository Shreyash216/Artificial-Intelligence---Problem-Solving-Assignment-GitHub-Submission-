# Artificial-Intelligence---Problem-Solving-Assignment-GitHub-Submission-
This Repository contains Two Projects

1) Minimax Task Selection Game
> A two-player adversarial task-picking game where an AI opponent uses the **Minimax Decision Tree** algorithm to always play optimally — maximising its own score while minimising yours.
---
 Overview
This project implements a console-based competitive game in which a human player and an AI agent take turns selecting tasks from a shared pool. Each task carries a numeric priority value. The player with the highest total score at the end wins.
The AI is powered by the Minimax algorithm — it recursively evaluates every possible future sequence of picks and always chooses the move that guarantees the best outcome under the assumption that the human also plays optimally.
---
🎓 Academic Details
Field	Details
Author	Shreyash
Institute	SRM Institute of Science and Technology, Tiruchirappalli
Subject	Artificial Intelligence / Decision Making Systems
Algorithm	Minimax (Decision Tree Search)
Language	Python 3.x
---
🧠 Algorithm — How Minimax Works Here
The game is modelled as a two-player, zero-sum game:
```
AI  = MAX player  →  wants to maximise (ai_score − user_score)
User = MIN player  →  wants to minimise (ai_score − user_score)
```
At each node in the decision tree, the algorithm:
Tries every possible task pick from the remaining pool.
Recursively simulates the opponent's best response.
Propagates the optimal score back up the tree.
The AI picks the task that leads to the globally best outcome.
Base case: when the pool is empty, the leaf node returns `ai_score − user_score` directly.
```
            [pool: 3, 7, 2]
             /      |      \
         pick 3   pick 7   pick 2     ← AI's MAX choices
          / \      / \      / \
        ...  ...  ...  ...  ...  ...  ← User's MIN responses
```
No alpha-beta pruning is applied here, keeping the implementation clean and readable for academic purposes.
---
🎮 Game Rules
A pool of tasks with integer priority values is provided at the start.
User always goes first, then turns alternate.
On each turn, the active player picks one task from the pool.
The picked task is removed from the pool — no re-selection.
The game ends when the pool is empty.
The player with the higher total score wins.
---
📂 Project Structure
```
minimax-task-game/
│
├── minimax_task_game.py    # Main program (all logic in one file)
└── README.md               # This file
```
---
▶️ How to Run
Prerequisites: Python 3.6 or higher. No external libraries required.
```bash
python minimax_task_game.py
```
On launch, you will be prompted to enter a custom task pool or press Enter to use the default:
```
Enter task priority values (space-separated), or press Enter
to use the sample input [3, 7, 2, 9, 5]:
  >
```
---
💡 Sample Session
Input:
```
Tasks: [3, 7, 2, 9, 5]
User starts first.
```
Output:
```
====================================================
     MINIMAX TASK SELECTION GAME
     AI uses Decision Tree Search (Minimax)
====================================================

  Initial Task Pool : [3, 7, 2, 9, 5]
  Total tasks       : 5
  User goes FIRST.

  ┌── Turn 1  (User's pick) ────────────────────────
  Available Pool : [3]  [7]  [2]  [9]  [5]
  Enter the task value you want to pick: 7

  ✔  User selects  : 7
  Remaining tasks  : [3, 2, 9, 5]

  ┌── Turn 2  (AI's pick) ──────────────────────────
  🤖 AI selects    : 9  (Minimax optimal)
  Remaining tasks  : [3, 2, 5]

  ┌── Turn 3  (User's pick) ────────────────────────
  Enter the task value you want to pick: 5

  ✔  User selects  : 5
  Remaining tasks  : [3, 2]

  ┌── Turn 4  (AI's pick) ──────────────────────────
  🤖 AI selects    : 3  (Minimax optimal)
  Remaining tasks  : [2]

  ┌── Turn 5  (User's pick) ────────────────────────
  Enter the task value you want to pick: 2

====================================================
  FINAL RESULTS
====================================================
  Tasks picked by User : [7, 5, 2]
  Tasks picked by AI   : [9, 3]
  ────────────────────────────────────────────────
  User Score  =  14
  AI Score    =  12
  ────────────────────────────────────────────────
  🏆  USER WINS!  (14 > 12)
====================================================
```
---
🔧 Functions Reference
Function	Description
`minimax(tasks, ai_score, user_score, is_ai_turn)`	Core recursive Minimax engine. Returns net AI advantage at a leaf node.
`ai_best_move(tasks, ai_score, user_score)`	Calls `minimax` for every possible pick and returns the index of the optimal one.
`get_user_pick(tasks)`	Interactively prompts the user and validates their pick.
`play_game(tasks)`	Main game loop — manages turns, display, and end-game verdict.
`main()`	Entry point — handles task input and launches `play_game`.
---
📊 Complexity Analysis
Metric	Value
Time complexity	O(n!) in the worst case — explores all permutations of picks
Space complexity	O(n) — recursion depth equals pool size
Practical limit	Pool sizes up to ~8–10 run instantly; larger pools may be slow
For larger inputs, Alpha-Beta Pruning can be added to reduce the effective branching factor and speed up the search significantly.
---
🔍 Key Insight
Even though the AI picks `9` (the highest value) on its very first move, the user can still win `14 – 12` with the sequence `7 → 5 → 2`. This is the optimal result under perfect play by both sides — the AI cannot guarantee a win when the user goes first on this particular pool. Minimax confirms this mathematically by exhausting the entire game tree.
---
🚀 Possible Extensions
Alpha-Beta Pruning — skip branches that cannot affect the final decision, enabling larger pool sizes.
Custom pool size — randomised task generation with configurable min/max values.
GUI version — interactive browser-based interface (already built as a companion widget).
Difficulty levels — limit Minimax search depth to simulate sub-optimal AI play.
Multiplayer mode — AI vs. AI simulation to observe pure optimal play.
---
📄 License
This project is submitted as academic coursework at SRM Institute of Science and Technology, Tiruchirappalli. Free to use for educational purposes.

2) Interactive Game AI (Tic-Tac-Toe System)
