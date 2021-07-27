n = input("Введите число: ")
sum = 0
mult = 1
for i in n:
    sum += int(i)
    mult *= int(i)
print(sum, mult)
