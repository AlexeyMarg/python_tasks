"""
По данному натуральном n вычислите сумму 1!+2!+3!+...+n!.
В решении этой задачи можно использовать только один цикл.
Пользоваться математической библиотекой math в этой задаче запрещено.
"""


n = int(input())

sum = 0
prev = 1
for i in range(1, n + 1):
    curr = prev * i
    sum += curr
    prev = curr
print(sum)