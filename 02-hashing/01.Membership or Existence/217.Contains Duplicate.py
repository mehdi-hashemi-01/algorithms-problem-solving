#217. Contains Duplicate

# nums = [1,2,3,1]
nums = [1,2,3,4]

seen = set()
state = False
for num in nums:
    if num not in seen:
        seen.add(num)
    else:
        state = True

print(state)

# seen = set()
# for num in nums:
#     if num in seen:
#         return True
#     seen.add(num)
#
# return False


# len(set(nums)) < len(nums)

# len(set(nums))!=len(nums)