"""
Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи.
В этой задаче нельзя использовать циклы — используйте рекурсию.
"""

def fibbonachi(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibbonachi(n-1) + fibbonachi(n-2)

n = int(input())
print(fibbonachi(n))