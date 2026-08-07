def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = []

    for j in range(cols):
        row = []

        for i in range(rows):
            row.append(matrix[i][j])

        result.append(row)

    return result


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

result = transpose(matrix)

print("Transpose:")

for row in result:
    print(*row)