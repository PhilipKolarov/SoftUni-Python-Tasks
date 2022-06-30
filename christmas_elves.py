from collections import deque

elf_energies = deque([int(x) for x in input().split(' ')])
boxes = [int(x) for x in input().split(' ')]

turns = 0
toys_made = 0
total_energy = 0

while boxes and elf_energies:
    turns += 1

    while elf_energies and elf_energies[0] < 5:
        elf_energies.popleft()

    if not elf_energies:
        break

    box = boxes.pop()
    elf_energy = elf_energies.popleft()

    toys_to_be_created_count = 1
    energy_to_be_spent = box
    energy_increase_factor = 1
    if turns % 3 == 0:
        toys_to_be_created_count = 2
        energy_to_be_spent *= 2
    if turns % 5 == 0:
        toys_to_be_created_count = 0
        energy_increase_factor = 0

    if energy_to_be_spent <= elf_energy:
        toys_made += toys_to_be_created_count
        total_energy += energy_to_be_spent
        elf_energies.append(elf_energy - energy_to_be_spent + energy_increase_factor)
    else:
        boxes.append(box)
        elf_energies.append(elf_energy * 2)

print(f"Toys: {toys_made}")
print(f"Energy: {total_energy}")
if boxes:
    print(f"Boxes left: {', '.join([str(x) for x in boxes])}")
if elf_energies:
    print(f"Elves left: {', '.join([str(x) for x in elf_energies])}")
