from my_tools.tools import timer, is_prime
from itertools import combinations

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
# Можно создать словарь {key:{p1, p2, p3...}}, где key - простое число из списка простых чисел
# А p1, p2, p3... - простые числа с которыми оно образует пару простых чисел key_p1 и p1_key.
# Затем идёт перебор комбинаций (p1, p2, p3 ... pn) группами по n-1 элементов.
# И для каждого элемента применяется метод множества intersection, если для каждого элемента
# длина последовательности == n-1, то сумма полученного подмножества + key возвращается как результат
# Время исполнения ~ 90c. Явно есть способ лучше, но не дался.


@timer
def problem_60(n=5):
    prime_list = [i for i in range(3, 8400) if is_prime(i)]
    combinations_list = combinations(prime_list, r=2)
    graf_dict = {}
    for i in combinations_list:
        if is_prime(int(str(i[0]) + str(i[1]))) and is_prime(int(str(i[1]) + str(i[0]))):
            graf_dict.setdefault(i[0], set()).add(i[1])
            graf_dict.setdefault(i[1], set()).add(i[0])
    # print(graf_dict)
    unfit_nums = set()
    for key in graf_dict.keys():
        comb_lst = combinations(graf_dict[key], r=n-1)
        for comb in comb_lst:
            if unfit_nums.intersection(set(comb)) == set(()):
                stack = 0
                in_lst = list(comb)
                in_lst.append(key)
                for i in comb:
                    if len(graf_dict[i].intersection(in_lst)) == n-1:
                        stack += 1
                    if stack == n-1:
                        return sum(graf_dict[i].intersection(in_lst)) + i
        unfit_nums.add(key)

    import sys
    return sys.getsizeof(graf_dict), graf_dict


if __name__ == "__main__":
    print(problem_60())
