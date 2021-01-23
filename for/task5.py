"""
Дано несколько чисел. Вычислите их сумму. Сначала вводите количество чисел N,
затем вводится ровно N целых чисел.
"""

N = int(input('Enter number of values\n'))
s = 0
for i in range(0, N):
    s = s + int(input())
print(s)
