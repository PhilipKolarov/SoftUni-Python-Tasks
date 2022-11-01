number_string = input()

dd = {}

numbers = [float(x) for x in number_string.split(" ")]

for number in numbers:
    if number not in dd:
        dd[number] = 0
    dd[number] += 1

for number, count in dd.items():
    print(f'{number:.1f} - {count} times')