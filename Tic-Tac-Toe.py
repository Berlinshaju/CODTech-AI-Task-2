import sys

# Constants representing the marks on the board
EMPTY = "-"
PLAYER_X = "X"
PLAYER_O = "O"

# Function to print the current board
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

# Function to check if the board is full
def is_full(board):
    return all(cell != EMPTY for row in board for cell in row)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to evaluate the board for the AI player
def evaluate(board):
    if check_winner(board, PLAYER_X):
        return 10
    elif check_winner(board, PLAYER_O):
        return -10
    else:
        return 0

# Minimax algorithm with Alpha-Beta Pruning for AI player
def minimax(board, depth, alpha, beta, is_maximizing):
    score = evaluate(board)
    if score == 10 or score == -10 or is_full(board):
        return score

    if is_maximizing:
        max_eval = -sys.maxsize
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth + 1, alpha, beta, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = sys.maxsize
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth + 1, alpha, beta, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move for the AI player
def find_best_move(board):
    best_eval = -sys.maxsize
    best_move = (-1, -1)
    alpha = -sys.maxsize
    beta = sys.maxsize
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                eval = minimax(board, 0, alpha, beta, False)
                board[i][j] = EMPTY
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Main function to play the game
def play_game():
    board = [[EMPTY]*3 for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    while not is_full(board):
        # Player's move
        row, col = map(int, input("Enter row and column (0-2): ").split())
        if board[row][col] != EMPTY:
            print("Cell already taken. Try again.")
            continue
        board[row][col] = PLAYER_O
        print_board(board)
        if check_winner(board, PLAYER_O):
            print("Congratulations! You win!")
            return
        if is_full(board):
            print("It's a draw!")
            return
        # AI's move
        print("AI is thinking...")
        ai_row, ai_col = find_best_move(board)
        board[ai_row][ai_col] = PLAYER_X
        print_board(board)
        if check_winner(board, PLAYER_X):
            print("AI wins! Better luck next time.")
            return
        if is_full(board):
            print("It's a draw!")
            return

# Run the game
if __name__ == "__main__":
    play_game()
