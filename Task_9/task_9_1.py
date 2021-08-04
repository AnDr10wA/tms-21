"""Создать csv файл с данными следующей структуры: Имя, Фамилия,
Возраст. Создать отчетный файл с информацией по количеству людей
входящих в ту или иную возрастную группу. Возрастные группы: 1-12, 13-18,
19-25, 26-40, 40+."""


import csv


row_next = ["first_name", "last_name", "age"]
rows = [
        ["Alesya", "Ivanova", 25],
        ["Elena", "Petrova", 33],
        ["Vadim", "Smoler", 35],
        ["Andrei", "Antowin", 45],
        ["Kirill", "Sidorov", 22],
        ["Lera", "Semenova", 47],
        ["Anastasia", "Mixnat", 23],
        ["Vladimir", "Nekrasov", 55],
        ["Vitaliy", "Malofei", 58],
        ["Egor", "Byterin", 8],
        ["kostya", "Miligek", 15]
            ]
with open("task_9_1.csv", "w") as filecsv:
    csvwriter = csv.writer(filecsv)
    csvwriter.writerow(row_next)
    csvwriter.writerows(rows)
nrow = []
age1_12 = 0
age13_18 = 0
age19_25 = 0
age26_40 = 0
age40 = 0
with open("task_9_1.csv", "r") as filecsv:
    csvfile = csv.reader(filecsv)
    for i in csvfile:
        nrow.append(i)
    sort_row = nrow[1:]
    for j in sort_row:
        if 0<int(j[2])<=12:
            age1_12 +=1
        elif 13<=int(j[2])<=18:
            age13_18 += 1
        elif 19<=int(j[2])<=25:
            age19_25 += 1
        elif 26<=int(j[2])<=40:
            age26_40 += 1
        elif int(j[2]) > 40:
            age40 += 1
with open("task_9_1_report", "w") as reportfile:
    writerow = [f"{age1_12}", " - колличество 1- 12\n",
                f"{age13_18}", " - колличество 13 - 18\n",
                f"{age19_25}", " - колличество 19- 25\n",
                f"{age26_40}", " - колличество 26-40\n",
                f"{age40}", " - колличество больше 40\n",]
    reportfile.writelines(writerow)






