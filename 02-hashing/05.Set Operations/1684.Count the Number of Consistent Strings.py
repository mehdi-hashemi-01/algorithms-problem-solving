#1684. Count the Number of Consistent Strings

allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
#Output: 7

allowed_set = set(allowed)
count = 0
for word in words:
    if set(word) <= allowed_set:
        count += 1

print(count)


allowed = set(allowed)
count = len(words)

for word in words:
    for char in word:
        if char not in allowed:
            count -= 1
            break

print(count)