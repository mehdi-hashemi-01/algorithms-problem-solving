source = "paper"
target = "title"

mapping = {}
result = []

for value in source:
    if value not in mapping:
        mapping[value] = len(mapping)

    result.append(mapping[value])

print(result)