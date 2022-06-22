def revert(num):
    return num[::-1]


def sum_nums(n, k):
    return str(int(n) + int(k))


n = input('Введите число N: ')
k = input('Введите число K: ')

summa = sum_nums(n, k)

print('Первое число наоборот: ' + revert(n))
print('Второе число наоборот: ' + revert(k))
print('Сумма: ' + summa)
print('Сумма наоборот: ' + revert(summa))

# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.


# Пример:


# Введите первое число: 102
# Введите второе число: 123


# Первое число наоборот: 201
# Второе число наоборот: 321

# Сумма: 522
# Сумма наоборот: 225