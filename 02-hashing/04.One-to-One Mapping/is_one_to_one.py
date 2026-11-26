source = ["a", "b", "b", "a"]
target = ["x", "y", "y", "x"]

result = True
if len(source) != len(target):
    result = False

forward = {}
reverse = {}

for a, b in zip(source, target):

    if a in forward:
        if forward[a] != b:
            result = False
            break

    if b in reverse:
        if reverse[b] != a:
            result = False
            break

    forward[a] = b
    reverse[b] = a

print(result)
print(forward)
print(reverse)