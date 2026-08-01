def find_missing(arr):
    n = len(arr)+1
    total = n*(n+1) // 2
    original = sum(arr)
    return total - original
arr = list(map(int, input("enter:").split()))
print(find_missing(arr))