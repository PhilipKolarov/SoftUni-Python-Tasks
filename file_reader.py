#print(sum([int(x) for x in opne('./numbers.txt', 'r')])) - bad practice!!!

file = open('./numbers.txt', 'r')
sum = 0

for line in file:
    sum += int(line)

print(sum)