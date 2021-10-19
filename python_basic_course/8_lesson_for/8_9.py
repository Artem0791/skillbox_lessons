x = int(input('Введите число х: '))

num_one = 1
num_two = 1
for i in range(1, 7):
    num_one *= (x - (2**i - 1))
    num_two *= (x - 2**i)
print(num_one/num_two)

# list_one = [2**n - 1 for n in range(1, 7)]
# list_two = [2**n for n in range(1, 7)]
# num_one = 1
# num_two = 1
# for i in list_one:
#     num_one *= (x - i)
# for i in list_two:
#     num_two *= (x - i)
# result = num_one/num_two
# print(result)


# Дано число x.
# Напишите программу для вычисления следующего выражения

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64))

