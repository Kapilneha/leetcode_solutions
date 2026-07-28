def removeElement(nums, val):

    j = 0

    for i in range(len(nums)):

        if nums[i] != val:
            nums[j] = nums[i]
            j += 1

    return j


nums = list(map(int, input("Enter numbers: ").split()))
val = int(input("Enter value to remove: "))

k = removeElement(nums, val)

print("Number of remaining elements:", k)
print("Updated array:", nums)
print("Valid elements:", nums[:k])