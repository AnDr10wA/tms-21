from exception import *



def summa(a,b):
    result = a+b
    return result

def division(a,b):
    result = " "
    try:
        result = a/b
    except ZeroDivisionError as err:
        print(f"Деление на 0 невозможно {err}")
    else:

        result = a/b
    return result

def mult(a,b):
    result = a*b
    return result

def sub(a,b):
    result = a-b
    return result



if __name__ == '__main__':
    a = 7
    b = 2
    print(summa(a,b))



