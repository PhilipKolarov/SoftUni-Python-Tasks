from collections import deque

green_light_time = int(input())
free_window = int(input())
cars = deque()
total_deque_len = 0
crash = False
crash_car = None
crash_letter = None
number_of_cars = 0
okay = True

while okay:
    input_string = input()
    if input_string == "END":
        break
    if input_string == "green":
        total_deque_len = 0
        for car in cars:
            total_deque_len += len(car)
            number_of_cars += 1
            if total_deque_len < green_light_time:
                continue
            elif total_deque_len < (green_light_time + free_window):
                break
            elif total_deque_len > (green_light_time + free_window):
                crash = True
                crash_car = car
                index = total_deque_len - (green_light_time + free_window) + 2
                crash_letter = car[index]
                okay = False
        cars.clear()
    else:
        cars.append(input_string)

if crash == False:
    print("Everyone is safe.")
    print(f"{number_of_cars} total cars passed the crossroads.")

else:
    print("A crash happened!")
    print(f"{crash_car} was hit at {crash_letter}.")
