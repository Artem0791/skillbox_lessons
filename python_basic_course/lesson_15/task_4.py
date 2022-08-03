def relevant_gpu():
    gpu_list = []
    model = 0
    num_gpu = int(input('Количество видеокарт: '))
    for gpu in range(num_gpu):
        new_gpu = int(input('{} Видеокарта: '.format(gpu + 1)))
        gpu_list.append(new_gpu)
        if model < new_gpu:
            model = new_gpu
    print('Старый список видеокарт: {}'.format(gpu_list))
    for gpu in gpu_list:
        if gpu == model:
            gpu_list.remove(gpu)
    print('Новый список видеокарт: {}'.format(gpu_list))


relevant_gpu()

# Задача 4. Видеокарты
# Что нужно сделать
#
# В базе магазина электроники есть список видеокарт компании NVIDIA разных поколений.
# Вместо полных названий хранятся только числа, которые обозначают модель и поколение видеокарты.
# Недавно компания выпустила новую линейку видеокарт. Самые старшие поколения разобрали за пару дней.

# Напишите программу, которая удаляет из списка видеокарт наибольшие элементы.