#350.Intersection of Two Arrays II
from collections import Counter

nums1 = [1, 2, 2, 1]
nums2 = [2, 1, 2]

if len(nums1) > len(nums2):
    nums1, nums2 = nums2, nums1

freq = {}
for x in nums1:
    freq[x] = freq.get(x, 0) + 1

result = []
for x in nums2:
    if freq.get(x, 0) > 0:
        result.append(x)
        freq[x] -= 1

print(result)


# count1 = Counter(nums1)
# count2 = Counter(nums2)
# common = count1 & count2
# result = list(common.elements())