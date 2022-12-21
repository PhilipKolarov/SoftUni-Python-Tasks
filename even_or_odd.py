def even_odd(*args):
    nums = []
    if args[-1] == 'even':
        for n in args[0:-1]:
            if n % 2 == 0:
                nums.append(n)
    elif args[-1] == 'odd':
        for n in args[0:-1]:
            if n % 2 != 0:
                nums.append(n)

    return nums


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))