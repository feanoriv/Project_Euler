from my_tools.tools import timer, is_prime
from itertools import combinations, permutations

"""
Задача 60
Простые числа 3, 7, 109 и 673 достаточно замечательны. Если взять любые 
два из них и объединить их в произвольном порядке, в результате всегда 
получится простое число. Например, взяв 7 и 109, получатся простые числа 
7109 и 1097. Сумма этих четырех простых чисел, 792, представляет собой 
наименьшую сумму элементов множества из четырех простых чисел, обладающих 
данным свойством.
Найдите наименьшую сумму элементов множества из 5 простых чисел, для которых 
объединение любых двух даст новое простое число.
"""


# В лоб решить нереально, т.е. перебирать ВСЕ варианты ВСЕХ перестановок для КАЖДОЙ пары.
# Можно создать словарь {n:{p1, p2, p3...}}, где n - простое число из списка простых чисел
# А p1, p2, p3... - простые числа с которыми оно образует пару простых чисел np1 и p1n.
# Словарь получается не длинный


@timer
def problem_60(n=4):
    prime_list = {i for i in range(3, 1000) if is_prime(i)}
    combinations_list = combinations(prime_list, r=2)
    graf_dict = {}
    for i in combinations_list:
        if is_prime(int(str(i[0]) + str(i[1]))) and is_prime(int(str(i[1]) + str(i[0]))):
            graf_dict.setdefault(i[0], set()).add(i[1])
            graf_dict.setdefault(i[1], set()).add(i[0])
    for key in graf_dict.keys():
        comb_lst = combinations(graf_dict[key], r=n)
        for comb in comb_lst:
            lst = list(comb[:])
            stack = 0
            for i in lst:
                lst.remove(i)  # TODO удаляет и от листа ничего не остаётся...
                lst.append(key)
                if len(graf_dict[i].intersection(lst)) == n-1:
                    stack += 1
                if stack == n - 1:
                    print(graf_dict[i].intersection(lst), i)

    import sys
    return sys.getsizeof(graf_dict), graf_dict


if __name__ == "__main__":
    print(problem_60())
