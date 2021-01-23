"""
Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.
"""

s = input()

res = ''
for i in range(len(s)):
    if i % 3 != 0:
        res += s[i]
print(res)