educational_grant = int(input('Ежемесячная стипендия студента: '))
expenses = int(input('Расходы на проживание: '))
need_money = 0
for n in range(10):
    difference = expenses - educational_grant
    need_money += difference
    expenses = expenses + (expenses * 3 // 100)
print('необходимо получить у родителей {}'.format(need_money))


# Ежемесячная стипендия студента составляет educational_grant руб.,
# а расходы на проживание превышают стипендию и составляют expenses руб. в месяц.
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
#
# Составьте программу расчета суммы денег,
# которую необходимо получить у родителей один раз в начале обучения,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.