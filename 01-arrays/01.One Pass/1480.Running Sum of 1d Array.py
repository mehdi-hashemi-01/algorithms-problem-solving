# 1480. Running Sum of 1d 01.Array
nums = [1,1,1,1]
# running_sum = 0
# result = []
# for i in nums:
#    running_sum = running_sum + i
#    result.append(running_sum)
# print(result)

for i in range(1, len(nums)):
    nums[i] = nums[i] + nums[i - 1]

print(nums)

