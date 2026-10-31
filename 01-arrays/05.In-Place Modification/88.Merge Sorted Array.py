#88. Merge Sorted Array

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

# for i in range(n):
#     nums1[m + i] = nums2[i]
#
# nums1.sort()
#
# print(nums1)

# valid_len = m
#
# for x in nums2:
#
#     pos = 0
#
#     while pos < valid_len and nums1[pos] <= x:
#         pos += 1
#
#     for j in range(valid_len, pos, -1):
#         nums1[j] = nums1[j - 1]
#
#     nums1[pos] = x
#
#     valid_len += 1




i = m - 1          # آخرین عنصر واقعی nums1
j = n - 1          # آخرین عنصر nums2
k = m + n - 1      # آخرین خانه nums1

while i >= 0 and j >= 0:

    if nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1
    else:
        nums1[k] = nums2[j]
        j -= 1

    k -= 1

# اگر چیزی از nums2 باقی مانده باشد
while j >= 0:
    nums1[k] = nums2[j]
    j -= 1
    k -= 1