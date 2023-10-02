def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 'Q':
            return False
    
    return True

def solve_n_queens_util(board, row, N, solutions):
    if row == N:
        solutions.append([''.join(row) for row in board])
        return
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 'Q'
            solve_n_queens_util(board, row + 1, N, solutions)
            board[row][col] = '.'  # backtrack

def solve_n_queens(N):
    board = [['.' for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_n_queens_util(board, 0, N, solutions)
    return solutions

# Example usage
N = 4
solutions = solve_n_queens(N)
for solution in solutions:
    print('\n'.join(solution))
    print()
