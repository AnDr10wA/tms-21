"""def my_func(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(kwargs)
        print(key, value)

my_func(a=5, b=7, c =20)

Создать функцию, которая принимает на вход
неопределенное количество именованных аргументов и
выводит на экран те из них, длина ключа которых четна.

"""
def func_dic(**kwargs):
    print(kwargs)
    for i in list(kwargs.keys()):
        if len(i) % 2 == 0:
            print(i, kwargs[i])
func_dic(hello = "world", pppp = "2222" )

