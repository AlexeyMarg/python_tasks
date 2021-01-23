"""
Дана строка. Найдите в этой строке второе вхождение буквы f, и выведите индекс этого вхождения.
Если буква f в данной строке встречается только один раз, выведите число -1,
а если не встречается ни разу, выведите число -2.
"""

s = input()


if s.count('f') == 0:
    print('Number of f: -2')
elif s.count('f') == 1:
    print('Number of f: -1')
else:
    number = s.find('f')
    temp = s[number :]
    number = number + temp.find('f') + 1
    print('Second f position:', number)