"""
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
"""

A = [1, 2, 3, 2, 3]
var = 0
i = 0

while i < len(A):
    temp = A[i]
    if A.count(temp) >= 2:
        var += 1
    A.remove(temp)
print(var)