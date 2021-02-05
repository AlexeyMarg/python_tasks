"""
Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*"
в шахматном порядке.
В левом верхнем углу должна стоять точка.
"""

n = int(input())
m = int(input())

a = []

for i in range(n):
    row = []
    for j in range(m):
        if (i+j) % 2 == 0:
            row.append('.')
        else:
            row.append('*')
    a.append(row)

for i in range(n):
    for j in range(m):
        print(a[i][j], ' ', end='')
    print('\n')