"""
Дано положительное действительное число X. Выведите его первую цифру после десятичной точки.
"""
x = 2.3452

print(int(x%1*10//1))