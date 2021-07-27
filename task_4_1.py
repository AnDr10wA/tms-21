a = [2, 4, 6, 8, 12, 13]

for i in a:

    a[a.index(i)] = i*(-2)
print(a)
index_a = list(range(len(a)))
ind = index_a[-1]


while ind >= 0:
    a[ind] = a[ind]*(-2)
    ind -= 1
print(a)
