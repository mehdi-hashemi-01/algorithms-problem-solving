nums = [4, 7, 9, 1, 6]

min_so_far = nums[0]

for num in nums:
    if num < min_so_far:
        min_so_far = num


print(min_so_far)