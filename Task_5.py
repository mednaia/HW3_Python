# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def negafibonacci_list(num):
    def fibon_rec(numb: int):
        if (numb <= 1):
            return numb
        else:
            return fibon_rec(numb - 1) + fibon_rec(numb - 2)

    def fibon_rec_neg(numb: int):
        if numb == -1:
            return 1
        elif numb == -2:
            return -1
        else:
            return fibon_rec_neg(numb + 2) - fibon_rec_neg(numb + 1)

    def fibon_list(n: int):
        list = []
        for i in range(-n, 0):
            list.append(fibon_rec_neg(i))
        for i in range(0, n+1):
            list.append(fibon_rec(i))
        return list
    
    if num >= 0:
        my_list = fibon_list(num)
    elif num < 0:
        num = num*-1
        my_list = fibon_list(num)
    return my_list

number = int(input('Enter your number: '))

print(f'Your Fibonacci sequence:\n{negafibonacci_list(number)}')