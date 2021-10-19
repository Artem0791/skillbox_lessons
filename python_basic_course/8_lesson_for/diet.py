wake_up = int(input('Во сколько проснулся?   '))
water = 0
calories_sum = 0

for hour in range(wake_up, 23, 3):
    print('Пошли есть в', hour, 'часов')
    water += 1
    calories = int(input('Сколько съел? '))
    calories_sum += calories
print('Выпито литров воды: {}'.format(water))
print('Съедено калорий: {}'.format(calories_sum))