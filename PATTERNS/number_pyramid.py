def number_pyramid(n):
    for i in range(1, n + 1):

        # Spaces
        for j in range(n - i):
            print(" ", end="")

        # Numbers
        for j in range(1, 2 * i):
            print(j, end="")

        print()


n = int(input("Enter number of rows: "))
number_pyramid(n)