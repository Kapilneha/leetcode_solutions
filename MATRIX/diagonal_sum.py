def diagonal_sum(matrix):
    n = len(matrix)
    total = 0

    for i in range(n):
        total += matrix[i][i]

        if i != n - 1 - i:
            total += matrix[i][n - 1 - i]

    return total


n = int(input("Enter matrix size: "))

matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

print("Diagonal sum:", diagonal_sum(matrix))