"""
1. Создать пять классов описывающие реальные объекты. Каждый класс
должен содержать минимум три приватных атрибута, конструктор, геттеры
и сеттеры для каждого атрибута, два метода.
"""

class Phone:
    def __init__(self, model = None, number = None, master = None, made_in = None, brand = None ):
        self.model = model
        self.__number = number
        self.__master = master
        self.__made = made_in
        self.brand = brand

    @property
    def brand1(self):
        print(self.brand)

    @brand1.setter
    def brand1(self, brand):
        self.brand = brand
    @property
    def modeli(self):
        print(self.model)

    @modeli.setter
    def modeli(self, modeli):
        self.model = modeli

    @property
    def number(self):
        print(self.__number)
    @number.setter
    def number(self, setnumber):
        self.__number = setnumber
    @property
    def master(self):
        print(self.__master)
    @master.setter
    def master(self, master):
        self.__master = master
    @property
    def made(self):
        print(self.__made)
    @made.setter
    def made(self, made):
        self.__made = made

    def call(self):
        print("Tik-tok, tik-tok")
    def camera(self):
        print("photo save")



sams = Phone("S7", "37525", "Andi", "Vietnam", "Samsung")

sams.made = "Vietnam"
# sams.made
# sams.master
# sams.number
# sams.modeli
# sams.brand1
# sams.call()
# sams.camera()


class Country:

    def __init__(self, name, square =None, population = None, presedent = None, army = None, capital = None):
        self.name = name
        self.__square = square
        self.__population = population
        self.presedent = presedent
        self.__army = army
        self.capital = capital

    @property
    def sg_name(self):
        print(self.name)
    @sg_name.setter
    def sg_name(self, name):
        self.name = name
    @property
    def square(self):
        print(self.__square)
    @square.setter
    def square(self, square):
        self.__square = square
    @property
    def population(self):
        print(self.__population)
    @population.setter
    def population(self, population):
        self.__population = population
    @property
    def sg_presedent(self):
        print(self.presedent)
    @sg_presedent.setter
    def sg_presedent(self, presedent):
        self.presedent = presedent
    @property
    def army(self):
        print(self.__army)
    @army.setter
    def army(self, army):
        self.__army = army

    @property
    def sg_capital(self):
        print(self.capital)
    @sg_capital.setter
    def sg_capital(self, capital):
        self.__capital = capital


    def holiday(self):
        print("Страна отдыхает")

    def elections(self):
        print("Вибираем нового президента")











bel = Country("Belarus", "207k", "10M", "Lykashenko", 65000, "Minsk")
# bel.holiday()
# bel.elections()
# bel.sg_name
# bel.square
# bel.population
# bel.sg_presedent
# bel.sg_capital
# bel.army

class Human:
    def __init__(self, gender, first_name, last_name, age, profession, number_phone, pasport_number ):
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.__profession = profession
        self.__numberphone = number_phone
        self.__pasportnumber = pasport_number

    def setgender(self, gender):
        self.gender = gender

    def getgender(self):
        print(self.gender)

    def get_first_name(self):
        print(self.first_name)

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        print(self.last_name)

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_age(self):
        print(self.age)

    def set_age(self, age):
        self.age = age

    def get_profession(self):
        print(self.__profession)

    def set_profession(self, profession):
        self.__profession = profession

    def get_phone(self):
        print(self.__numberphone)

    def set_phone(self, numberphone):
        self.__numberphone = numberphone

    def get_pasport(self):
        print(self.__pasportnumber)

    def set_pasport(self, pasport):
        self.__pasportnumber = pasport


    def work(self):
        print("Work and work!!")

    def hello(self):
        print("Hello world!")


andi = Human("Man", "Andi", "Antowin", "32", "ingineer", "3752592931293", "232412")

andi.get_age()
andi.get_profession()
print(andi.age)
andi.set_profession("Doctor")
andi.get_profession()
andi.hello()


