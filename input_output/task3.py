"""
n школьников делят k яблок поровну, неделящийся остаток остается в корзинке.
Сколько яблок достанется каждому школьнику? Сколько яблок останется в корзинке?
Программа получает на вход числа n и k и должна вывести искомое количество яблок (два числа).
"""


def apples_separation():
    n = int(input('Введите количество яблок\n'))
    k = int(input('Введите количество школьнико\n'))
    print('Каждый получит', n // k, 'яблок')
    print('Остаток: ', n % k)
    return n // k, n % k

apples_separation()
