
from classes import *

circl = Circle(p1 = (1,1), r = 5)
trian = Triangle(p1 = (3,0), p2= (3,4), p3 = (6,0))
square = Square(p1 = (0,0), p2 = (0,5))


print(f"Площадь круга равна  {circl.square()}")
print(f"Периметр круга равен  {circl.perimetr()}")
print(f"Площадь треугольника равна {trian.square()}")
print(f"Периметр треугольника равен {trian.perimetr()}")
print(f"Площадь квадрата равна  {square.square()}")
print(f"Периметр квадрата равен  {square.perimetr()}")