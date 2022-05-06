


"""

"""





""" Все пан-цифровые числа делятся на 3 кроме n=7,4,1. Поэтому проверяем 7 циферные."""

# print(problem_41())


"""

"""





# print(problem_42())


"""

"""





# print(problem_43())


"""

"""





# print(problem_44())


"""

"""





# print(problem_45())


"""

"""





# print(problem_46())


"""

"""





# print(problem_47())


"""
Задача 48
Сумма 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
Найдите последние десять цифр суммы 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""





# print(problem_48())


"""

"""





# print(problem_49())


"""

"""





# print(problem_50())


"""

"""

""" 

"""





# print(problem_51())


"""

"""





# print(problem_52())


"""

"""





# print(problem_53())


"""

"""





# print(problem_54())


"""

"""




# print(problem_55())


"""

"""



# print(problem_56())


"""

"""



# print(problem_57())


"""

"""




# print(problem_58())


"""


"""




# print(problem_59())


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


def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

"""
1) Чистый брутфорс - приведенный решённый пример решается за 61485 мс
2) Добавлены такие условия    if 3 in i:
                                if sum(i) % 3 != 0:
                                    continue
                              else:
                                if sum(i) % 3 == 0:
                                    continue
   решается за 42907 мс

"""
@timer
def problem_60(n=5):
    prime_list = [i for i in range(2, 10000) if is_prime(i)]
    combinations_list = combinations(prime_list, r=n)
    for i in combinations_list:
        if 3 in i:
            if sum(i) % 3 == 0:
                continue
        perm = permutations(i, r=2)
        res = [is_prime(int("".join(map(str, k)))) for k in perm]
        if all(res):
            return i


print(problem_60())
