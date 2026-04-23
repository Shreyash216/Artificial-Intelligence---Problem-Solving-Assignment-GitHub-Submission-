import math

board = [' ' for _ in range(9)]

def print_board():
    print("\n")
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])
    print("\n")

def is_winner(player):
    win_positions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    return any(all(board[i] == player for i in pos) for pos in win_positions)

def minimax(is_maximizing):
    if is_winner('O'):
        return 1
    if is_winner('X'):
        return -1
    if ' ' not in board:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    best_move = 0

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = 'O'

while True:
    print_board()

    move = input("Enter position (1-9): ")

    if not move.isdigit():
        print("Enter a number!")
        continue

    move = int(move) - 1   # 🔥 important change

    if move < 0 or move > 8 or board[move] != ' ':
        print("Invalid move!")
        continue

    board[move] = 'X'

    if is_winner('X'):
        print_board()
        print("You win!")
        break

    if ' ' not in board:
        print_board()
        print("Draw!")
        break

    ai_move()

    if is_winner('O'):
        print_board()
        print("AI wins!")
        break