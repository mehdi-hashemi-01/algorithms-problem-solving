#724. Find Pivot Index

nums = [1,7,3,6,5,6]

PivotIndex = -1

# for i in range(len(nums)):
#     left_sum = sum(nums[:i])
#     right_sum = sum(nums[i + 1:])
#
#     if left_sum == right_sum:
#         PivotIndex = i
#         break
#
# print(PivotIndex)

total_sum = sum(nums)
left_sum = 0

for i, num in enumerate(nums):
    right_sum = total_sum - left_sum - num

    if right_sum == left_sum:
        PivotIndex = i
        break

    left_sum += nums[i]

print(PivotIndex)