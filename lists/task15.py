"""
N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N.
Затем по этому ряду бросили K шаров, при этом i-й шар сбил все кегли с номерами от li до ri включительно.
Определите, какие кегли остались стоять на месте.
Программа получает на вход количество кеглей N и количество бросков K. Далее идет K пар чисел li, ri,
при этом 1≤ li≤ ri≤ N.

Программа должна вывести последовательность из N символов, где j-й символ есть “I”, если j-я кегля
осталась стоять, или “.”, если j-я кегля была сбита.
"""

N = int(input())
k = int(input())
A = ['I' for i in range(N)]

for i in range(k):
    li = int(input())
    ri = int(input())
    for j in range(li, ri+1):
        A[j-1] = '.'
print(A)