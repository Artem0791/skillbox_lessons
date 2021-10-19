totalSoldiers = int(input('Кол-во солдат в шеренге: '))
total_rules = int(input('Кол-во правил в уставе? '))
push_ups = 0
for soldier in range(totalSoldiers, 0, -4):
    soldier_rules = int(input('Солдат, назови кол-во правил в уставе: '))
    if total_rules != soldier_rules:
        print('Неверно!', 10 * soldier, 'отжиманий!')
        push_ups += 10 * soldier
print('Общее кол-во отжиманий {}'. format(push_ups))
