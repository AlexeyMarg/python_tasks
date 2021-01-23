"""
Заданы две клетки шахматной доски. Если они покрашены в один цвет, то выведите слово YES,
а если в разные цвета — то NO. Программа получает на вход четыре числа от 1 до 8 каждое,
задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
"""

def chess_fun(a, b, c, d):
    if (a % 2 == 1 and b % 2 == 1) or (a % 2 == 0 and b % 2 == 0):
        first = True
    else:
        first = False
    if (c % 2 == 1 and d % 2 == 1) or (c % 2 == 0 and d % 2 == 0):
        second = True
    else:
        second = False
    if first == second:
        print('yes')
        return  True
    else:
        print('no')
        return False

chess_fun(1,1,2,6)


