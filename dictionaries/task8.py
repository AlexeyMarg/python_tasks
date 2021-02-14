"""
Помогите Васе выполнить работу по созданию латинско-английского словаря из англо-латинского.
В первой строке содержится единственное целое число N — количество английских слов в словаре.
Далее следует N описаний. Каждое описание содержится в отдельной строке, в которой записано сначала
английское слово, затем отделённый пробелами дефис, затем разделённые запятыми с пробелами переводы
этого английского слова на латинский. Все слова состоят только из маленьких латинских букв.
Переводы отсортированы в лексикографическом порядке. Порядок следования английских слов в словаре
также лексикографический.

Выведите соответствующий данному латинско-английский словарь, в точности соблюдая формат входных данных.
В частности, первым должен идти перевод лексикографически минимального латинского слова, далее —
второго в этом порядке и т.д.
Внутри перевода английские слова должны быть также отсортированы лексикографически.
"""

n = int(input())
d0 = dict()
d1 = dict()
l = []
for i in range(n):
    s = input().replace('-', ',').replace(' ', '').split(',')
    d0[s[0]] = s[1:]
for i in d0.keys():
    for j in d0[i]:
        l.append(j)
l = sorted(l)
for i in l:
    for j in d0.keys():
        for k in d0[j]:
            if i == k:
                d1[i] = j
for i in d1.keys():
    print(i, d1[i])
