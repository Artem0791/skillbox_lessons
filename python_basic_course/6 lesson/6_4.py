print('Задача 4. Календари')

calendar = []
month = None
while month != 0:
  month = int(input('Введите число: '))
  if month % 2 == 0:
    calendar.append(month)
  else:
    continue
print(calendar)
# Ваня увлекается историей, а в особенности календарями.
# Он изучает календари разных времён, эпох и народностей. 
# Для исследования ему нужно посчитать,
# у кого сколько было месяцев с чётным количеством дней.
 
# Напишите программу,
# которая считает количество только чётных чисел в последовательности 
# (последовательность заканчивается при вводе нуля)
# и выводит ответ на экран.