import random
import functools


# ЗАДАЧА-1
# Написать свой декоратор который будет проверять остаток от
# деления числа 100 на результат работы функции.
# Если остаток от деления = 0, вывести сообщение "We are OK!»,
# иначе «Bad news guys, we got {}» остаток от деления.


def verify_remainder(func):
    @functools.wraps(func)
    def wrapper():
        value = func()
        if value % 100 == 0:
            print("We are OK!")
        else:
            print("Bad news guys, we got {}".format(value))

    return wrapper


@verify_remainder
def get_random_value():
    return random.randint(0, 1000)


get_random_value()


# ЗАДАЧА-2
# Написать декоратор который будет выполнять предпроверку типа аргумента
# который передается в вашу функцию. Если это int, тогда выполнить функцию и
# вывести результат, если это str(), тогда зарейзить ошибку
# ValueError (raise ValueError(“string type is not supported”))

def verify_type(func):
    @functools.wraps(func)
    def wrapper(var):
        try:
            int_type = int(var)
            func(int_type)
        except ValueError:
            raise ValueError("String type is not supported")

    return wrapper


@verify_type
def is_even(var):
    if var % 2 == 0:
        return print("{} - number is even".format(var))
    else:
        return print("{} - Number is not even".format(var))


value = input("Enter integer value for verify(even/odd) - ")
is_even(value)

# *ЗАДАЧА-3
# Написать декоратор который будет кешировать значения аргументов и результаты
# работы вашей функции и записывать его в переменную cache. Если аргумента нет
# в переменной cache и функция выполняется, вывести сообщение
# «Function executed with counter = {}, function result = {}» и количество раз
# сколько эта функция выполнялась. Если значение берется из переменной cache,
# вывести сообщение «Used cache with counter = {}» и количество
# раз обращений в cache.

count = 0


def track_cache(func):
    cache = {}

    def wrapper(*args):
        global count
        if args in cache:
            count += 1
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            print(f"Run with args={args}, result={cache}")
            print(f"Used cache with counter = {count}")
            return result
    return wrapper


@track_cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(6)
