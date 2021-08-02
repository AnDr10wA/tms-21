from random import randint

def create_func(n, random_from = 1, random_to=9):

    matrix = [[randint(random_from, random_to) for i in range(n)] for j in range(n)]
    for i in matrix:
        print(i)

create_func(5, 2, 15)