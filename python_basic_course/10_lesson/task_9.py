layers = int(input('Введите количество уровней пирамиды: '))
num = 1
for layer in range(1, layers + 1):
    for s in range(layers - layer):
        print(end='   ')
    for i in range(layer):
        print(num, end='    ')
        num += 2
    print()


# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
#
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29
