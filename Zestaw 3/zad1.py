import functools


def pamiec(func):
    slownik = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if(args in slownik):
            return slownik[args]
        else:
            fib = func(*args, **kwargs)
            slownik[args] = fib
            return fib
    
    return wrapper


@pamiec
def fibonacci(n):
    return n if 0 <= n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


for i in range(100):
    print(fibonacci(i))
