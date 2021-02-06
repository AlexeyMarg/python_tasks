"""
Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.
Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.
Решение оформите в виде функции swap_columns(a, i, j).
"""


def swap_columns(a, i, j):
    for k in range(n):
        a[k][i], a[k][j] = a[k][j], a[k][i]
    return 0


n = int(input('Rows: '))
m = int(input('Columns: '))
a = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        a[i][j] = int(input())
print('List created')
i = int(input())
j = int(input())
swap_columns(a, i, j)

for i in range(n):
    for j in range(m):
        print(a[i][j], ' ', end='')
    print('\n')
