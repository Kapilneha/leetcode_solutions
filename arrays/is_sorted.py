def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False

    return True


arr = list(map(int, input("Enter array elements: ").split()))

print(is_sorted(arr))