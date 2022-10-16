n = int(input())
log = [input().split(', ') for _ in range(n)]
parking_lot = set()

for direction, car_number in log:
    if direction == "IN":
        parking_lot.add(car_number)
    else:
        parking_lot.remove(car_number)
if parking_lot:
    [print(car_number) for car_number in parking_lot]
else:
    print("Parking Lot is Empty")