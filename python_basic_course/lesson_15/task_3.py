def bad_cell():
    num_cell = int(input('Количество клеток: '))
    not_valid = []
    for cell in range(num_cell):
        cell_eff = int(input('Эффективность {} клетки: '.format(cell+1)))
        if cell + 1 > cell_eff:
            not_valid.append(cell_eff)
    print('Неподходящие значения: {}'.format(not_valid))


bad_cell()

# Задача 3. Клетки
# Что нужно сделать
#
# В научной лаборатории выводят и тестируют новые виды клеток. Есть список из N этих клеток,
# элементом которого является показатель эффективности, а индексом — ранг клетки.
# Учёные отбирают клетки по следующему принципу: если эффективность клетки меньше её ранга, то она не подходит.
#
# Напишите программу, которая выводит на экран элементы списка, значения которых меньше их индекса.