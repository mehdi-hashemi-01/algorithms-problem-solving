#27. Remove Element

nums = [2, 3, 2, 2, 3]
val = 3

n = len(nums)
i = 0

#Brute Force
while i < n:
    if nums[i] == val:
        for j in range(1, n - 1):
            nums[j] = nums[j + 1]

        n -= 1
    else:
        i += 1

print(n)
print(nums)


# write = 0
#
# for read in range(len(nums)):
#     if nums[read] != val:
#         nums[write] = nums[read]
#         write += 1
#
# print(write)
# print(nums)


