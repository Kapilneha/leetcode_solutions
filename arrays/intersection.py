def intersection(nums1, nums2):
    set1 = set(nums1)
    result = set()

    for num in nums2:
        if num in set1:
            result.add(num)

    return list(result)


nums1 = list(map(int, input("Enter first array: ").split()))
nums2 = list(map(int, input("Enter second array: ").split()))

print(intersection(nums1, nums2))