nums = [2,7,11,15]
target = 9

seen = {}
find = 0

for i, num in enumerate(nums):
    complement = target - num

    if complement in seen:
        find = [seen[complement], i]

    seen[num] = i

print(find)



# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print([i, j])
