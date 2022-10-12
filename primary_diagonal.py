n = int(input())
matrix = []
primary_diagonal_sum = 0

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

for i in range(n):
    primary_diagonal_sum += matrix[i][i]

print(primary_diagonal_sum)
