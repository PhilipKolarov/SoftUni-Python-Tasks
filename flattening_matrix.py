n = int(input())
output_list0 = []

for i in range(n):
    input_list = [int(x) for x in input().split(", ")]
    for x in input_list:
        output_list0.append(x)

print(output_list0)
