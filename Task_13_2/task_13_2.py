

import argparse
import csv
from time import sleep
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first-name', required=True)
parser.add_argument('-ln', '--last-name',   required=True)
parser.add_argument('-ti', '--time-focus', nargs='?', const = 25, type=int, required=True)
parser.add_argument('-tb', '--time-break',type=int, nargs='?', const = 5, required=True)
parser.add_argument('-nc', '--number-cycles', type=int, nargs='?', const = 4,  required=True)
parser.add_argument('-nt', '--name-task', required=True)
args = parser.parse_args()
date = datetime.now()
list_date = f"{date.day}.{date.month}.{date.year} {date.hour}:{date.minute}:{date.second}"
print(list_date)

with open("log_file.csv" , "a") as csvfile:
    csvwriter = csv.writer(csvfile)
    #csvwriter.writerow(["First name", "Last name", "Date", "Name Task"])
    csvwriter.writerow([args.first_name, args.last_name, list_date, args.name_task])

time_of_task = args.time_focus*60

def view_time(time):
    if time<0:
        return "00"
    elif time<10:
        return f"0{time}"
    else:
        return time

def timer_time(time):
    minutes = time//60
    seconds = time%60
    while True:
        if seconds>0:
            seconds -=1
            sleep(1)
            print(f"{view_time(minutes)}:{view_time(seconds)}")
        else:
            if minutes>0:
                minutes-=1
                seconds+=60
            else:
                break

for i in range(args.number_cycles):
    print("Start focus!")
    timer_time(time_of_task)
    print("Stop focus, BREAK!!!! ")
    timer_time(args.time_break*60)
    print("Stop break, FOCUS!!!")








