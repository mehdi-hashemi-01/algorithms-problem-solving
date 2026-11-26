s = "egg"
t = "add"

forward = {}
reverse = {}
is_isomorphic = True

if len(s) != len(t):
    is_isomorphic = False
else:
    for a, b in zip(s, t):
        if a in forward and forward[a] != b:
            is_isomorphic = False
            break

        if b in reverse and reverse[b] != a:
            is_isomorphic = False
            break

        forward[a] = b
        reverse[b] = a

print(is_isomorphic)

# return len(set(s)) == len(set(t)) == len(set(zip(s, t)))

# HashS = {}
# for sc, tc in zip(s,t):
#     if sc in HashS:
#         if HashS[sc]!=tc:
#             return False
#     elif tc in HashS.values():
#         return False
#     HashS[sc]=tc
# return True