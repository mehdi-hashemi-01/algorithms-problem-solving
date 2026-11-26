pattern = "abba"
text = "dog cat cat dog"

words = text.split()

forward = {}
reverse = {}
is_match = True

if len(pattern) != len(words):
    is_match = False
else:
    for letter, word in zip(pattern, words):
        if letter in forward and forward[letter] != word:
            is_match = False
            break

        if word in reverse and reverse[word] != letter:
            is_match = False
            break

        forward[letter] = word
        reverse[word] = letter

print(is_match)