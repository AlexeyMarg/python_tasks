"""
Дан список стран и городов каждой страны.
Затем даны названия городов. Для каждого города укажите, в какой стране он находится.
"""

n = int(input())
d = dict()
for i in range(n):
    s = input().split()
    temp = []
    for j in range(1, len(s)):
        temp.append(s[j])
    d[s[0]] = temp

s = input()
for i in d.keys():
    if s in d[i]:
        print(i)
        break

