def containsDuplicate(nums):

    seen = set()

    for num in nums:

        if num in seen:
            return True

        seen.add(num)

    return False


nums = list(map(int, input("Enter numbers: ").split()))

print(containsDuplicate(nums))


# method 2 
def containsDuplicate(nums):

    seen = set(nums)

    if len(seen) == len(nums):
        return False

    return True