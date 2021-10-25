num = int(input('Введите число: '))
equal = 0
bigger = 0
for n in range(1, num + 1):
    sum_num = 0
    for symbol in str(n):
        sum_num += int(symbol)
    if sum_num > equal:
        equal = sum_num
        bigger = n
print('наибольшее по сумме цифр число: ', bigger)


# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.
