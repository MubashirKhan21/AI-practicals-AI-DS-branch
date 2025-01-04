def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n")

def is_safe(board, row, col, N):
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == "Q":
            return False
    
    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False
    
    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False
    
    return True

def solve_queens_util(board, col, N):
    if col >= N:
        print_board(board)
        return True
    
    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = "Q"
            res = solve_queens_util(board, col + 1, N) or res
            board[i][col] = "."  # Backtrack if placing a queen doesn't lead to a solution
    
    return res

def solve_queens(N):
    board = [["." for _ in range(N)] for _ in range(N)]
    if not solve_queens_util(board, 0, N):
        print("No solution exists.")

# Example usage
if __name__ == "__main__":
    N = 8  # Size of the chessboard
    solve_queens(N)
