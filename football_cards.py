info = input().split(' ')
team_a = 11
team_b = 11
players_loses = []
condition = True

for card in info:
    if card not in players_loses:
        players_loses.append(card)
        if 'A' in card:
            team_a -= 1
        elif 'B' in card:
            team_b -= 1

        if team_a < 7 or team_b < 7:
            condition = False
            break

print(f" Team A - {team_a}; Team B - {team_b}")

if condition == False:
    print("Game was terminated")