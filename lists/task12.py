"""
Дан список целых чисел, число k и значение C.
Необходимо вставить в список на позицию с индексом k элемент, равный C, сдвинув все элементы,
имевшие индекс не менее k, вправо.
Поскольку при этом количество элементов в списке увеличивается,
после считывания списка в его конец нужно будет добавить новый элемент, используя метод append.

Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе
и не создавая дополнительного списка.
"""

A = [int(s) for s in input().split()]
v = int(input())
k = int(input())

temp = A[k]
A[k] = v
for i in range(k+1, len(A)-1):
    A[i], temp = temp, A[i+1]
A.append(temp)
for i in A:
    print(i)