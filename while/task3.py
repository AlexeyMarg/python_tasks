"""
По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N.
Выведите показатель степени и саму степень.
Операцией возведения в степень пользоваться нельзя!
"""

def stepen2(n):
    res = 1
    i = 1
    while i <= n:
        res = res * 2
        i += 1
    return res

N = int(input())
x = 1
while stepen2(x) <= N:
    x += 1
print(x-1, ' ', stepen2(x-1))


