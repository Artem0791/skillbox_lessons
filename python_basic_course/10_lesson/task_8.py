size = int(input('Введите число: '))
for s in range(size):
    for i in range(size - s - 1):
        print(end=' ')
    for j in range(2*s - 1):
        print("#", end='')
    print()

# Напишите программу,
# которая выводит на экран равнобедренный треугольник (пирамидку),
# заполненный символами хэштега "#". Пусть высота пирамиды вводится пользователем.


# Подсказка: вспомните, как выводился колонтитул вида -----!!!!!!-----

   #
  ###
 #####
#######