#1572. Matrix Diagonal Sum

mat = [[1,2,3], [4,5,6], [7,8,9]]
# mat = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]

total = 0
n = len(mat)
for i in range(n):
    total += mat[i][i]
    if i != n - 1 - i:
        total += mat[i][n-i-1]

print(total)

