#485. Max Consecutive Ones

nums = [1,1,0,1,0,1,1,1,1]

count = 0
best = 0

for num in nums:
    if num == 1:
        count += 1
    else:
        count = 0 

    if count > best:
        best = count


print(best)