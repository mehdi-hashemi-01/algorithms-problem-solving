#1002. Find Common Characters

from collections import Counter

words = ["bella","label","roller"]

common = Counter(words[0])
for word in words[1:]:
    current = Counter(word)
    common = common & current
result = list(common.elements())

print(result)

result = []
for char in range(ord('a'), ord('z') + 1):
    char = chr(char)
    min_count = float('inf')
    for word in words:
        count = word.count(char)
        min_count = min(min_count, count)
        if min_count == 0:
            break
    result.extend([char] * min_count)

print(result)


common = Counter(words[0])
for word in words[1:]:
    common &= Counter(word)

print(list(common.elements()))