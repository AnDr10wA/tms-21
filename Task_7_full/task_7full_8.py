"""
Написать функцию принимающая на вход неопределенным количеством
аргументов и именованный аргумент mean_type. В зависимости от mean_type
вернуть среднеарифметическое либо среднегеометрическое. Написать
программу в виде трех функций.

"""
from math import sqrt
def result_func(*args, **kwargs):
    print(args)
    print(kwargs)
    if kwargs["mean_type"] == 1:
        sr_arifm(args)
    else:
        sr_geom(args)

def sr_arifm(a):

    arif = sum(a)/len(a)
    print(f"Среднее арифметическое равно:  {arif}")
def sr_geom(a):
    geom = 1
    for i in a:
        geom *= i
    sr_geo = sqrt(geom)
    print(f"Среднее геометрическое равно:  {int(sr_geo)}")


result_func(21, 343, 33, 21, 56, mean_type = int(input("Введите mean_type")))
