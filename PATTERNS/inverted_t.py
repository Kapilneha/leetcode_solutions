def inverted(n):
    for i in range(n , 0, -1):
        for j in range(i):
            print("*", end='')
        print()

n = int(input("n:"))
print(inverted(n))
