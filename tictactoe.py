def print_board(board):
    print("---------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("---------")

def check_win(board, player):
    # בדיקות שורות
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # בדיקות עמודות
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # בדיקה אלכסון ראשי
    if all([board[i][i] == player for i in range(3)]):
        return True
    # בדיקת אלכסון משני
    if all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def board_full(board):
    return all([cell != " " for row in board for cell in row])

def tictactoe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        print(f"תור של {current_player}.")
        try:
            row = int(input("הכנס מספר שורה (1-3): ")) - 1
            col = int(input("הכנס מספר עמודה (1-3): ")) - 1
        except ValueError:
            print("קלט לא חוקי, נסה שוב.")
            continue
        if row not in range(3) or col not in range(3):
            print("שורה או עמודה לא חוקית, נסה שוב.")
            continue
        if board[row][col] != " ":
            print("תא תפוס, נסה שוב.")
            continue
        board[row][col] = current_player
        if check_win(board, current_player):
            print_board(board)
            print(f"כל הכבוד! השחקן {current_player} ניצח!")
            break
        if board_full(board):
            print_board(board)
            print("תיקו!")
            break
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tictactoe()