data = [int(x) for x in input().split(', ')]
columns = data[0]
rows = data[1]
total_sum = 0
main_list = []

for _ in range(columns):
    column_list = [int(x) for x in input().split(', ')]
    for i in range(rows):
        total_sum += column_list[i]
    main_list.append(column_list)

print(total_sum)
print(main_list)
