from my_tools.tools import timer, is_prime
"""
Задача 37
Число 3797 обладает интересным свойством. Будучи само по себе простым числом, 
из него можно последовательно выбрасывать цифры слева направо, число же при этом 
остается простым на каждом этапе: 3797, 797, 97, 7. Точно таким же способом можно 
выбрасывать цифры справа налево: 3797, 379, 37, 3.
Найдите сумму единственных одиннадцати простых чисел, из которых можно выбрасывать 
цифры как справа налево, так и слева направо, но числа при этом остаются простыми.
ПРИМЕЧАНИЕ: числа 2, 3, 5 и 7 таковыми не считаются.
"""


def check_variations_is_prime(n: str):
    if len(n) == 1:
        return False
    for i in range(len(n) - 1):
        n1 = n[i + 1:]
        n2 = n[:-i - 1]
        if not is_prime(int(n1)):
            return False
        if not is_prime(int(n2)):
            return False
    return True


@timer
def problem_37(n=1000000):  # До 1000_000 таких чисел 11 шт. => далее их нет исходя из условия.
    res = 0
    for i in range(11, n, 2):
        if any(n in ["0", "4", "6", "8"] for n in str(i)):
            continue
        if str(i).endswith("1") or str(i).startswith("1"):
            continue
        if is_prime(i):
            if check_variations_is_prime(str(i)):
                res += i
    return res


if __name__ == "__main__":
    print(problem_37())
