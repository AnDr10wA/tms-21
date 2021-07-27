from random import *

n  = 5

m2 = []
for i in range(n):
    m1 = []
    m2.append(m1)
    for i in range(n):
        m1.append(randint(1, 10))
print(m2)
for elem in range(len(m2)):
    l2 = m2[elem].copy()
    l2.sort()
    m2[elem][elem] = l2[-1]
print(m2)