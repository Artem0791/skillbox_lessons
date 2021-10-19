totalHours = int(input('Введите количество часов: '))
cells = 1
for hour in range(1, totalHours // 3 + 1):
    cells *= 2
    print('Прошло часов: ', hour * 3)
    print('Кол-во клеток: ', cells)
    print('Осталось часов: ', totalHours - hour * 3)
    print()
print('Наблюдение завершено')
