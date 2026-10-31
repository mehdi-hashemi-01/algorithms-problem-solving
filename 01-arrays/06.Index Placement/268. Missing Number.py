# 268. Missing Number
nums = [3,0,1]

# seen = set(nums)
# for i in range(len(nums)+1):
#     if i not in seen:
#         print(i)
#         break



i = 0
n = len(nums)

while i < n:
    value = nums[i]

    if nums[i] != i:
        nums[i], nums[value] = nums[value], nums[i]
    else:
        i += 1

missing = n

for i in range(n):
    if nums[i] != i:
        missing = i
        break

print(missing)