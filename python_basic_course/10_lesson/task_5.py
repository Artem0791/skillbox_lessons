first = int(input('Введите начальное число: '))
last = int(input('Введите конечное число: '))
simple_num_list = []

for num in range(first, last):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
       simple_num_list.append(num)

print('Простые числа в заданной последовательности: ', simple_num_list)
# for num in range(2,101):
#     if all(num%i!=0 for i in range(2,num)):
#        print (num)

#Напишите программу,
#которая считает количество простых чисел в заданной последовательности
#и выводит ответ на экран.