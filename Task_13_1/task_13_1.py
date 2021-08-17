
import sys
import argparse
import csv
from time import sleep
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first-name',
required=True)
parser.add_argument('-ln', '--last-name',
required=True)
parser.add_argument('-ho', '--hours',
required=True)
parser.add_argument('-mi', '--minutes',
required=True)
parser.add_argument('-se', '--seconds',
required=True)
args = parser.parse_args()
date = datetime.now()
list_date = f"{date.day}.{date.month}.{date.year} {date.hour}:{date.minute}:{date.second}"
print(list_date)

with open("log_file.csv" , "a") as csvfile:
    csvwriter = csv.writer(csvfile)
    #csvwriter.writerow(["First name", "Last name", "Date"])
    csvwriter.writerow([args.first_name, args.last_name, list_date])



try:
    hours = int(args.hours)
    minutes = int(args.minutes)
    seconds = int(args.seconds)
except ValueError as err:
    print("Ведите корректные данные: ")
else:
    hours = int(args.hours)
    minutes = int(args.minutes)
    seconds = int(args.seconds)

def view_time(time):
    if time<0:
        return "00"
    elif time<10:
        return f"0{time}"
    else:
        return time

while True:

    if seconds > 0:
        seconds -= 1
        sleep(1)
        print(f"{view_time(hours)}:{view_time(minutes)}:{view_time(seconds)})")
    else:
        if minutes > 0:
            minutes -= 1
            seconds += 60
        else:
            if hours > 0:
                hours -= 1
                minutes += 60
            else:
                print("ALARM")
                break









