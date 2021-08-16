from func import *
from exception import ValueException


def input_func(operation):


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
        result = Math(a,b)
        operations = {"1":result.division(), "2": result.mult(), "3": result.summa(), "4":result.sub()}
        print(operations[operation])





def vie_func(operation):


    if operation in ["1", "2", "3", "4"]:
        input_func(operation)

    else:
        try:
            raise ValueException
        except ValueException as err:
            print(err)


