from collections import deque

water_quantity = int(input())
people = deque()
while True:
    command = input()
    if command == "Start":
        break
    people.append(command)

while True:
    command = input()
    if command == "End":
        break

    if command.startswith("refill "):
        params = command.split(" ")
        water_quantity += int(params[1])
    else:
        person = people.popleft()
        water_needed = int(command)

        if water_needed <= water_quantity:
            print(f'{person} got water')
            water_quantity -= water_needed
        else:
            print(f"{person} must wait")

print(f"{water_quantity} liters left")
