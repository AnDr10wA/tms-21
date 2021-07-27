

while True:
    x = int(input("Введите Х: "))
    y = int(input("Ведите У: "))
    sign = input("Ведите операцию: ")
    if sign == "+":
        print(x+y)
    elif sign == "-":
        print(x-y)
    elif sign == "/":
        if y == 0:
            print("y не может быть равен 0")
        else:
            print(x/y)
    elif sign == "*":
        print(x*y)
    elif sign == "0":
        break
    else:
        "Введена неверная операция"

