'''Создать матрицу случайных чисел и сохранить ее в json
файл. После прочесть ее, обнулить все четные элементы
и сохранить в другой файл'''
from random import  *
import json

matrix = [[randint(1, 5) for i in range(5) ] for j in range(5)]
print(matrix)
print(json.dumps({"matrix": matrix}))
with open("matrix.txt", "w" ) as j_file:
    j_file.write(json.dumps({"matrix": matrix}))
with open("matrix.txt") as mat_file:
    data = mat_file.read()

    data1 = json.loads(data)
    for i in  data1['matrix']:
        for j in range(len(i)):
            if i[j] % 2 == 0:
                i[j]= 0
    print(data1)
    with open("new_matrix.txt", "w") as data2:
        data2.write(json.dumps({"matrix": data1["matrix"]}))





