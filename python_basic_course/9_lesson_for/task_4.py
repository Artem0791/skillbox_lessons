print('Сцена')

rows = int(input('Введите кол-во рядов: '))
seats = int(input('Введите кол-во сидений в ряду: '))
distance = int(input('Введите кол-во метров между рядами: '))
row_view = ''
seats_view = ''
distance_view = ''

for seat in range(seats):
    seats_view += '='
for dis in range(distance):
    distance_view += '*'
for row in range(rows):
    row_view += seats_view + ' ' + distance_view + ' ' + seats_view + '\n'


print(row_view)

# Планируется построить театр под открытым небом,
# но для начала нужно хотя бы примерно понять сколько должно быть рядов,
# сидений в них и какое лучше сделать расстояние между рядами.
#
# Напишите программу,
# которая получает на вход кол-во рядов, сидений и свободных метров между рядами,
# а затем выводит примерный макет театра на экран.

# Сцена
# Введите кол-во рядов: 5
# Введите кол-во сидений ряду: 7
# Введите кол-во метров между рядами: 3
#
# ======= *** =======
# ======= *** =======
# ======= *** =======
# ======= *** =======
# ======= *** =======