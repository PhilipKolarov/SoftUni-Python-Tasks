clothes = [int(c) for c in input().split()]

capacity = int(input())
current_capacity = capacity
rack_counter = 1

while clothes:
    current_clothing = clothes[-1]
    if current_clothing > current_capacity:
        rack_counter += 1
        current_capacity = capacity
    else:
        current_capacity -= current_clothing
        clothes.pop()

print(rack_counter)