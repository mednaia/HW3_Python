# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def convert_decimal_into_binary(number):
    result = " "
    while number > 0:
        bit = number % 2
        result = str(bit) + result
        number = number // 2
    return result

num = int(input("Input decimal number:"))
print(f'Binary number: {convert_decimal_into_binary(num)}')