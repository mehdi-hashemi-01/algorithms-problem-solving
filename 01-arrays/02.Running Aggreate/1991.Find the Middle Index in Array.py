nums = [1,-1,4]

total_sum = sum(nums)

left_sum = 0
middle_index = -1

for i, num in enumerate(nums):

    right_sum = total_sum - left_sum - num

    if left_sum == right_sum:
        middle_index = i
        break

    left_sum += num

print(middle_index)