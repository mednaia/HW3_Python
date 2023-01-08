# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]



def product_list(lst):
    lenth = 0
    new_list = []
    product = 0
    if len(lst) % 2 != 0:
        lenth = len(lst)//2 + 1
    else:
        lenth = len(lst)//2
    for i in range(lenth):
        product = lst[i]*lst[len(lst)-i-1]
        new_list.append(product)
    return(new_list)


my_list = list(map(int, input('Input numbers: ').split()))
print(product_list(my_list))


