"""
Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.
"""

A = [1, 2, 2, 3, 3, 3]
count = 1

for i in range(len(A)-1):
    if A[i+1] > A[i]:
        count += 1
print(count)