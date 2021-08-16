from exception import *


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def summa(self):
        result = self.a + self.b
        return result

    def division(self):
        result = " "
        try:
            result = self.a/self.b
        except ZeroDivisionError as err:
            print(f"Деление на 0 невозможно {err}")
        else:

            result = self.a/self.b
        return result

    def mult(self):
        result = self.a*self.b
        return result

    def sub(self):
        result = self.a-self.b
        return result



if __name__ == '__main__':
    a = 7
    b = 2
    print(summa(a,b))



