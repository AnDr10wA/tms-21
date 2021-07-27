a = [2, 4, 6, 8, 12, 13]
sum = 0
for i in a:
    if i % 2 == 0:
        sum += 1
print(sum)

index_a = list(range(len(a)))
ind = index_a[-1]
sum_w = 0

while ind >= 0:
    if a[ind] % 2 == 0:
        sum_w += 1
    ind -= 1
print(sum_w)
