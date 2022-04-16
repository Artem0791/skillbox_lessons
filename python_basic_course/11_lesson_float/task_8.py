print('Задача 8. Часы')

import math


hour = int(input('Введите градус часовой стрелки: '))

minute = hour * 12

minute = math.radians(minute)

print('Минутная стрелка пройдет расстояние {}'.format(minute))
