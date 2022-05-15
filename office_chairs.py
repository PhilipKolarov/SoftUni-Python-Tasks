def operation(quantity):
    enough_chairs = True
    available_chairs = 0
    for i in range(1, quantity + 1):
        current_row = input().split(" ")
        chairs = current_row[0]
        visitors = int(current_row[1])
        if len(chairs) >= visitors:
            available_chairs += len(chairs) - visitors
        else:
            diff = visitors - len(chairs)
            print(f"{diff} more chairs needed in room {i}")
            enough_chairs = False

    if enough_chairs == True:
        print(f"Game On, {available_chairs} free chairs left")

rooms = int(input())
operation(rooms)