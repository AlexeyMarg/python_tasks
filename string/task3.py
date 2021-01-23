"""
Дана строка. Разрежьте ее на две равные части (если длина строки — четная,
а если длина строки нечетная, то длина первой части должна быть на один символ больше).
Переставьте эти две части местами, результат запишите в новую строку и выведите на экран.
При решении этой задачи не стоит пользоваться инструкцией if.
"""

s = input()
second_half_length = len(s) // 2
result = s[-second_half_length:] + s[0: len(s)-second_half_length]
print(result)