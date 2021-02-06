"""
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу.
На главной диагонали должны быть записаны числа 0. На двух диагоналях, прилегающих к главной, числа 1.
На следующих двух диагоналях числа 2, и т.д.
"""

n = int(input())
a = [[0]*n for i in range(n)]

for i in range(0, n):
    for j in range(1, i+1):
        a[i-j][i] = j
    for j in range(i+1, n):
        a[j][i] = j-i


for i in range(n):
    for j in range(n):
        print(a[i][j], ' ', end='')
    print('\n')