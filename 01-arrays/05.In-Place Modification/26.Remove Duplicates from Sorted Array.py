# 26.Remove Duplicates from Sorted Array

nums = [1, 1, 2]

n = len(nums)

# if n == 0:
#     print(0)
#
# i = 1
#
# while i < n:
#     if nums[i] == nums[i - 1]:
#         for j in range(i, n - 1):
#             nums[j] = nums[j + 1]
#
#         n -= 1
#     else:
#         i += 1
#
#     print(n)


if not nums:
    print(0)

write = 1

for read in range(1, len(nums)):
    if nums[read] != nums[write - 1]:
        nums[write] = nums[read]
        write += 1

print(write)