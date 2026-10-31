matrix = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
    [13,14, 15, 16]
]

rows = len(matrix)
cols = len(matrix[0])

top = 0
bottom = rows - 1
left = 0
right = cols - 1


result = []

while top <= bottom and left <= right:

    # چپ به راست
    for j in range(left, right + 1):
        result.append(matrix[top][j])

    top += 1

    # بالا به پایین
    for i in range(top, bottom + 1):
        result.append(matrix[i][right])

    right -= 1

    if top <= bottom:

        # راست به چپ
        for j in range(right, left - 1, -1):
            result.append(matrix[bottom][j])

        bottom -= 1

    if left <= right:

        # پایین به بالا
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])

        left += 1

print(result)