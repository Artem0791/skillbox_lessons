# Напишите функцию summa_n,
# которая принимает одно целое положительное число N
# и выводит сумму всех чисел от 1 до N включительно.
#
# Пример работы программы:
# Введите число: 5
#
# Я знаю, что сумма чисел от 1 до 5 равна 15


def summa_n(n):
    summa = 0
    for num in range(n+1):
        summa += num
    print('Я знаю, что сумма чисел от 1 до {} равна {}'.format(n, summa))


n = int(input('Введите число: '))
summa_n(n)
