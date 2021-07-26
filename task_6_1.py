"""1) Создать матрицу случайных чисел от a до b, размерность матрицы n*m
2) Найти максимальный элемент матрицы.
3) Найти минимальный минимальный матрицы.
4) Найти сумму всех элементов матрицы.
5) Найти индекс ряда с максимальной суммой элементов.
6) Найти индекс колонки с максимальной суммой элементов.
7) Найти индекс ряда с минимальной суммой элементов.
8) Найти индекс колонки с минимальной суммой элементов.
9) Обнулить все элементы выше главной диагонали.
10) Обнулить все элементы ниже главной диагонали.
11) Создать две новые матрицы matrix_a, matrix_b случайных чисел
размерностью n*m.
12)Создать матрицу равную сумме matrix_a и matrix_b.
13)Создать матрицу равную разности matrix_a и matrix_b.
14)Создать новую матрицу равную matrix_a умноженной на g. g вводится с
клавиатура"""

from random import *

n = 10
m = 15
a= 0
b = 100
#Создать матрицу случайных чисел от a до b, размерность матрицы n*m
matrix = m*[n*[0]]
matrix = [[randint(a,b) for i in range(n)] for j in range(m)]
print(matrix)
for i in matrix:
    print(i)
#2) Найти максимальный элемент матрицы.

#3) Найти минимальный минимальный матрицы.
def max_elm(matr1):
    maxi = 0
    min_i = 1000
    for i in matr1:

        if min(i) < min_i:
            min_i = min(i)
        if max(i) > maxi:
            maxi = max(i)
    return print(maxi, min_i)
#Найти сумму всех элементов матрицы.
def summ_elem(matr1):
    sum = 0
    for i in matr1:
        for j in i:
            sum += j

    return print(sum)

# 5) Найти индекс ряда с максимальной суммой элементов.
def index_max(matr1):
    summ_row = []
    for i in matr1:
        sum = 0
        for j in i:
            sum += j
        summ_row.append(sum)
    max_inde = summ_row.index(max(summ_row))
    min_index = summ_row.index(min(summ_row))

    return print(max_inde, min_index)

# Найти индекс колонки с максимальной суммой элементов.
#Найти индекс ряда с минимальной суммой элементов.
def index_max_colum(matr1):

    summ_col = []
    sum = 0

    for i in range(len(matr1[0])):
        for j in matr1:
            sum += j[i]
        summ_col.append(sum)
        sum = 0

    max_sum_col = summ_col.index(max(summ_col))
    min_sum_col = summ_col.index(min(summ_col))

    return print(max_sum_col, min_sum_col)

#Обнулить все элементы выше главной диагонали.
def obnull_pump(matr1):
    matr2 = matr1.copy()
    for i in range(len(matr2)):
        for j in range(len(matr2[i])):
            if j>i:
                matr2[i][j] = 0
        print(matr2[i])
    pass


#Обнулить все элементы ниже главной диагонали.



def obnull_dump(matr231):
    matr3 = matr231.copy()
    for i in range(len(matr3)):
        for j in range(len(matr3[i])):
            if j < i:
                matr3[i][j] = 0
        print(matr3[i])

    pass







print("Максимальный и минимальный элементы")
max_elm(matrix)
print("Сумма всех элементов")
summ_elem(matrix)
print("Индекс ряда с максимальной и минимальной суммой элементов")
index_max(matrix)
print("Индекс колонки с максимальной суммой элементов")
index_max_colum(matrix)
print(matrix)
matr11 = matrix[:].copy()
matr12 = matrix[:].copy()
print("обнуление диагонали ниже")
obnull_dump(matr12)
print("обнуление диагонали выше")
obnull_pump(matr11)
print("*"*50)

# Создать две новые матрицы matrix_a, matrix_b случайных чисел
# размерностью n*m. Создать матрицу равную сумме matrix_a и matrix_b.
def matrix_a_and_b(n, m):
    matrix_a = [[randint(1,10) for i in range(n)] for j in range(m)]
    matrix_b = [[randint(1,10) for i in range(n)] for j in range(m)]
    matrix_sum = m*[n*[0]]
    print(matrix_a)
    print(matrix_b)

    for i in range(len(matrix_a)):
        for j in range(len(matrix_a[i])):
            matrix_b[i][j] +=  matrix_a[i][j]
    print("Сумма матриц a и b")
    for elm in matrix_b:
        print(elm)
#Создать матрицу равную разности matrix_a и matrix_b.


def matrix_a_dif_b(n, m):
    matrix_a = [[randint(1,10) for i in range(n)] for j in range(m)]
    matrix_b = [[randint(1,10) for i in range(n)] for j in range(m)]
    matrix_sum = m*[n*[0]]
    print(matrix_a)
    print(matrix_b)

    for i in range(len(matrix_a)):
        for j in range(len(matrix_a[i])):
            matrix_b[i][j] -=  matrix_a[i][j]
    print("Разница матриц a и b")
    for elm in matrix_b:
        print(elm)
#Создать новую матрицу равную matrix_a умноженной на g. g вводится с клавиатуры

def matrix_a_g(n, m):
    matrix_a = [[randint(1,10) for i in range(n)] for j in range(m)]
    g = int(input("Введите g: "))

    print(matrix_a)


    for i in range(len(matrix_a)):
        for j in range(len(matrix_a[i])):
            matrix_a[i][j] *=  g
    print("Новая матрица a и g")
    for elm in matrix_a:
        print(elm)



matrix_a_and_b(5, 5)
print("Разница матриц A и B")
matrix_a_dif_b(5, 5)
matrix_a_g(5, 5)