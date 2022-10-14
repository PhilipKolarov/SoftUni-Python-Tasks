def fill_the_box(height, length, width, *args):
    volume = height * length * width
    cubes_remaining = 0

    for x in args:
        if x == "Finish":
            break

        if volume >= x:
            volume -= x
        else:
            x -= volume
            cubes_remaining += x
            volume = 0

    if volume != 0:
        return f"There is free space in the box. You could put {volume} more cubes."
    else:
        return f"No more free space! You have {cubes_remaining} more cubes."


print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))