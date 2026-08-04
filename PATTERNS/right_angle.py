def rtriangle(n):
    for i in range(1, n+1):
        for j in range(1,i+1):
            print(j, end='')  #for numbers not *
        print()

n = int(input("n:"))
rtriangle(n)