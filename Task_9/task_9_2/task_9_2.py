"""
Создать csv файл с данными о ежедневной погоде. Структура: Дата,
Место, Градусы, Скорость ветра. Найти среднюю погоду(скорость ветра и
градусы) для Минск за последние 7 дней.
"""

import csv
from datetime import *


fields = ["Date", "Place", "Temperature", "Spead_wind"]
rows = [
    ['27.07.2021', 'minsk', '27', '10'],
['28.07.2021', 'minsk', '29', '7'],
['29.07.2021', 'minsk', '25', '15'],
['30.07.2021', 'minsk', '26', '9'],
['31.07.2021', 'minsk', '28', '12'],
['01.08.2021', 'minsk', '26', '6'],
['02.08.2021', 'minsk', '27', '12'],
['03.08.2021', 'minsk', '27', '10'],
['01.08.2021', 'vitesk', '26', '6'],
['02.08.2021', 'grodno', '27', '12'],
['03.08.2021', 'lida', '27', '10']


]

filename = "task_9_2.csv"
with open(filename, 'w' ) as csvfile:
    writcsv = csv.writer(csvfile)
    writcsv.writerow(fields)
    writcsv.writerows(rows)

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvfile)
    print(fields)
    info = []
    for i in csvreader:
        info.append(i)
    info_sort = info[0:]
    list_temp = []
    list_wind = []
    datetime_now = datetime.now().date()
    delta_date = datetime_now - timedelta(days=7)
    for elem in info_sort:
        if elem[1] == "minsk":
            if delta_date < datetime.strptime(elem[0], '%d.%m.%Y').date():
                list_temp.append(elem[2])
                list_wind.append(elem[3])
    print(list_wind)
    print(list_temp)
    sum_temp = 0
    sum_wind = 0
    for i in list_temp:
        sum_temp += int(i)
    for i in list_wind:
        sum_wind += int(i)
    average_temp = sum_temp/len(list_temp)
    average_wind = sum_wind/len(list_wind)

    print(f"Средняя температура для Минска {average_temp}, средняя скорость ветра {average_wind}")








