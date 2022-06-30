from collections import deque

flowers = {'rose': 'rose', 'daffodil': 'daffodil', 'tulip': 'tulip', 'lotus': 'lotus'}

input_vowels = deque([x for x in input().split()])
input_consonants = [x for x in input().split()]

flower_found_condition = False
flower_found = None
min_range = min(len(input_consonants), len(input_vowels))

for _ in range(min_range):
    current_vowel = input_vowels.popleft()
    current_consonant = input_consonants.pop()
    for flower in flowers.keys():
        if current_vowel in flower and current_vowel in flowers[flower]:
            flowers[flower] = flowers[flower].replace(current_vowel, '')
        if current_consonant in flower and current_consonant in flowers[flower]:
            flowers[flower] = flowers[flower].replace(current_consonant, '')
        if flowers[flower] == '':
            flower_found = flower
            flower_found_condition = True
    if flower_found_condition == True:
        break

if flower_found_condition == True:
    print(f"Word found: {flower_found}")
else:
    print('Cannot find any word!')

if input_vowels:
    print(f"Vowels left: {' '.join(input_vowels)}")
if input_consonants:
    print(f"Consonants left: {' '.join(input_consonants)}")
