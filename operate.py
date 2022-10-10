def operate(operation, *args):
    def add(*args):
        return sum(args)

    def subtract(x, *args):
        return x + sum(-y for y in args)

    def multiply(*args):
        result = 1
        for value in args:
            result *= value

        return result

    def divide(x, *args):
        result = x
        for value in args:
            result /= value

        return result

    if operation == '+':
        return add(*args)
    elif operation == '-':
        return subtract(*args)
    elif operation == '*':
        return multiply(*args)
    elif operation == '/':
        return divide(*args)
    else:
        None


print(operate('+', 1, 2, 3))
print(operate('-', 1, 2, 3))
print(operate('*', 1, 2, 6))
print(operate('/', 4, 2, 2))
