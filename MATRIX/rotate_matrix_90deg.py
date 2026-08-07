#1. Transpose the matrix
#2. Reverse every row
def rotate_matrix(matrix):
    n = len(matrix)

    # Step 1: Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

    return matrix


n = int(input("Enter matrix size: "))

matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

result = rotate_matrix(matrix)

print("Rotated matrix:")
for row in result:
    print(*row)