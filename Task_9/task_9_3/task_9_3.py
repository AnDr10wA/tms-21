"""
Дан файл, содержащий различные даты. Каждая дата - это число, месяц и
год. Найти самую раннюю дату. [02-8.1-ML-29]
"""
from datetime import *
import csv

filename = "task_9_3.csv"
top = ["Something", "date"]
down = [
    ["Apple", "18/03/2021"],
    ["Crocodile", "25/03/2021"],
    ["Number", "18/04/2021"],
    ["Fruits", "22/03/2020"],
    ["Water", "18/03/2021"]

]

with open(filename, "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(top)
    csvwriter.writerows(down)
rows = []
with open(filename, "r") as file:

    readfile = csv.reader(file)
    rfile = []
    for i in readfile:
        rfile.append(i)
    print(readfile)
    read_for_sort =  rfile[1:]
    for row in read_for_sort:

        rows.append(row[1])
print(rows)
sortrow = sorted(rows, key = lambda x: datetime.strptime(x , '%d/%m/%Y'))
print(sortrow)
print(f"Самая ранняя дата в файле {sortrow[0]}")



