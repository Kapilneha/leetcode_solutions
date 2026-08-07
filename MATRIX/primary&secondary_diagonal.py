def diagonal(matrix):
    n=len(matrix)
    print("primary")
    for i in range(n):
        print(matrix[i][i], end=' ')
    print()

    print("secondary")
    for i in range(n):
        print(matrix[i][n-1-i], end=' ')
    print()

n = int(input("enter the size:"))
matrix=[]
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
print(diagonal(matrix))   