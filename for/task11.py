"""
Для настольной игры используются карточки с номерами от 1 до N.
Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек.
Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N).
Программа должна вывести номер потерянной карточки.
"""

N = int(input())
s = 0
for i in range(1, N+1):
    s += i
for i in range(1, N):
    s = s - int(input())

print(s)
