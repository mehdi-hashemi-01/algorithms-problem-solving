#2574. Left and Right Sum Differences

nums = [10,4,8,3]
#Output: [15,1,11,22]

total_sum = sum(nums)
left_sum = 0
for i, num in enumerate(nums):
    right_sum = total_sum - left_sum - num
    nums[i] = abs(right_sum-left_sum)
    left_sum += num

print(nums)