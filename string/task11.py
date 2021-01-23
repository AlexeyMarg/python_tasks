"""
Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.
"""

s = input()
start, end = s.find('h'), s.rfind('h')
res = s[:start]
for i in s[start:end+1]:
    if i == 'h':
        res += 'H'
    else:
        res += i
res += s[end+1:]
print(res)