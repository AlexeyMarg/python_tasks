"""
Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.
Каждое число записано в отдельной строке.
"""


def triangle_square():
    a = float(input('Введите длину первого катета\n'))
    b = float(input('Введите длину второго катета\n'))
    print('Площадь треугольника', a * b / 2)
    return a * b / 2


triangle_square()