#242.Valid Anagram

s = "anagram"
t = "nagaram"

result = True
if len(s) != len(t):
    result = False

freq = {}
for ch in s:
    freq[ch] = freq.get(ch,0)+1

for ch in t:
    if freq.get(ch,0) == 0:
        result = False
    freq[ch] -= 1

print(result)

# if len(s) != len(t):
#     return False
#
# l = list(set(s))
# for i in l:
#     if s.count(i) != t.count(i):
#         return False
# return True