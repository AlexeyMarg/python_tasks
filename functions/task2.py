"""
Дано действительное положительное число a и целоe число n.
Вычислите an. Решение оформите в виде функции power(a, n).
Стандартной функцией возведения в степень пользоваться нельзя.
"""

def power(a, n):
    res = 1
    for i in range(1, n+1):
        res = res * a
    return res

a = int(input('a: '))
n = int(input('n: '))
print(power(a, n))