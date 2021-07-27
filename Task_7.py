"""
1. Написать 12 функций по переводу:
Дюймы в сантиметры,Сантиметры в дюймы,Мили в километры,Километры в мили,Фунты в килограммы
Килограммы в фунты,Унции в граммы,Граммы в унции,Галлон в литры,Литры в галлоны,Пинты в литры
Литры в пинты
Примечание: функция принимает на вход число и возвращает конвертированное число
2. Написать программу, со следующим интерфейсом: пользователю предоставляется на
выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
от одного до двенадцати. После программа запрашивает ввести численное значение.
Затем программа выдает конвертированный результат. Использовать функции из первого
задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.
"""

def duim_in_sant(a):
    sant = a*2.54
    return sant
def sant_in_duim(a):
    duim = a/2.54
    return duim
def mile_in_km(a):
    km = a*1.6
    return km
def km_in_mile(a):
    mile = a/1.6
    return mile
def funt_in_kg(a):
    kg = a*2.2
    return kg
def kg_in_funt(a):
    funt = a/2.2
    return funt
def unc_in_gram(a):
    gram = a*28.35
    return gram
def gram_in_unc(a):
    unc = a/28.35
    return unc
def galon_in_litr(a):
    litr = a*3.785
    return litr
def litr_in_galon(a):
    galon = a/3.785
    return galon
def pint_in_litr(a):
    litr = a*1.76
    return litr
def litr_in_pint(a):
    pint = a/1.76
    return pint


spisok = { "1": "Дюймы в сантиметры", "2": "Сантиметры в дюймы", "3": "Мили в километры",
        "4":"Километры в мили", "5":"Фунты в килограммы", "6": "Килограммы в фунты",
        "7": "Унции в граммы", "8": "Граммы в унции", "9":"Галлон в литры",
        "10": "Литры в галлоны", "11": "Пинты в литры", "12": "Литры в пинты"}
for i in list(spisok.keys()):
    print(f"Введите {i} для перевода {spisok[i]}")

while True:
    func = input("Выберите финкцию: ")
    if func == "0":
        print("Программа завершена")
        break
    a = float(input("Введите значение: "))
    spisok_func = {"1": duim_in_sant(a), "2": sant_in_duim(a), "3": mile_in_km(a),
                   "4": km_in_mile(a), "5": funt_in_kg(a), "6": kg_in_funt(a),
                   "7": unc_in_gram(a), "8": gram_in_unc(a), "9": galon_in_litr(a),
                   "10": litr_in_galon(a), "11": pint_in_litr(a), "12": litr_in_pint(a)}

    print(spisok_func[func])
