"""
Дана последовательность натуральных чисел x1, x2, ..., xn.
Определите стандартное отклонение для данной последовательности натуральных чисел, завершающейся числом 0.
"""

from  math import sqrt

s = int(input())
summ = s
s = int(input())
sigma_sq = summ ** 2 + s ** 2 + 2 * (summ + s) + 2 * ((summ + s) / 2) ** 2
counter = 2
while s != 0:
    s = int(input())
    if s != 0:
        counter += 1
        summ = summ + s
        med = summ / counter
        sigma_sq = (sigma_sq * (counter - 2) + s**2 +2*s*med + counter * s**2) / (counter - 1)
print(sqrt(sigma_sq))
