def containers():
    container_list = []
    count_cont = int(input('Количество контейнеров: '))
    for _ in range(count_cont):
        cont = int(input('Введите вес контейнера: '))
        container_list.append(cont)
    container_list.sort()
    container_list.reverse()
    return container_list


def new_container():
    cont_list = containers()
    new_cont = int(input('Введите вес нового контейнера: '))
    index_cont = 1
    for c in cont_list:
        if new_cont > c:
            cont_list.index(new_cont, cont_list[index_cont])
        else:
            index_cont += 1
    print('Номер, который получит новый контейнер: {}'.format(index_cont))


new_container()
