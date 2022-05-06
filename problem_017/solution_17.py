from my_tools.tools import timer

"""
Задача 17
Если записать числа от 1 до 5 английскими словами (one, two, three, four, five), 
то используется всего 3 + 3 + 5 + 4 + 4 = 19 букв.
Сколько букв понадобится для записи всех чисел от 1 до 1000 (one thousand) включительно?
Примечание: Не считайте пробелы и дефисы. Например, число 342 (three hundred and forty-two) 
состоит из 23 букв, число 115 (one hundred and fifteen) - из 20 букв. 
Использование "and" при записи чисел соответствует правилам британского английского.
"""
# dict из просторов
ones = {
    0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {
    2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
    7: 'seventy', 8: 'eighty', 9: 'ninety'}
illions = {
    1: 'thousand', 2: 'million', 3: 'billion', 4: 'trillion', 5: 'quadrillion',
    6: 'quintillion', 7: 'sextillion', 8: 'septillion', 9: 'octillion',
    10: 'nonillion', 11: 'decillion'}


@timer
def problem_17(n=1000):
    res = 0
    for i in range(1, n + 1):
        if i // 10 <= 1:
            res += len(ones[i])
        elif 2 <= i // 10 <= 9:
            res += len(tens[i // 10]) + len(ones[i % 10])
        elif 9 < i // 10 < 100:
            if i % 100 == 0:
                res += len(ones[i / 100]) + len("hundred")
            elif i % 100 <= 19:
                res += len(ones[i // 100]) + len("hundred") + len("and") + len(ones[i % 100])
            elif i % 100 >= 19:
                res += len(ones[i // 100]) + len("hundred") + len("and") + len(tens[(i % 100) // 10]) + len(
                    ones[(i % 100) % 10])
        elif i // 1000 >= 1:
            res += len("onethousand")
    return res


if __name__ == "__main__":
    print(problem_17())
