"""
Даны два списка чисел. Найдите все числа, которые входят как в первый,
так и во второй список и выведите их в порядке возрастания.
Примечание. И даже эту задачу на Питоне можно решить в одну строчку.
"""

a = set([int(i) for i in input().split()])
b = set([int(i) for i in input().split()])

print(sorted(list(a.intersection(b))))