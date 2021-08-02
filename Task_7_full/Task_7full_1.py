"""
Написать функцию, которая получает на вход имя и выводит
строку вида: “Hello, {name}”. Создать список из 5 имен.
Вызвать функцию для каждого элемента списка в цикле.
"""
def name_rep(name):
    print(f"Hello,  {name}")
    pass

spisok_name = ["Lera", "Andrei", "Egor", "Vasya", "Nik"]

for i in spisok_name:
    name_rep(i)