nums = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target: "))

hashmap = {}

for i in range(len(nums)):
    complement = target - nums[i]

    if complement in hashmap:
        print("Answer:", [hashmap[complement], i])
        break

    hashmap[nums[i]] = i