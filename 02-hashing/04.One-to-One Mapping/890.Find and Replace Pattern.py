#890.Find and Replace Pattern

words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern = "abb"

# Build the pattern signature
mapping = {}
pattern_numbers = []

for letter in pattern:
    if letter not in mapping:
        mapping[letter] = len(mapping)

    pattern_numbers.append(mapping[letter])

answer = []

for word in words:
    # Build a fresh signature for each word
    mapping = {}
    word_numbers = []

    for letter in word:
        if letter not in mapping:
            mapping[letter] = len(mapping)

        word_numbers.append(mapping[letter])

    if word_numbers == pattern_numbers:
        answer.append(word)

print(answer)


# def matches(word, pattern):
#     pattern_to_word = {}
#     word_to_pattern = {}
#
#     for p, w in zip(pattern, word):
#
#         if p in pattern_to_word:
#             if pattern_to_word[p] != w:
#                 return False
#
#         if w in word_to_pattern:
#             if word_to_pattern[w] != p:
#                 return False
#
#         pattern_to_word[p] = w
#         word_to_pattern[w] = p
#
#     return True
#
#
# result = []
#
# for word in words:
#     if matches(word, pattern):
#         result.append(word)
#
# return result