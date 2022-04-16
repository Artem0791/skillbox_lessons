import math

a = int(input('Длина 1й стороны треуголника: '))
b = int(input('Длина 2й стороны треуголника: '))
c = int(input('Длина 3й стороны треуголника: '))

p = (a+b+c)/2
S = round(math.sqrt(p*(p-a)*(p-b)*(p-c)), 2)

print('Площадь треугольника равна: ', S)
