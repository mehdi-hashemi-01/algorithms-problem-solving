#1707.Unique Number of Occurrences

arr = [1, 2, 2, 1, 1, 3, 3]

freq = {}
for i, num in enumerate(arr):
    freq[num] = freq.get(num, 0) + 1

seen = set()
result = True

for count in freq.values():
    if count in seen:
        result = False
        break
    seen.add(count)

print(result)

# counts = Counter(arr).values()
# return len(set(counts)) == len(counts)