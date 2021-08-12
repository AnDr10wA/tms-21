"""
Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы:
переопределить магические методы сравнения(==, !=, >=, <=, <, >),
сложения, вычитания, умножения на число, вывод на экран. Перегрузить
конструктор на обработку входных параметров вида: одна строка, три
числа, другой объект класса MyTime, и отсутствие входных параметров.
Реализовать нормальное отображение времени(​ 12:65:83​ - 13:06:23)
"""

class MyTime:

    def __init__(self, hours = 0, minutes =0, seconds = 0, one_str = None, obj_mytime = None ):


        if one_str:
            time = one_str.split(":")

            self.hours = int(time[0])
            self.minutes = int(time[1])
            self.seconds = int(time[2])

        elif obj_mytime:
            self.hours = obj_mytime.hours
            self.minutes = obj_mytime.minutes
            self.seconds = obj_mytime.seconds
        else:
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds

    def norm_time(self, obj):

        seconds = obj.seconds % 60
        minutes = (obj.minutes + (obj.seconds // 60)) % 60
        hours = obj.hours + (obj.minutes + (obj.seconds // 60)) // 60
        return MyTime(hours, minutes, seconds)




    def __add__(self, arg):
        minutes = self.minutes + arg.minutes
        hours = self.hours + arg.hours
        seconds = self.seconds + arg.seconds

        return self.norm_time(MyTime(hours, minutes, seconds))

    def __mul__(self, arg):
        hours = self.hours*arg
        minutes = self.minutes*arg
        seconds = self.seconds*arg
        return  self.norm_time(MyTime(hours, minutes, seconds))

    def __sub__(self, arg):
        hours = self.hours - arg.hours
        minutes = self.minutes - arg.minutes
        seconds = self.seconds - arg.seconds
        return self.norm_time(MyTime(hours, minutes, seconds))

    def __eq__(self, arg):

        return (self.hours == arg.hours) and (self.minutes == arg.minutes) and (self.seconds == arg.seconds)
    def __ne__(self, arg):
        return (self.hours != arg.hours) and (self.minutes != arg.minutes) and (self.seconds != arg.seconds)
    def __lt__(self, arg):
        return (self.hours < arg.hours) and (self.minutes < arg.minutes) and (self.seconds < arg.seconds)
    def __gt__(self, arg):
        return (self.hours < arg.hours) and (self.minutes < arg.minutes) and (self.seconds < arg.seconds)
    def __le__(self, arg):
        return (self.hours <= arg.hours) and (self.minutes <= arg.minutes) and (self.seconds <= arg.seconds)
    def __ge__(self, arg):
        return (self.hours >= arg.hours) and (self.minutes >= arg.minutes) and (self.seconds >= arg.seconds)



time_1 = MyTime(12, 20, 21)
time_2 = MyTime(5, 23, 22)
print(time_2.hours, time_2.minutes, time_2.seconds)
print(time_1.hours, time_1.minutes, time_1.seconds)
result = time_1 + time_2
print(time_2.hours, time_2.minutes, time_2.seconds)
print(time_1.hours, time_1.minutes, time_1.seconds)
res = time_2 - time_1
res1 = time_1*5
print(res1.hours, res1.minutes, res1.seconds)
print(time_1 == time_2)
print(time_1 != time_2)
print(result.hours, result.minutes, result.seconds)
print(res.hours, res.minutes, res.seconds)
print(time_2.hours, time_2.minutes, time_2.seconds)
print(time_1.hours, time_1.minutes, time_1.seconds)
new_time1 = MyTime(one_str= "23:34:43")
new_time2 = MyTime(one_str= "22:51:55")
print(new_time2.hours, new_time2.minutes, new_time1.seconds)

resu = new_time1 + new_time2
print(resu.hours, resu.minutes, resu.seconds)

