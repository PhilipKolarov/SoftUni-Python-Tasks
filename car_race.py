input_list = list(map(int, input().split(" ")))
list_middle_index = int((len(input_list) + 1) / 2)
left_list = list(input_list[0:list_middle_index - 1])
right_list = list(input_list[(list_middle_index)::])

left_total_time = 0
right_total_time = 0

right_list.reverse()

for left_time in left_list:
    time_index = int(left_list.index(left_time))
    left_time = int(left_time)
    if left_time != 0:
        left_total_time += left_time
    elif left_time == 0:
        left_total_time *= 0.8

for time in right_list:
    time_index = int(right_list.index(time))
    time = int(time)
    if time != 0:
        right_total_time += time
    elif time == 0:
        right_total_time *= 0.8

if left_total_time > right_total_time:
    print(f"The winner is right with total time: {right_total_time:.1f}")
if left_total_time < right_total_time:
    print(f"The winner is left with total time: {left_total_time:.1f}")