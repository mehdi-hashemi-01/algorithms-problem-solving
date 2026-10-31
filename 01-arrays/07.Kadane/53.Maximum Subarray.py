#53. Maximum Subarray

# nums = [5,-4,-1,7,8]
# best = nums[0]
#
# for start in range(len(nums)):
#     current_sum = 0
#
#     for end in range(start, len(nums)):
#         current_sum += nums[end]
#         best = max(best, current_sum)
#
# print(best)

nums = [-2,1,-3,4,-1,2,1,-5,4]
# best = nums[0]
#
# best_start = 0
# best_end = 0

# for start in range(len(nums)):
#     current_sum = 0
#
#     for end in range(start, len(nums)):
#         current_sum += nums[end]
#
#         if current_sum > best:
#             best = current_sum
#             best_start = start
#             best_end = end
#
# best_subarray = nums[best_start:best_end + 1]
#
# print(best)
# print(best_subarray)


current_sum = nums[0]
best_sum = nums[0]

temp_start = 0
best_start = 0
best_end = 0

for i in range(1, len(nums)):

    # تصمیم: ادامه بدهیم یا از اینجا شروع کنیم؟
    if nums[i] > current_sum + nums[i]:
        current_sum = nums[i]
        temp_start = i
    else:
        current_sum += nums[i]

    # اگر جواب بهتری پیدا شد
    if current_sum > best_sum:
        best_sum = current_sum
        best_start = temp_start
        best_end = i

best_subarray = nums[best_start:best_end + 1]

print(best_sum)
print(best_subarray)



current_sum = 0
max_sum = nums[0]

for i in range(len(nums)):
    current_sum += nums[i]

    if current_sum > max_sum:
        max_sum = current_sum

    if current_sum < 0:
        current_sum = 0

print(max_sum)

current_sum = nums[0]
best_sum = nums[0]

for i in range(1, len(nums)):
    current_sum = max(nums[i], current_sum + nums[i])
    best_sum = max(best_sum, current_sum)

print(best_sum)