print('Задача 9. Игра «Угадай число»')

attempts = 1
mystery_num = 0
while mystery_num != 7:
  mystery_num = int(input('Угадайте загаданное число: '))
  if mystery_num > 7:
    attempts += 1
    print('Число больше, чем нужно. Попробуйте ещё раз!')
  elif mystery_num < 7:
    attempts += 1
    print('Число меньше, чем нужно. Попробуйте ещё раз!')
  else:
    break

print('Вы угадали! Число попыток: {}'.format(attempts))
# В одном из домашних заданий мы делали задачу, 
# где папа-программист написал для сына программу, которая просит его угадать число.
# Недостаток программы был в том, 
# что бедному сыну приходилось её каждый раз перезапускать, чтобы угадывать число. 
# Теперь, когда мы знаем гораздо больше,
# пришло время исправить этот недостаток и заодно немного улучшить саму игру.
 
# Напишите программу-игру,
# которая запрашивает у пользователя число до тех пор,
# пока он его не отгадает.
# Выводите сообщения в соответствии с примером.
 
# Пример (загадали число 7):
# Введите число: 3
# Число меньше, чем нужно. Попробуйте ещё раз!
# Введите число: 10
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 8
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 7
# Вы угадали! Число попыток: 4