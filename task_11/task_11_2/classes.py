"""
Создать класс Point, описывающий точку(атрибуты: x, y). Создать класс
Figure. Создать три дочерних класса Circle(атрибуты: координаты
центра(тип Point), длина радиуса; методы: нахождение периметра и
площади окружности), Triangle(атрибуты: три точки, методы: нахождение
площади и периметра), Square(атрибуты: две точки, методы: нахождение
площади и периметра). При потребности создавать все необходимые
методы не описанные в задании. Создать список фигур и в цикле
подсчитать и вывести площади всех фигур на экран[my-oop-03]
Примечание: в рамках задание создать два файла: ​ classes.py ​ и m
​ ain.py ​ . В
первом будут описаны все классы, во втором классы будут
импортированы и использованы.
"""
import math
# def point():
#     x = 5
#     y = 5
#
#     matrix = [[" "*15]*15]
#     matrix[0][y] = matrix[0][y][:x-1] + "." + matrix[0][y][x:]
#     for i in matrix:
#         for j in i:
#             print(j)





class Point:

    def __init__(self, x , y):
        self.x = x
        self.y = y

class Figure:

    def __init__(self, p1, p2 =None, p3 = None, r = None):

        self.p1 = Point(p1[0], p1[1])
        if p2:
            self.p2 = Point(p2[0], p2[1])
        if p3:
            self.p3 = Point(p3[0], p3[1])
        self.r = r

class Circle(Figure):

    def square(self):
        square = 3.14 * self.r**2
        return square

    def perimetr(self):
        perim = 2*3.14*self.r
        return perim

class Triangle(Figure):

    def square(self):

        square = abs((self.p1.x-self.p3.x)*(self.p2.y - self.p3.y) - (self.p1.y - self.p3.y)*(self.p2.x - self.p3.x)) * 0.5
        return square



    def perimetr(self):

        ab = math.sqrt((self.p2.x-self.p1.x)**2 + (self.p2.y - self.p1.y)**2)
        bc = math.sqrt((self.p3.x - self.p2.x)**2 + (self.p3.y-self.p2.y)**2)
        ac = math.sqrt((self.p3.x - self.p1.x)**2 + (self.p3.y - self.p1.y)**2)
        perim = ab+bc+ac
        return perim

class Square(Figure):

    def square(self):
        ab = math.sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2)
        square = ab**2
        return square

    def perimetr(self):
        ab = math.sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2)
        perim = ab*4
        return perim





