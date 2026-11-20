#451. Sort Characters By Frequency
s = "tree"

freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

chars = sorted(freq, key=freq.get, reverse=True)

parts = []
for ch in chars:
    parts.append(ch*freq[ch])

print("".join(parts))


# ans=[]
# for char in set(s):
#     count=s.count(char)
#     ans.append(char*count)
# ans.sort(key=len, reverse=True)
# return "".join(ans)