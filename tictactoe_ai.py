import sys

# The game board positions are represented by 0-8
# 0 | 1 | 2
# ---------
# 3 | 4 | 5
# ---------
# 6 | 7 | 8

def print_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_winner(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != ' ':
            return board[condition[0]]
    if ' ' not in board:
        return 'Tie'
    return None

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'O':  # AI wins
        return 1
    if winner == 'X':  # Human wins
        return -1
    if winner == 'Tie':
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_score = -float('inf')
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, depth=0, is_maximizing=False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def main():
    print("=" * 45)
    print("🎮 UNBEATABLE TIC-TAC-TOE AI INITIALIZED 🎮")
    print("Positions are numbered 1 to 9 from top-left.")
    print("You are 'X' and the AI is 'O'.")
    print("=" * 45)

    board = [' '] * 9
    print_board([str(i+1) for i in range(9)]) # Print positions guide

    while True:
        # Human player turn
        try:
            move_input = input("Enter your move position (1-9) or 'exit': ").strip().lower()
            if move_input == 'exit':
                print("Game closed. Goodbye!")
                sys.exit()
                
            move = int(move_input) - 1
            if move < 0 or move > 8 or board[move] != ' ':
                print("❌ Invalid move or position already filled. Try again.")
                continue
        except ValueError:
            print("❌ Please enter a valid number between 1 and 9.")
            continue

        board[move] = 'X'
        print_board(board)

        # Check state after user move
        if check_winner(board):
            break

        # AI player turn
        print("🤖 AI is thinking...")
        ai_move = get_best_move(board)
        if ai_move != -1:
            board[ai_move] = 'O'
            print_board(board)

        # Check state after AI move
        if check_winner(board):
            break

    final_result = check_winner(board)
    if final_result == 'Tie':
        print("🤝 It's a Tie! Perfect defense.")
    elif final_result == 'O':
        print("🤖 The AI won! (Minimax calculations make it unbeatable).")
    else:
        print("🎉 You won!") # This shouldn't be possible with Minimax!

if __name__ == "__main__":
    main()