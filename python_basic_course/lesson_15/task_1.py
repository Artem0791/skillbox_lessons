def make_list():
    ready_list = []
    n = int(input('Введите число: '))
    for i in range(n):
        if i % 2 != 0:
            ready_list.append(i)
    print('Список из нечётных чисел от одного до N: {}'.format(ready_list))


make_list()

# Дано целое число N. Напишите программу, которая формирует список из нечётных чисел от одного до N.
