from collections import deque

chocolate_seq = [int(x) for x in input().split(', ')]
milk_seq = deque([int(x) for x in input().split(', ')])

milkshakes = 0

while chocolate_seq and milk_seq and milkshakes < 5:
    chocolate = chocolate_seq.pop()
    milk = milk_seq.popleft()

    if chocolate <= 0 and milk <= 0:
        continue

    if chocolate <= 0:
        milk_seq.appendleft(milk)
        continue

    if milk <= 0:
        chocolate_seq.append(chocolate)
        continue

    if chocolate == milk:
        milkshakes += 1
    else:
        milk_seq.append(milk)
        chocolate_seq.append(chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate_seq:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate_seq])}")
else:
    print(f"Chocolate: empty")

if milk_seq:
    print(f"Milk: {', '.join([str(x) for x in milk_seq])}")
else:
    print(f"Milk: empty")
