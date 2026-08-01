def second_largest(arr):
    largest = float('-inf')
    second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest

arr = list(map(int, input("enter:").split()))
print(second_largest(arr))