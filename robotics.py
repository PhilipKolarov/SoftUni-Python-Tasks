from collections import deque

def read_robots():
    result = {}
    input_robots = input().split(';')
    for robot in input_robots:
        robot_details = robot.split('-')
        name = robot_details[0]
        processing_time = robot_details[1]
        result[name] = processing_time
    return result


def in_seconds(hours, minutes, seconds):
    return hours * 60 * 60 + minutes * 60 + seconds

def to_str_time():
    a = time_in_seconds // 3600
    b = (time_in_seconds % 3600) // 60
    c = (time_in_seconds % 3600) % 60
    return f"{a:02d}:{b:02d}:{c:02d}"

def read_products():
    result = deque()
    while True:
        line = input()
        if line == 'End':
            break
        result.append(line)
    return result


robots = read_robots()
available_robots = [r for r in robots.keys()]
processing_robots = {}

starting_time_parts = [int(x) for x in input().split(':')]
time_in_seconds = in_seconds(starting_time_parts[0], starting_time_parts[1], starting_time_parts[2])

products = read_products()

while products:
    time_in_seconds = (time_in_seconds + 1) % (24 * 60 * 60)

    for robot_name in [k for k in processing_robots.keys()]:
        processing_robots[robot_name] -= 1
        if processing_robots[robot_name] <= 0:
            processing_robots.pop(robot_name)

    current_product = products.popleft()
    for robot_name in available_robots:
        if robot_name not in processing_robots:
            print(f"{robot_name} - {current_product} [{to_str_time()}]")
            processing_robots[robot_name] = int(robots[robot_name])
            break
    else:
        products.append(current_product)

#https://pastebin.com/2iS5hQyq