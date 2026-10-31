#2032. Two Out of Three

nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
#Output: [3,2]


n1 = set(nums1)
n2 = set(nums2)
n3 = set(nums3)
print(list(n1 & n2 | n2 & n3 | n3 & n1))



set1 = set(nums1)
set2 = set(nums2)
set3 = set(nums3)

# اعداد مشترک بین لیست اول و دوم
common12 = set1 & set2

# اعداد مشترک بین لیست اول و سوم
common13 = set1 & set3

# اعداد مشترک بین لیست دوم و سوم
common23 = set2 & set3

# اجتماع تمام اعداد مشترک
result = common12 | common13 | common23

# تبدیل مجموعه به لیست
print(list(result))