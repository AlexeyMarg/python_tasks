"""
Напишите программу, которая приветствует пользователя, выводя слово Hello,
введенное имя и знаки препинания
"""

def hello_func():
    name = input('Enter your name, please\n')
    print('Hello,' + name + '!')
    return 'Hello,' + name

hello_func()