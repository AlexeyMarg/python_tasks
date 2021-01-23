"""
Дана строка. Удалите из этой строки все символы @.
"""

s = input()
res = ''
for i in s:
    if i != '@':
        res = res + i
print(res)