# 442. Find All Duplicates in an Array

nums = [4, 3, 2, 7, 8, 2, 3, 1]

duplicates = []

for i in range(len(nums)):
    value = abs(nums[i])
    index = value - 1

    if nums[index] < 0:
        duplicates.append(value)
    else:
        nums[index] = -nums[index]

print(duplicates)