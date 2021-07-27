from datetime import *


train = [{"train_number": 902, "st_arrive": "Minsk", "time_arrive" : "10:40", "st_out": "Grodno", "time_out": "7:40"},
        {"train_number": 903, "st_arrive": "Minsk", "time_arrive" : "12:40", "st_out": "Moskow", "time_out": "2:40"},
        {"train_number": 904, "st_arrive": "Minsk", "time_arrive" : "16:40", "st_out": "Kiev", "time_out": "8:20"},
        {"train_number": 905, "st_arrive": "Minsk", "time_arrive" : "15:40", "st_out": "Vitebsk", "time_out": "3:00"},
        {"train_number": 906, "st_arrive": "Minsk", "time_arrive" : "18:40", "st_out": "Vilnus", "time_out": "16:10"}
        ]

time = "%H:%M"
del_time = datetime.strptime("10:20", "%H:%M")-datetime.strptime("3:00", "%H:%M")
delta = datetime.strptime(train[0]["time_arrive"], time) - datetime.strptime(train[0]["time_out"], time)
print(train[0]["time_arrive"])
print(del_time)
for i in range(len(train)):
    d_time = datetime.strptime(train[i]["time_arrive"], time) - datetime.strptime(train[i]["time_out"], time)
    print(d_time, del_time)
    if d_time > del_time:
        print(train[i])