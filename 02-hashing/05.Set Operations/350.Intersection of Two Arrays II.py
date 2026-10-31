#350. Intersection of Two Arrays II
from collections import Counter

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

ans=[]
nums1.sort()
nums2.sort()
n1=len(nums1)
n2=len(nums2)
i=0
j=0
while i<n1 and j<n2:
    if nums1[i]==nums2[j]:
        ans.append(nums2[j])
        i += 1
        j += 1
    elif nums1[i]>nums2[j]:
        j+=1
    else:
        i += 1
print(ans)

# شمارش تعداد تکرار اعداد لیست اول
count1 = Counter(nums1)

# شمارش تعداد تکرار اعداد لیست دوم
count2 = Counter(nums2)

# پیدا کردن اعداد مشترک با حداقل تعداد تکرار
common = count1 & count2

# تبدیل نتیجه به لیست با حفظ تکرارها
result = list(common.elements())

print(result)