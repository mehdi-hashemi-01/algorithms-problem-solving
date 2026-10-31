matrix = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
    [13,14, 15, 16]
]

rows = len(matrix)
cols = len(matrix[0])

for i in range(rows):
    for j in range(cols):
        if i == j:
            print(matrix[i][j], end=" ")

print("")
print("----------------------------")

for i in range(min(rows, cols)):
    print(matrix[i][i], end=" ")