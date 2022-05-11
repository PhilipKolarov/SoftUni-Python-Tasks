city_input = input()
city_data_dict = {}

while city_input != "Sail":
    city_data = city_input.split('||')
    name = city_data[0]
    population = int(city_data[1])
    gold = int(city_data[2])
    if name in city_data_dict.keys():
        (city_data_dict[name])[0] += population
        (city_data_dict[name])[1] += gold
    else:
        city_data_dict[name] = [population, gold]
    city_input = input()

command = input()
while command != "End":
    command = command.split("=>")

    if command[0] == "Prosper":
        current_town = command[1]
        gold_increase = command[2]
        if int(gold_increase) >= 0:
            (city_data_dict[current_town])[1] += int(gold_increase)
            gold_total = (city_data_dict[current_town])[1]
            print(f"{gold_increase} gold added to the city treasury. {current_town} now has {gold_total} gold.")
        else:
            print('Gold added cannot be a negative number!')

    elif command[0] == "Plunder":
        current_town = command[1]
        people_killed = command[2]
        gold_taken = command[3]
        (city_data_dict[current_town])[0] -= int(people_killed)
        (city_data_dict[current_town])[1] -= int(gold_taken)
        print(f"{current_town} plundered! {gold_taken} gold stolen, {people_killed} citizens killed.")
        if (city_data_dict[current_town])[0] == 0 or (city_data_dict[current_town])[1] == 0:
            del city_data_dict[current_town]
            print(f"{current_town} has been wiped off the map!")
        else:
            pass
    command = input()

if city_data_dict != {}:
    print(f"Ahoy, Captain! There are {len(city_data_dict)} wealthy settlements to go to:")
    for key, value in city_data_dict.items():
        print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")
else:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')
