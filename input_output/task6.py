"""
Напишите программу, которая считывает целое число и выводит текст,
аналогичный приведенному в примере (пробелы важны!).
The next number for the number 1534 is 1535.
The previous number for the number 1534 is 1533.
"""

def prev_and_next():
    i = int(input('Enter number\n'))
    print('The next number for the number ', i, ' is ', i+1, '\n')
    print('The previous number for the number ', i, ' is ', i - 1)

prev_and_next()
