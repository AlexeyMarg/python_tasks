"""
В математике функция sign(x) (знак числа) определена так:
sign(x) = 1, если x > 0,
sign(x) = -1, если x < 0,
sign(x) = 0, если x = 0.
Для данного числа x выведите значение sign(x).
Эту задачу желательно решить с использованием каскадных инструкций if... elif... else.
"""


def sign(a):
    if a > 0:
        res = 1
    elif a == 0:
        res = 0
    else:
        res = -1
    return res


a = float(input('Enter the number\n'))
print(sign(a))
