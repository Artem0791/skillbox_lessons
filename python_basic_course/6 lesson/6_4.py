print('Задача 4. Календари')

calendar = []
month = int(input('Введите число: '))
while month != 0:
  if month % 2 == 0:
    calendar.append(month)
    month = int(input('Введите число: '))
  else:
    month = int(input('Введите число: '))
print(calendar)
# Ваня увлекается историей, а в особенности календарями.
# Он изучает календари разных времён, эпох и народностей. 
# Для исследования ему нужно посчитать,
# у кого сколько было месяцев с чётным количеством дней.
 
# Напишите программу,
# которая считает количество только чётных чисел в последовательности 
# (последовательность заканчивается при вводе нуля)
# и выводит ответ на экран.