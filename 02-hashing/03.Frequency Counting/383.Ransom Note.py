#383.Ransom Note

ransomNote = "aa"
magazine = "aab"

stock = {}
result = True

for ch in magazine:
    stock[ch] = stock.get(ch, 0) + 1

for ch in ransomNote:
    if stock.get(ch, 0) == 0:
        result = False
    stock[ch] -= 1

print(result)


# unique = set(ransomNote)
#
# for char in unique:
#     if ransomNote.count(char) > magazine.count(char):
#         return False
# return True