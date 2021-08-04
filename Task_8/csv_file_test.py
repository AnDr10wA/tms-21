
"""Написать функции по работе с csv файлами в файле csv_utils.py. Чтение.
Запись. Добавление записи(по позиции, по-умолчанию в конец)."""
import csv


def read_csv(filename):
    rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
#    fields = next(csvreader)
        for row in csvreader:
            rows.append(row)

 #   print("Total no. of rows: %d" %
 #         (csvreader.line_num))

    return rows
read_csv("username.csv")

def add_row(filename, row, position = None):
    rows = read_csv(filename)
    if position == None:
        rows.append(row)
    else:
        new_rows = []
        new_rows.append(rows[:position])
        new_rows.append(row)
        new_rows.append(rows[position:])
    print(new_rows)
    return new_rows

add_row("username.csv", ["add", ])




