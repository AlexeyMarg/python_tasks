"""
Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания,
если A < B, или в порядке убывания в противном случае.
"""

a = 10
b = 5

temp = []
if a < b:
    for i in range(a, b + 1):
        temp.append(i)
else:
    for i in range(b, a + 1):
        temp.insert(0, i)

for i in temp:
    print(i)
