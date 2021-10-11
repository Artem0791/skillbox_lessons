sort_list = []

for num in range(10, 100):
    first = num // 10
    second = num % 10
    mult = (first * second) * 3
    if num == mult:
        sort_list.append(num)
    else:
        continue

print(sort_list)

#Напишите программу,
# которая находит и выводит все двузначные числа,
# которые равны утроенному произведению своих цифр.
# К таким относятся, например, 15 и 24.