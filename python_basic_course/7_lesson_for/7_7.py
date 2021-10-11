num_a = int(input('Введите число а: '))
num_b = int(input('Введите число b: '))
sort_nums = []
for num in range(num_a, num_b):
    if num % 3 == 0:
        sort_nums.append(num)

print(sum(sort_nums)/len(sort_nums))
# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль
# среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.
