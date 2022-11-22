def store_results(func):
    def wrapper(*args):
        result = func(*args)
        with open('./results.txt', 'a') as file:
            return f"you called {func.__name__}{args}\nit returned {result}"
            file.write('\n')

        return result
    
    return wrapper


@store_results
def func(*args):
    return 3 + len(args)

@store_results
def sum_func(a, b):
    return a + b
