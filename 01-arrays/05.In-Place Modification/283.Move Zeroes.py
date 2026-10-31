#283. Move Zeroes

nums = [0,1,0,3,12]
n = len(nums)

if not nums:
    print(0)

# i = 0
#
# while i < n:
#     if nums[i] == 0:
#         for j in range(i,n-1):
#              nums[j] = nums[j+1]
#         nums[n-1] = 0
#         n -= 1
#     else:
#         i += 1
# print(nums)
if not nums:
    print(0)

write = 0
for read in range(len(nums)):
    if nums[read] != 0:
        nums[write] = nums[read]
        write += 1

for i in range(write, len(nums)):
    nums[i] = 0
print(nums)