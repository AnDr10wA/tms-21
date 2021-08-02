


def fact2(n):
    if n>0:
        if n % 2 == 0:
            fact = list(range(1, n+1)[1::2])
            print(fact)
            dabl_fact = 1
            for i in fact:
                dabl_fact *= i
            print(dabl_fact)
        else:
            fact = list(range(1, n+1)[::2])
            print(fact)
            dabl_fact = 1
            for i in fact:
                dabl_fact *= i
            print(dabl_fact)
    else:
        print("Введите положительное целое число!")

def main():
    fact2(33)

if __name__ == "__main__":
    main()
