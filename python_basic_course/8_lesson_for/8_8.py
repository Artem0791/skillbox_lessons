N = int(input('Введите значение N: '))
S = 0
summ = 1
for n in range(N+1):
    S += summ
    summ *= -1/2
print('Сумма ряда равна {}'.format(S))

# Дано натуральное число N.
# Напишите программу для вычисления следующей суммы ряда (начиная с единицы)

# S = 1 - 1/2 + 1/4 - 1/8 + … (-1)**N * 1/2**N