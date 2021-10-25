while True:
    for attempt in range(1, 4):
        pincode = int(input('Введите пинкод: '))
        if pincode == 1234:
            print('\nПинкод верный. Получите зарплату!')
            break
        print('Неверный пинкод! Остлось {} попыток.'.format(3 - attempt))
    else:
        print('\nВаша карта заблокирована')
    print('Следующий клиент, добро пожаловать!')