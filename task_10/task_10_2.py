"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
разворот(изменение знака скорости). Все атрибуты приватные.
"""

class Car:
    def __init__(self, brand, model, year_issue, speed = 0):
        self.__brand = brand
        self.__model = model
        self.__year_issue = year_issue
        self.__speed = speed

    def more_speed(self, up = 5):
        self.__speed += up

    def less_speed(self, down = 5):
        self.__speed -= down

    def stop(self):
        self.__speed = 0

    def get_speed(self):
        print(self.__speed)

    def rev_speed(self):
        self.__speed = -self.__speed


volvo = Car("Volvo", "XC90", "2008", 140)


volvo.get_speed()
volvo.more_speed()
volvo.get_speed()
volvo.less_speed(20)
volvo.get_speed()
volvo.rev_speed()
volvo.get_speed()
