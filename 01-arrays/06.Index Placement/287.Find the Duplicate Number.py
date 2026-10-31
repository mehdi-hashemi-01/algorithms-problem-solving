#287.Find the Duplicate Number
nums = [1, 3, 4, 2, 2, 3, 5, 5]

# i = 0
#
# while i < len(nums):
#     if nums[i] != i + 1:
#         correct_index = nums[i] - 1
#
#         if nums[i] == nums[correct_index]:
#             return nums[i]
#
#         nums[i], nums[correct_index] = nums[correct_index], nums[i]
#
#     else:
#         i += 1

seen = set()
duplicates = set()

for num in nums:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(duplicates)

# slow = nums[0]
# fast = nums[0]

# مرحله اول: پیدا کردن نقطه برخورد داخل چرخه
# while True:
#     slow = nums[slow]
#     fast = nums[nums[fast]]
#
#     if slow == fast:
#         break
#
# # مرحله دوم: پیدا کردن شروع چرخه
# slow = nums[0]
#
# while slow != fast:
#     slow = nums[slow]
#     fast = nums[fast]
#
# return slow