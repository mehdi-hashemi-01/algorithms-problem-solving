matrix = [[1,2,3],[4,5,6],[7,8,9]]

n = len(matrix)

for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print(matrix)



# matrix = [[1,2,3],[4,5,6],[7,8,9]]
#
# n = len(matrix)
# m = len(matrix[0])
#
# # result = [[0] * n for _ in range(m)]
# result = []
#
# for i in range(m):
#     row = []
#
#     for j in range(n):
#         row.append(0)
#
#     result.append(row)
#
# for i in range(n):
#     for j in range(m):
#         result[j][i] = matrix[i][j]
#
# print(result)