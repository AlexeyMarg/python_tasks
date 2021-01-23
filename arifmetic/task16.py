"""
С начала суток часовая стрелка повернулась на угол в α градусов.
Определите сколько полных часов, минут и секунд прошло с начала суток,
то есть решите задачу, обратную задаче «Часы - 1».
Запишите ответ в три переменные и выведите их на экран.
"""

alpha = 31.05

total_seconds = alpha/360*12*3600
hours = int(total_seconds // 3600)
total_seconds = total_seconds - hours*3600
minutes = int(total_seconds // 60)
seconds = int(total_seconds - minutes*60)

print(hours,':', minutes, ':', seconds)
