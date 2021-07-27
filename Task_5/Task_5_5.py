from random import *

n = 19
l1 = []
for i in range(n):
    l1.append(randint(1,100))
print(l1)
l2 = l1.copy()
def maks(n):
    n.sort()
    maks = n[-1]
    return maks
for i in range(len(l1)):

    if l2[i] % 2 == 0:
        l2[i] = maks(l1)
print(l2)
print(maks(l1))