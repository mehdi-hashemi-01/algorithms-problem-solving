#303. Range Sum Query - Immutable

nums = [-2, 0, 3, -5, 2, -1]
left = 2
right = 5

prefix_sum = [0,]
for i in range(0, len(nums)):
     prefix_sum.append(prefix_sum[i] + nums[i])

answer = prefix_sum[right + 1] - prefix_sum[left]
print(answer)