"""
Шахматный слон ходит по диагонали. Даны две различные клетки шахматной доски,
определите, может ли слон попасть с первой клетки на вторую одним ходом.
"""


def check_chess(a, b, c, d):
    if abs(a - c) == abs(b - d):
        print('Yes')
    else:
        print('No')
    return 0


check_chess(4, 4, 5, 5)
