#238. Product of Array Except Self


# nums = [1, 2, 3, 4]
#
# n = len(nums)
#
# answer = [1] * n
#
# for i in range(n):
#     product = 1
#
#     for j in range(n):
#         if i != j:
#             product *= nums[j]
#
#     answer[i] = product
#
# print(answer)
#
#
#
# nums = [1, 2, 3, 4]
#
# n = len(nums)
#
# prefix = [1] * n
# suffix = [1] * n
# answer = [1] * n
#
#
# # ساخت Prefix
# for i in range(1, n):
#     prefix[i] = prefix[i - 1] * nums[i - 1]
#
#
# # ساخت Suffix
# for i in range(n - 2, -1, -1):
#     suffix[i] = suffix[i + 1] * nums[i + 1]
#
#
# # طبق فرمول اصلی
# for i in range(n):
#     answer[i] = prefix[i] * suffix[i]
#
#
# print("prefix =", prefix)
# print("suffix =", suffix)
# print("answer =", answer)

# nums = [1,2,3,4]
#
# n = len(nums)
#
# answer = [1] * n
#
# left_product = 1
#
# for i in range(n):
#     answer[i] = left_product
#     left_product *= nums[i]
#
# right_product = 1
#
# for i in range(n - 1, -1, -1):
#     answer[i] *= right_product
#     right_product *= nums[i]
#
# print(answer)



# left_max[i]
# =
# max(left_max[i - 1], nums[i - 1])
# max(float('-inf'), 3)


# right_max[i]
# =
# max(right_max[i + 1], nums[i + 1])



nums = [3, 1, 4, 2, 5, 1]

n = len(nums)

left_max = [float('-inf')] * n
right_max = [float('-inf')] * n
answer = [0] * n


# ساخت Prefix Maximum
for i in range(1, n):
    left_max[i] = max(
        left_max[i - 1],
        nums[i - 1]
    )


# ساخت Suffix Maximum
for i in range(n - 2, -1, -1):
    right_max[i] = max(
        right_max[i + 1],
        nums[i + 1]
    )


# ترکیب چپ و راست
for i in range(n):
    answer[i] = max(
        left_max[i],
        right_max[i]
    )


print("left_max =", left_max)
print("right_max =", right_max)
print("answer =", answer)