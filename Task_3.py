# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def find_difference_between_max_min(lst):
    new_list = []
    diff = 0
    fraction = 0
    for i in lst:
        if i % 1 != 0:
            fraction = round(i % 1,9)
            new_list.append(fraction)
        else:
            i += 1
    diff = max(new_list) - min(new_list)
    return(diff)

my_list = list(map(float, input('Input numbers: ').split()))
print(find_difference_between_max_min(my_list))