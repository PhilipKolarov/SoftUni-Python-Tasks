from collections import deque

pumps_count = int(input())
pumps = deque()
for _ in range(pumps_count):
    pumps.append([int(x) for x in input().split()])

for attempt in range(pumps_count):
    reservoir = 0
    fail = False
    for petrol, distance in pumps:
        reservoir = reservoir + petrol - distance
        if reservoir < 0:
            fail = True
            break

    if fail:
        pumps.append(pumps.popleft())
    else:
        print(attempt)
        break
