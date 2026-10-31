#771. Jewels and Stones

jewels = "aA"
stones = "aAAbbbb"

jewel_set = set(jewels)
count = 0
for letter in stones:
    if letter in jewel_set:
        count += 1
# return count
print(count)

