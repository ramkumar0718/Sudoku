def main(board):
    empty = find_empty(board)
    if not empty:
        return True
    else:
        row, col = empty

    for i in range(1, 10):
        if check(board, i, (row, col)):
            board[row][col] = i
            if main(unsolved_board):
                return True
            board[row][col] = 0
    return False

def check(board, num, pos):
    for i in range(len(board)):
        if board[i][pos[1]] == num and i != pos[0]:
            return False

    for i in range(len(board[0])):
        if board[pos[0]][i] == num and i != pos[1]:
            return False                                    

    x_box = pos[0] // 3
    y_box = pos[1] // 3

    for i in range(x_box * 3, x_box * 3 + 3):
        for j in range(y_box * 3, y_box * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def print_board(message, board):
    print(f"\n{message}")
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("\n-------------------------------", end=" ")
        print()
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end=" ")
            print(board[i][j], "", end=" ")


unsolved_board = [
    [0, 2, 0, 6, 0, 8, 0, 0, 0],
    [5, 8, 0, 0, 0, 9, 7, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 0],
    [3, 7, 0, 0, 0, 0, 5, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 8, 0, 0, 0, 0, 1, 3],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 9, 8, 0, 0, 0, 3, 6],
    [0, 0, 0, 3, 0, 6, 0, 9, 0]
]

print_board("Unsolved Board:", unsolved_board)
main(unsolved_board)
print_board("\nSolved Board:", unsolved_board)