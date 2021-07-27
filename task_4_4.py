
c = [1, 2, 3, 4, 5]
b = []
for i in c[1:]:
    b = b.append(i)
b.append(c[0])
print(b)
c = [1, 2, 3, 4, 5]
b = []
c.reverse()
print(c)
a = len(c)-2
while a >=0:
    b.append(c[a])
    a -= 1
b.append(c[-1])
print(b)
