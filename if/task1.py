"""
Даны два целых числа. Выведите значение наименьшего из них.
"""
def min_func():
    a = float(input('Enter first number\n'))
    b = float(input('Enter second number\n'))
    if a<b:
        print('Minimum is ', a)
    else:
        print('Minimum is ', b)

min_func()