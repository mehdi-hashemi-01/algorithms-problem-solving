#1413. Minimum Value to Get Positive Step by Step Sum

nums = [-3,2,-3,4,2]

total_sum = 0
min_sum = 0

for num in nums:
    total_sum  += num
    min_sum = min(min_sum, total_sum)

startValue  = 1 - min_sum
print(startValue)
