good_customer = 0

for num in range(10):
    user = int(input('Введите номер пользователя: '))
    if user > 0 and user % 2 == 0:
        good_customer += 1
    else:
        continue
print('Законопослушных граждан: ', good_customer)

# Должники и законопослушные граждане хранятся в одной базе банка.
# Из этой базы нам выделяются по 10 человек, у каждого из которых есть свой номер.
# Правда, иногда база глючит и выдаёт нам отрицательный номер.
# А ещё по статистике, которую собрал наш МирПрогБанк,
# каждый второй, кто в этом году брал кредит, не выплатил его вовремя.
#
# Пользователь вводит 10 чисел.
# Напишите программу,
# которая определяет, сколько из них являются одновременно четными и положительными.