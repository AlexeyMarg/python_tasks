"""
Дана строка.
Сначала выведите третий символ этой строки.
Во второй строке выведите предпоследний символ этой строки.
В третьей строке выведите первые пять символов этой строки.
В четвертой строке выведите всю строку, кроме последних двух символов.
В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого).
В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
В седьмой строке выведите все символы в обратном порядке.
В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
В девятой строке выведите длину данной строки.
"""

s = input()
print(s[2])
print(s[-2])
print(s[0:4])
print(s[0:-2])
temp=''
for i in range(1, len(s)+1):
    if i % 2 == 0:
        temp = temp + s[i-1]
print(temp)
temp = ''
for i in range(1, len(s)+1):
    if i % 2 == 1:
        temp = temp + s[i-1]
print(temp)
temp = s[-1]
for i in range(2, len(s)+1):
    temp = temp + s[-i]
print(temp)
temp = ''
for i in range(1, len(s)+1):
    if i % 2 == 1:
        temp = temp + s[-i]
print(temp)
print(len(s))
