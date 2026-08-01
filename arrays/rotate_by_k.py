def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def left_rotate(arr, k):
    n = len(arr)
    k = k % n

    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    reverse(arr, 0, n - 1)

    return arr


#method 2
def left_rotate(arr, k):
    n = len(arr)
    k = k % n

    return arr[k:] + arr[:k]


arr = list(map(int, input("Enter the array elements: ").split()))
k = int(input("Enter the value of k: "))

print("Array after left rotation:")
print(left_rotate(arr, k))