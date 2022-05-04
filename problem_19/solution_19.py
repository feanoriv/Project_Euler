from my_tools.tools import timer

"""
Задача 19
Дана следующая информация (однако, вы можете проверить ее самостоятельно):
1 января 1900 года - понедельник.
В апреле, июне, сентябре и ноябре 30 дней.
В феврале 28 дней, в високосный год - 29.
В остальных месяцах по 31 дню.
Високосный год - любой год, делящийся нацело на 4, однако последний год века (ХХ00) 
является високосным в том и только том случае, если делится на 400.
Сколько воскресений выпадает на первое число месяца в двадцатом веке 
(с 1 января 1901 года до 31 декабря 2000 года)?
"""


mounts_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


@timer
def problem_19():
    year = 1900
    mount = 1
    day = 1
    weekday = 1
    year_mount_day_weekday = []
    while True:
        if (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0):
            mounts_days[2] = 29
        else:
            mounts_days[2] = 28
        year_mount_day_weekday.append([year, mount, day, weekday])

        if day < mounts_days[mount]:
            day += 1
        else:
            day = 1
            if mount < 12:
                mount += 1
            else:
                mount = 1
                year += 1
        if weekday < 7:
            weekday += 1
        else:
            weekday = 1

        if year == 2001:
            counter = 0
            for elem in year_mount_day_weekday:
                if elem[2] == 1 and elem[3] == 7 and elem[0] != 1900:
                    counter += 1
            return counter


if __name__ == "__main__":
    print(problem_19())
