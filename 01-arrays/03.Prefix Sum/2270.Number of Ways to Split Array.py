#2270. Number of Ways to Split Array

nums = [10, 4, -8, 7]

total_sum = sum(nums)
left_sum = 0
count = 0

for num in nums[:-1]:
    left_sum += num
    right_sum = total_sum - left_sum

    if left_sum >= right_sum:
        count += 1



print(count)