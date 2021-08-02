"""
Написать программу для работы с матрицами:
1. Создание
2. Вывод
3. Сумма всех элементов
4. Нахождение максимального элемента
5. Нахождение минимального элемента.
"""


from random import *

def create_matrix():
    n = 5
    m=5
    a=1
    b=10
    matrix = [[randint(a,b) for i in range(n)] for j in range(m)]

    return matrix

def output_matrix(matrix):
    for i in matrix:
        print(i)
print("Матрица: ")
output_matrix(create_matrix())

def summ_matrix(matrix):
    summ = 0
    for i in matrix:
        summ +=sum(i)

    return summ
print("Сумма элементов матрицы")
print(summ_matrix(create_matrix()))

def max_elem(matrix):
    maxi = []
    for i in matrix:
        maxi.append(max(i))
    print(max(maxi))
    return max(maxi)
print("Максимальный  элемент матрицы")
max_elem(create_matrix())

def min_elem(matrix):
    mini = []
    for i in matrix:
        mini.append(min(i))
    print(min(mini))
    return min(mini)
print("Минимальный элемент матрицы")
min_elem(create_matrix())
