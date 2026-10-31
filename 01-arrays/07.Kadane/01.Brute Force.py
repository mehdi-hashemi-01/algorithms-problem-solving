nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_sum = 0
best = nums[0]

for start in range(len(nums)):
    current_sum = 0

    for end in range(start, len(nums)):
        current_sum += nums[end]
        best = max(best, current_sum)

print(best)