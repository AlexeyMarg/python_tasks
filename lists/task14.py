"""
Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""

A = [1, 2, 3, 2, 3, 4]
x = 0

i = 0
while i < len(A):
    temp = A[i]
    if A.count(temp) == 1:
        x += 1
    A.remove(temp)
    i += 1
print(x)
