edge_len = int(input('Введите длину грани: '))

for row in range(edge_len):
    for col in range(edge_len * 2):
        if row == 0 or row == edge_len - 1:
            print('-', end='')
        elif col == 0 or col == edge_len * 2 - 1:
            print('|', end='')
        else:
            print(' ', end='')
    print()
