# Степан, как и большая часть населения планеты,
# для расчёта суммы и разности чисел использует калькулятор.
#
# Однако в работе ему нужно
# делать не только  обычные действия вроде сложения и вычитания,
# а делать что-то вручную он уже устал.
#
# Поэтому Степан решил немного расширить функциональность своего калькулятора.
#
# Напишите программу,
# которая спрашивает у пользователя число и действие,
# которое нужно с ним сделать:
# вывести сумму его цифр,
# вывести максимальную цифру или вывести минимальную цифру.
#
# Каждое действие оформите в виде отдельной функции,
# а основную программу зациклите.


def summa_a(a):
    summa = 0
    if a < 10:
        summa = a
    else:
        a = str(a)
        for num in a:
            num = int(num)
            summa += num
    print(summa)


def bigger_a(a):
    bigger = 0
    if a < 10:
        bigger = a
    else:
        a = str(a)
        for num in a:
            if int(num) > bigger:
                bigger = int(num)
    print(bigger)


def smaller_a(a):
    smaller = 0
    if a < 10:
        smaller = a
    else:
        a = str(a)
        for num in a:
            if smaller == 0:
                smaller = int(num)
            else:
                if smaller > int(num):
                    smaller = int(num)
    print(smaller)


a = int(input('Введите число: '))
do = int(input('Введите действие: \n1 - вывести сумму его цифр '
               '\n2 - вывести максимальную цифру \n3 - вывести минимальную цифру \n'))
if do == 1:
    summa_a(a)
elif do == 2:
    bigger_a(a)
else:
    smaller_a(a)
