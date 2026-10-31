#2215. Find the Difference of Two Arrays

nums1 = [1,2,3]
nums2 = [2,4,6]
#Output: [[1,3],[4,6]]

a = set(nums1)
b = set(nums2)

only_a = list(a - b)
only_b = list(b - a)

print([only_a, only_b])


# answer0=set()
# answer1=set()
# set1 = set(nums1)
# set2 = set(nums2)
# for num in nums1:
#     if not (num in set2):
#         answer0.add(num)
# for num in nums2:
#     if not (num in set1):
#         answer1.add(num)
# return [list(answer0),list(answer1)]