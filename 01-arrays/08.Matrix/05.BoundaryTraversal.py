matrix = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
    [13,14, 15, 16]
]

rows = len(matrix)
cols = len(matrix[0])

# بالا
for j in range(cols):
    print(matrix[0][j], end=" ")

# راست
for i in range(1, rows):
    print(matrix[i][cols-1], end=" ")

# پایین
for j in range(cols-2, -1, -1):
    print(matrix[rows-1][j], end=" ")

# چپ
for i in range(rows-2, 0, -1):
    print(matrix[i][0], end=" ")