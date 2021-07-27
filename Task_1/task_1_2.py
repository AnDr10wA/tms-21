"""
Даны действительные числа x и y. Получить |x| - |y|/ 1+ |y|
"""

import math


x = 5
y = 4

result = (abs(x)-abs(y))/(1+abs(y))
print(f"Результат равен: {result}")