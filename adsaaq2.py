def matrix_chain_multiplication(matrices):
    n = len(matrices)
    dp = [[0] * n for _ in range(n)]
    parenthesization = [[0] * n for _ in range(n)]

    for length in range(2, n):
        for i in range(1, n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + matrices[i - 1][0] * matrices[k][1] * matrices[j][1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    parenthesization[i][j] = k

    return parenthesization, dp[1][n - 1]

def print_optimal_parenthesization(parenthesization, i, j):
    if i == j:
        print(f"Matrix {i}", end="")
        return
    print("(", end="")
    print_optimal_parenthesization(parenthesization, i, parenthesization[i][j])
    print_optimal_parenthesization(parenthesization, parenthesization[i][j] + 1, j)
    print(")", end="")

# Example usage
matrices = [(2, 3), (3, 4), (4, 2)]
parenthesization, min_scalar_multiplications = matrix_chain_multiplication(matrices)
print("Optimal Parenthesization:")
print_optimal_parenthesization(parenthesization, 1, len(matrices) - 1)
print("\nMinimum Scalar Multiplications:", min_scalar_multiplications)
