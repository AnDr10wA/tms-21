
print(range(199, 1, -1))
def delitel(var):
    dife = []
    for i in range(var, 1, -1):
        if var % i == 0 and var !=i:
            dife.append(i)
            dife.sort()
    return dife
def sum(delit):
    sum = 0
    for i in delit:
        sum += i
    return sum+1
def friend():
    for number in range(200, 300):

        numbe = sum(delitel(number))
        if numbe > 200 and numbe < 300:
            if sum(delitel(numbe)) == number:
                print(number, numbe)



print(delitel(200))
print(sum(delitel(200)))
print(friend())