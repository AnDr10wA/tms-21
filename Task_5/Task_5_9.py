m = int(input("Введите число: "))
delit = ""
for i in range(m-1, 1, -1):
    if m % i == 0:
        delit += f"{i}  "
        
print(f"Делители числа {delit}")