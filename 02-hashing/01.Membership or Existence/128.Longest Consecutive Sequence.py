#128. Longest Consecutive Sequence

nums = [100,4,200,1,3,2]

value = set(nums)
longest = 0

for x in nums:
    if x-1 not in value:
        current = x
        length = 1

        while current + 1 in value:
            current += 1
            length += 1

        longest = max(longest, length)
        # longest = max(longest, current - x)

print(longest)


# if not nums:
#     print(0)
#
# nums = list(set(nums))
# nums.sort()
# cnt = 1
# maxi = 1
#
# for i in range(len(nums) - 1):
#     if nums[i + 1] - nums[i] == 1:
#         cnt += 1
#         maxi = max(maxi, cnt)
#     else:
#         cnt = 1