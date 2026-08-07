def search_matrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])

    i = 0
    j = cols - 1

    while i < rows and j >= 0:

        if matrix[i][j] == target:
            return i, j

        elif matrix[i][j] > target:
            j -= 1

        else:
            i += 1

    return -1


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

target = int(input("Enter target: "))

print(search_matrix(matrix, target))