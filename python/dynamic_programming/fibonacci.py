import timeit

def fibonacci(n, cache=None):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    result = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    cache[n] = result
    return result


def fib(n):
    a = 1
    b = 1
    for i in range(2, n + 1):
        a, b = b, a+b
    return b

print(fib(5))
