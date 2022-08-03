def factorial(n):
    fct = 1
    for s in range(1, n+1):
        fct *= s
    return fct


def f(n, x):
    return (-1**n)*((x)**(2*n))/(2*(factorial(n)))


def row_sum():
    last_x = 1
    sum_x = 0
    n = 1
    while abs(last_x) > precision:
        last_x = f(n, x)
        sum_x += last_x
        n += 1
    return sum_x

precision = float(input('Введите точность: '))
x = float(input('Введите x: '))
print('Сумма ряда =  {}'.format(row_sum()))

# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709
