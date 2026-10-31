#41. First Missing Positive

nums = [1, -1, 3, 4]

seen = set(nums)
for i in range(1, 2 ** 31):
    if i not in seen: print(i)