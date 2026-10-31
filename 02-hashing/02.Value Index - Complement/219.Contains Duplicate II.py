#219. Contains Duplicate II

nums = [1, 2, 3, 1]
k = 3
last = {}
# for i, num in enumerate(nums):
#     if num in last and i-last[num] <= k:
#         return True
#     last[num] = i
# return False


# if (len(nums)==len(set(nums))):
#     return False
#
# hmp={}
# for i,j in enumerate(nums):
#     if j in hmp and (i-hmp[j])<=k:
#         return True
#     hmp[j]=i
# return False


# if len(set(nums)) == len(nums):
#     return False
#
# seen = {}
# for i, n in enumerate(nums):
#     if n in seen and i - seen[n] <= k:
#         return True
#     else:
#         seen[n] = i
#
# return False