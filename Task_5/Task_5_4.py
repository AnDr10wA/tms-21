

def nnn(n):
    sum = 0
    n = n+1
    for i in range(1, n):
        sum += 1/i
    return sum
res = nnn(6)
print(res)
