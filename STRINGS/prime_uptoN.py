def print_primes(n):
    for num in range(2, n + 1):
        is_prime = True

        i = 2
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1

        if is_prime:
            print(num, end=" ")


n = int(input())
print_primes(n)