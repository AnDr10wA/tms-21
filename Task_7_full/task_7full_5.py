"""
Создать функцию, принимающая на вход неопределенное
количество аргументов и возвращающая сумму args[i] * i

Пример: args = [4,3,2,1],
возвращает 4 * 0 + 3 * 1 + 2 * 2 + 1 * 3 = 10

"""

def sum_argfs(*args):
    print(args)
    sumi = 0
    for i in args:
        sumi+=args[i]*i
    print(sumi)
a = [4, 3, 2, 1]
sum_argfs(4, 3, 2, 1)
