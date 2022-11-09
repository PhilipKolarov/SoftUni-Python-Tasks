from collections import deque

materials_seq = [int(x) for x in input().split(' ')]
magic = deque([int(x) for x in input().split(' ')])

crafting_table = {
    150: "Doll",
    250: "Wooden Train",
    300: "Teddy Bear",
    400: "Bicycle"
}

crafted_toys = {}

while materials_seq and magic:
    material = materials_seq.pop()
    value = magic.popleft()

    if material == 0 and value == 0:
        continue

    if material == 0:
        magic.appendleft(value)
        continue

    if value == 0:
        materials_seq.append(material)
        continue

    result = material + value
    if result in crafting_table:
        toy_name = crafting_table[result]
        if toy_name in crafted_toys:
            crafted_toys[toy_name] += 1
        else:
            crafted_toys[toy_name] = 1
        continue

    if result < 0:
        materials_seq.append(material + value)
    else:
        materials_seq.append(material + 15)

print(magic)

if ('Doll' in crafted_toys and 'Wooden train' in crafted_toys) or ('Teddy bear' in crafted_toys and 'Bicycle' in crafted_toys):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials_seq:
    print(f"Materials left: {', '.join([str(x) for x in materials_seq])}")

if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

for toy, count in sorted(crafted_toys.items()):
    print(f"{toy}: {count}")
