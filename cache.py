def cache(func):
    memo = {}
    def wrapper(n):
        if n in memo:
            return memo[n]
        result = func(n)
        memo[n] = result
        return result

    wrapper.log = memo
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(8))