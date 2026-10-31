#349. Intersection of Two Arrays

nums1 = [1,2,2,1]
nums2 = [2,2]

lookup = set(nums1)
result = set()

for value in nums2:
    if value in lookup:
        result.add(value)
print(list(result))