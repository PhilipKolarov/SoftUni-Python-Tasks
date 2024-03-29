n = int(input())

matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split(', ')])

primary_diagonal = []
for i in range(n):
    primary_diagonal.append(matrix[i][i])

secondary_diagonal = []
for i in range(n):
    secondary_diagonal.append(matrix[i][n - 1 - i])

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")