#189. Rotate Array

nums = [1,2,3,4,5,6,7]
k = 3

# n = len(nums)
#
# if n == 0:
#     print(0)
#
# k %= n
#
# for _ in range(k):
#     last = nums[n - 1]
#
#     for i in range(n - 1, 0, -1):
#         nums[i] = nums[i - 1]
#
#     nums[0] = last
#
# print(nums)


# n = len(nums)
#
# if n == 0:
#     print(0)
#
# k %= n
#
# result = [0] * n
#
# for i in range(n):
#     new_index = (i + k) % n
#     result[new_index] = nums[i]
#     # result[(i + k) % n] = nums[i]
#
# # nums[:] = result
# for i in range(n):
#     nums[i] = result[i]


# n = len(nums)
#
# if n == 0:
#     print(0)
#
# k %= n
#
# nums.reverse()
# nums[:k] = reversed(nums[:k])
# nums[k:] = reversed(nums[k:])


n = len(nums)
k %= n

def reverse(left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

reverse(0, n - 1)   # برعکس کردن کل آرایه
reverse(0, k - 1)   # برعکس کردن k عنصر اول
reverse(k, n - 1)   # برعکس کردن بقیه