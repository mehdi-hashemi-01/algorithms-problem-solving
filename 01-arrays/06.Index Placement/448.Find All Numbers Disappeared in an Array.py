#448. Find All Numbers Disappeared in an Array

nums = [4,3,2,7,8,2,3,1]

# seen = set(nums)
# result = []
# for num in range(1, len(nums)+1):
#     if num not in seen:
#         result.append(num)
#
# print(result)


for i in range(len(nums)):
    num = abs(nums[i])
    index = num - 1

    nums[index] = -abs(nums[index])

result = []

for i in range(len(nums)):
    if nums[i] > 0:
        result.append(i + 1)

print(result)
# n=len(nums)
# s=set(nums)
# ans=[]
# for i in range(1,n+1):
#     if i not in s:
#         ans.append(i)