list_of_auto = [
        {"serial_number": "1234", "year": 1997 },
        {"serial_number": "1334", "year": 1999 },
        {"serial_number": "4234", "year": 2010 },
        {"serial_number": "1786", "year": 2020 }
    ]
n = 2000
new_list_auto = [i for i in list_of_auto if i["year"]>n]
print(new_list_auto)