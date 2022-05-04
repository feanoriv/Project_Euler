from functools import wraps
from time import time


# Таймер для определения времени выполнения функции
def timer(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000)) - start
            print(f"Функция {func.__name__} с аргументом(ами) {args}, - завершилась за: {end_ if end_ > 0 else 0} ms")

    return _time_it


# Является ли число простым
def is_prime(n: int) -> bool:
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    for k in range(3, int(n ** 0.5) + 1, 2):
        if n % k == 0:
            return False
    else:
        return True


# Является ли число палиндромом
def is_palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]


# Перемножение всех элементов списка
def multiply(lst: list) -> int:
    if not all(isinstance(elem, (int, float)) for elem in lst):
        raise ValueError("Список должен содержать только числа")
    res = 1
    for elem in lst:
        res *= elem
    return int(res)


# Решето Эратосфена возвращает список простых чисел до "n"
def sieve_of_eratosthenes(n: int) -> list:
    lst = list(range(2, n + 1))
    i, k = 0, 0
    sqrt_n = int(n ** 0.5) + 1
    while sqrt_n >= k:
        k = lst[i]
        lst = [x for x in lst if x % k != 0]
        lst.insert(i, k)
        i += 1
    return lst


# Факториал
def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res