n = int(input())

matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split(' ')])

primary_diagonal = []
for i in range(n):
    primary_diagonal.append(matrix[i][i])

secondary_diagonal = []
for i in range(n):
    secondary_diagonal.append(matrix[i][n - 1 - i])

diff = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(diff)
