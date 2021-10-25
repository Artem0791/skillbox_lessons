num = int(input('Введите число: '))
fac_sum = 0
for f in range(1, num + 1):
    factorial = 1
    for n in range(1, f + 1):
        factorial *= n
    fac_sum += factorial
print('Сумма факториалов равна {}'.format(fac_sum))

# Напишите программу,
# которая запрашивает у пользователя число N
# и находит сумму факториалов 1! + 2! + 3! +... + N!
