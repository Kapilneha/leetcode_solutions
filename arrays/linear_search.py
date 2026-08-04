def linear(arr, target):
    for num in arr:
        if num == target:
            return "FOUND"

    return -1

arr = list(map(int, input("arr:").split()))
target = int(input("target:"))
print(linear(arr, target))