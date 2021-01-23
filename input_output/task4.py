"""
Дано число n. С начала суток прошло n минут.
Определите, сколько часов и минут будут показывать электронные часы в этот момент.
Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59).
Учтите, что число n может быть больше, чем количество минут в сутках.
"""

def clock(n):
    minutes = n % 60
    hours = n // 60 % 24
    print(str(hours) + ':' + str(minutes))
    return str(hours) + ':' + str(minutes)

test_input_data = [150, 1441, 444, 180, 1439, 1440, 2000, 3456, 5678, 9876]
test_output_data=['2:30', '0:1', '7:24', '3:0', '23:59', '0:0', '9:20', '9:36', '22:38', '20:36']

j = 0
for i in range(len(test_input_data)):
    if test_output_data[i] != clock(test_input_data[i]):
        j += 1
        print('Test ', i+1, ' failed')
if j == 0:
    print('All tests passed')
