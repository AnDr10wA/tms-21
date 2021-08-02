
from math import *

def is_power_n(k, n):

    if k>0 and n>1:

        if log(k,n) % 1 == 0:
            print("True")
            return 1

        else:
            print("False")




#is_power_n(17, 2)
collection = [2, 10, 16, 25, 625, 14, 8, 125, 23]
sum = 0
for i in collection:
    n = 5
    if is_power_n(i, n) == 1:
        sum += 1

print(sum)







