# a = int(input('Начальное число: '))
# b = int(input('Конечное число: '))
# c = int(input('Кратное число: '))
# num_list = []
# for n in range(a, b):
#     if n % c == 0:
#         num_list.append(n)
#
# middle = sum(num_list) / len(num_list)
# print(num_list)
# print(middle)
a = int(input('Начальное число: '))
b = int(input('Конечное число: '))
c = int(input('Кратное число: '))
num_sum = 0
len_num = 0
for n in range(a, b):
    if n % c == 0:
        num_sum += n
        len_num += 1

middle = num_sum/len_num
print(middle)
#Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль среднее арифметическое
# всех чисел из отрезка [a; b], которые кратны числу c.
# Подсказка: (a и b  являются промежутком, а c для проверки кратности).
