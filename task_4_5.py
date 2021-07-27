
c = [1, 1]

for i in range(15):
    c.append(c[-1]+c[-2])

print(c)
a = 15
c = [1, 1]
while a>=0:
    c.append(c[-1] + c[-2])
    a -= 1
print(c)

'''
a = [1, 2, 3, 4, 5]
b = a[1:].copy
d = a[0]
print(d)
c = b.append(d)

print(c)
'''