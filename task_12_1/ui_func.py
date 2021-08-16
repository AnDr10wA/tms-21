from func import *
from exception import ValueException
def input_func(func):

    a = input("Ведите а  ")
    b = input("Ведите b  ")
    try:
        a = int(a)
        b = int(b)
    except ValueError as err:
        print("а и b доджны быть целыми числами")
    else:
        a = int(a)
        b = int(b)
        print(func(a,b))

def vie_func(operation):


    if operation ==  "1":
        input_func(division)
    elif operation == "2":
        input_func(mult)
    elif operation == "3":
        input_func(summa)
    elif operation == "4":
        input_func(sub)
    else:
        try:
            raise ValueException
        except ValueException as err:
            print(err)

