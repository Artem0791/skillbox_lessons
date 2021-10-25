# cross = int(input('Введите размер креста: '))
# for row in range(cross):
#     for col in range(cross):
#         if row < col and row != cross - (col + 1):
#             print(' ', end=' ')
#         elif row > col and row != cross - (col + 1):
#             print(' ', end=' ')
#         else:
#             print('^', end=' ')
#     print()


cross = int(input('Введите размер креста: '))
for row in range(cross):
    for col in range(cross):
        if (row < col and row != cross - (col + 1)) or (row > col and row != cross - (col + 1)):
            print(' ', end=' ')
        else:
            print('^', end=' ')
    print()


# Напишите программу,
# которая выводит на экран крест из символов “^”.
#
# (Символы выводятся по диагоналям воображаемого квадрата.)
# ^        ^
#  ^      ^
#   ^    ^
#    ^  ^
#     ^^
#     ^^
#    ^  ^
#   ^    ^
#  ^      ^
# ^        ^
