string = input('Введите строку: ')
prevSym = ''
equalSym = False
for letter in string:
    if prevSym == letter:
        equalSym = True
        break
    else:
        prevSym = letter

if equalSym:
    print('Обнаружены 2 одинаковые буквы подряд')
else:
    print('Нет одинаковых букв подряд')
