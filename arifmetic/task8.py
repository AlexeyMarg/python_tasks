"""
Пирожок в столовой стоит a рублей и b копеек.
Определите, сколько рублей и копеек нужно заплатить за n пирожков.
Программа получает на вход три числа: a, b, n, и должна вывести два числа:
стоимость покупки в рублях и копейках.
"""

a = 10
b = 15
n = 2

r = a * n + b * n // 100
k = b * n % 100
print(r, ',', k)