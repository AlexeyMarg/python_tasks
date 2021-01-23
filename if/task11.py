"""
Яша плавал в бассейне размером N × M метров и устал.
В этот момент он обнаружил, что находится на расстоянии x метров от одного из длинных бортиков
(не обязательно от ближайшего) и y метров от одного из коротких бортиков.
Какое минимальное расстояние должен проплыть Яша, чтобы выбраться из бассейна на бортик?
Программа получает на вход числа N, M, x, y.
Программа должна вывести число метров, которое нужно проплыть Яше до бортика.
"""


def yasha(n, m, x, y):
    if x < abs(n - x) and x < y and x < abs(m - y):
        print(x)
    elif abs(n - x) < y and abs(n - x) < abs(m - y):
        print(abs(n - x))
    elif y < abs(m - y):
        print(y)
    else:
        print(abs(m - y))
    return 0


yasha(23, 52, 8, 43)
