"""
========================================================================
Minimax Task Selection Game
========================================================================
Author      : Shreyash
Institute   : SRM Institute of Science and Technology, Tiruchirappalli
Description : A two-player alternating task-selection game where the AI
              uses the Minimax algorithm (Decision Tree Search) to always
              pick the optimal task, maximising its score while minimising
              the user's advantage.

Rules       :
  - A shared pool of tasks (each with a numeric priority/weight) is given.
  - User and AI take alternate turns; User goes first.
  - On each turn the active player picks one task from the pool.
  - The picked task is removed from the pool.
  - AI always picks using Minimax — it considers every possible future
    sequence of picks to guarantee the best outcome.
  - Game ends when the pool is empty.
  - Winner is whoever has the higher total score.
========================================================================
"""

import math
from typing import List, Tuple


# ─────────────────────────────────────────────────────────────────────
# MINIMAX ENGINE
# ─────────────────────────────────────────────────────────────────────

def minimax(
    tasks     : List[int],
    ai_score  : int,
    user_score: int,
    is_ai_turn: bool
) -> int:
    """
    Recursive Minimax search over all possible task selections.

    Parameters
    ----------
    tasks      : Remaining tasks in the pool.
    ai_score   : AI's accumulated score so far in this branch.
    user_score : User's accumulated score so far in this branch.
    is_ai_turn : True if it is the AI's turn (MAX), False for User (MIN).

    Returns
    -------
    int : The net score advantage for AI (ai_score - user_score) at the
          leaf node that results from optimal play by both sides.
    """
    # Base case: no tasks left — return net advantage for AI
    if not tasks:
        return ai_score - user_score

    if is_ai_turn:
        # MAX: AI wants to maximise (ai_score - user_score)
        best = -math.inf
        for i, task_val in enumerate(tasks):
            remaining = tasks[:i] + tasks[i+1:]
            score = minimax(remaining, ai_score + task_val, user_score, False)
            best = max(best, score)
        return best
    else:
        # MIN: User's optimal play minimises AI's net advantage
        best = math.inf
        for i, task_val in enumerate(tasks):
            remaining = tasks[:i] + tasks[i+1:]
            score = minimax(remaining, ai_score, user_score + task_val, True)
            best = min(best, score)
        return best


def ai_best_move(tasks: List[int], ai_score: int, user_score: int) -> int:
    """
    Evaluates all possible picks for the AI and returns the index of
    the task that leads to the highest net advantage after Minimax search.
    """
    best_val   = -math.inf
    best_index = 0

    for i, task_val in enumerate(tasks):
        remaining  = tasks[:i] + tasks[i+1:]
        score      = minimax(remaining, ai_score + task_val, user_score, False)
        if score > best_val:
            best_val   = score
            best_index = i

    return best_index


# ─────────────────────────────────────────────────────────────────────
# DISPLAY HELPERS
# ─────────────────────────────────────────────────────────────────────

DIVIDER = "─" * 52

def print_header() -> None:
    print("\n" + "=" * 52)
    print("     MINIMAX TASK SELECTION GAME")
    print("     AI uses Decision Tree Search (Minimax)")
    print("=" * 52)

def print_pool(tasks: List[int]) -> None:
    pool_str = "  ".join(f"[{t}]" for t in tasks)
    print(f"  Available Pool : {pool_str if pool_str else '(empty)'}")

def print_scores(user_score: int, ai_score: int,
                 user_tasks: List[int], ai_tasks: List[int]) -> None:
    print(f"  User  — Tasks: {user_tasks}  |  Score: {user_score}")
    print(f"  AI    — Tasks: {ai_tasks}   |  Score: {ai_score}")

def print_turn_banner(turn: int, actor: str) -> None:
    print(f"\n  ┌── Turn {turn}  ({actor}'s pick) " + "─" * (28 - len(actor)))


# ─────────────────────────────────────────────────────────────────────
# GAME LOOP
# ─────────────────────────────────────────────────────────────────────

def get_user_pick(tasks: List[int]) -> Tuple[int, int]:
    """
    Prompts the user to pick a task by its value.
    Returns (index_in_list, task_value).
    """
    while True:
        try:
            print(f"  Your options : {tasks}")
            choice = int(input("  Enter the task value you want to pick: ").strip())
            if choice in tasks:
                idx = tasks.index(choice)
                return idx, choice
            else:
                print("  [!] That value is not in the pool. Try again.")
        except ValueError:
            print("  [!] Please enter a valid integer.")


def play_game(tasks: List[int]) -> None:
    """Main interactive game loop."""

    print_header()
    print(f"\n  Initial Task Pool : {tasks}")
    print(f"  Total tasks       : {len(tasks)}")
    print(f"  User goes FIRST.\n")
    print(DIVIDER)

    pool        : List[int] = list(tasks)
    user_tasks  : List[int] = []
    ai_tasks    : List[int] = []
    user_score  : int       = 0
    ai_score    : int       = 0
    turn        : int       = 1
    is_user_turn: bool      = True   # User always starts first

    while pool:
        print_turn_banner(turn, "User" if is_user_turn else "AI")
        print_pool(pool)

        if is_user_turn:
            # ── User's turn ───────────────────────────────────────────
            idx, picked = get_user_pick(pool)
            pool.pop(idx)
            user_tasks.append(picked)
            user_score += picked
            print(f"\n  ✔  User selects  : {picked}")
        else:
            # ── AI's turn (Minimax) ───────────────────────────────────
            idx   = ai_best_move(pool, ai_score, user_score)
            picked = pool.pop(idx)
            ai_tasks.append(picked)
            ai_score += picked
            print(f"\n  🤖 AI selects    : {picked}  (Minimax optimal)")

        print(f"  Remaining tasks  : {pool}")
        print(f"  {DIVIDER}")
        print_scores(user_score, ai_score, user_tasks, ai_tasks)
        print(f"  {DIVIDER}")

        is_user_turn = not is_user_turn
        turn        += 1

    # ─────────────────────────────────────────────────────────────────
    # FINAL RESULTS
    # ─────────────────────────────────────────────────────────────────
    print("\n" + "=" * 52)
    print("  FINAL RESULTS")
    print("=" * 52)
    print(f"  Tasks picked by User : {user_tasks}")
    print(f"  Tasks picked by AI   : {ai_tasks}")
    print(f"  Remaining tasks      : {pool}  (none)")
    print(DIVIDER)
    print(f"  User Score  =  {user_score}")
    print(f"  AI Score    =  {ai_score}")
    print(DIVIDER)

    if user_score > ai_score:
        print(f"  🏆  USER WINS!  ({user_score} > {ai_score})")
    elif ai_score > user_score:
        print(f"  🤖  AI WINS!    ({ai_score} > {user_score})")
    else:
        print(f"  🤝  IT'S A TIE! ({user_score} = {ai_score})")

    print("=" * 52 + "\n")


# ─────────────────────────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────────────────────────

def main():
    print("\nEnter task priority values (space-separated), or press Enter")
    print("to use the sample input [3, 7, 2, 9, 5]:")
    raw = input("  > ").strip()

    if raw:
        try:
            tasks = list(map(int, raw.split()))
            if not tasks:
                raise ValueError
        except ValueError:
            print("  [!] Invalid input. Using default: [3, 7, 2, 9, 5]")
            tasks = [3, 7, 2, 9, 5]
    else:
        tasks = [3, 7, 2, 9, 5]

    play_game(tasks)


if __name__ == "__main__":
    main()
