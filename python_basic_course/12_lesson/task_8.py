#Напишите функцию, вычисляющую наибольший общий делитель двух чисел
def divider(a, b):
    n = max(a, b)
    max_divider = 0
    for i in range(1, n):
        if a % i == 0 and b % i == 0:
            max_divider = i
    print('Наибольший общий делитель: {}'.format(max_divider))


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
divider(a, b)
