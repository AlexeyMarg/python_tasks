"""
В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
"""

A = [3, 4, 5, 2, 1]

m = A[0]
n = A[0]
index_m = 0
index_n = 0
for i in range(1, len(A)):
    if A[i] > m:
        m = A[i]
        index_m = i
    if A[i] < n:
        n = A[i]
        index_n = i
A[index_n], A[index_m] = A[index_m], A[index_n]
for i in A:
    print(i)