import re

n = int(input())
encrypted_messages = list()
for _ in range(n):
    encrypted_messages.append(input())

expression1 = r"([SsTtAaRr])"
matches = None
matches_dict = {}

for message in encrypted_messages:
    matches = re.findall(expression1, message)
    matches_dict[message] = matches

decrypted_messages = list()
for key in matches_dict:
    decrypted_message = ''
    for ch in key:
        new_ascii_value = ord(ch) - len(matches_dict[key])
        new_ch = chr(new_ascii_value)
        decrypted_message += new_ch
    decrypted_messages.append(decrypted_message)

expression2 = r"(?<=@)([^A-Za-z@!:>-]*)(?P<planet>[A-Za-z]+)([^A-Za-z@!:>-]*):([^0-9@!:>-]*)(?P<population>\d+)([^0-9@!:>-]*)!([^AD@!:>-]*)(?P<action>[A|D])([^AD@!:>-]*)!->([^0-9@!:>-]*)(?P<soldiers>\d+)([^0-9@!:>-]*)"
attack_list = list()
defeat_list = list()

for message in decrypted_messages:
    matches = re.finditer(expression2, message)
    for match in matches:
        planet = match.group('planet')
        population = int(match.group('population'))
        action = match.group('action')
        soldiers = int(match.group('soldiers'))
        if action == 'A':
            attack_list.append(planet)
        if action == 'D':
            defeat_list.append(planet)

attack_list = sorted(attack_list)
defeat_list = sorted(defeat_list)

print(f"Attacked planets: {len(attack_list)}")
for planet in attack_list:
    print(f"-> {planet}")
print(f"Destroyed planets: {len(defeat_list)}")
for planet in defeat_list:
    print(f"-> {planet}")
