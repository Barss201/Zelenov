'''Написати декоратор для будь якої функції, що буде зберігати історію викликів функцій у файлі.'''

import datetime

def some_de(some_func):
    def wrapper(*args, **kwargs):
        time = datetime.datetime.now()
        result = some_func(*args, **kwargs)
        file = open("result.txt", "a")
        file.write(str(f"{some_func.__name__} was called with args {args} {kwargs} at {time} and return result {result}\n"))
        file.close()
        return result
    return wrapper
@some_de
def apper(n, k):
    return n + k

apper(10, 5)
@some_de
def test(a, b):
    return a * b

test(3, 5)