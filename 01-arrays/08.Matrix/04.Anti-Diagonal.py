matrix = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
    [13,14, 15, 16]
]

#column + row = n - 1
#column = n - 1 - row

n = len(matrix)

for i in range(n):
    print(matrix[i][n-1-i], end=" ")