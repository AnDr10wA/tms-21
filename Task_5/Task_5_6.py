from random import *


a = []
n = 20
for i in range(n):
    a.append(randint(1, 10))
print(a)
for i in range(len(a)):
    l1 = []
    if a[i] > a[i - 1]:
        l1.append(a[i-1])
        l1.append(a[i])
        n = 1
        if i < len(a) - 1:
            while a[i]<a[i+n]:
                l1.append(a[i+n])
                n+=1
                break
        print(l1)
