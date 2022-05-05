from my_tools.tools import timer
"""
Задача 31
В Англии валютой являются фунты стерлингов £ и пенсы p, и в обращении есть восемь монет:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) и £2 (200p).
£2 возможно составить следующим образом:
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
Сколькими разными способами можно составить £2, используя любое количество монет?
"""


@timer
def problem_31_old(n=16):
    coins = [2, 5, 10, 20, 50, 100, 200]
    indexes = [-2, -3, -4, -5, -7, -8, -9]
    res = [[]]
    while sum(res[0]) < n:
        print(sum(res[0]))
        for lst in res:
            lst.append(1)
        new_lists = []
        for lst in res:
            for ind in indexes:
                if sum(lst[ind:]) == coins[indexes.index(ind)]:
                    new_lst = lst[:]
                    del new_lst[ind:]
                    new_lst.insert(ind, coins[indexes.index(ind)])
                    new_lists.append(sorted(new_lst, reverse=True))

        if new_lists:
            for lst in new_lists:
                if lst not in res:
                    res.append(lst)
    import sys
    return len(res), sys.getsizeof(res)

#
# @timer
# def problem_31(n=7):
#     coins = [2, 5, 10, 20, 50, 100, 200]
#     ways = 1
#     return ways


if __name__ == "__main__":
    print(problem_31_old())
