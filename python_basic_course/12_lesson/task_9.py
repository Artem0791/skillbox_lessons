# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
#
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
#
# Однако программист, на место которого вы пришл
# и, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
#
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
#
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
#
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
#
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.
import random


def rock_paper_scissors():
    player_one = input("Камень, ножницы или бумага: ")
    actions = ["камень", "бумага", "ножницы"]
    player = random.choice(actions)
    if player_one == player:
        print('Ничья')
    elif player_one == actions[0] and player == actions[1]:
        print('Бумага бьет камень, вы проиграли!')
    elif player_one == actions[1] and player == actions[0]:
        print('Бумага бьет камень, вы выиграли!')
    elif player_one == actions[0] and player == actions[2]:
        print('Камень бьет ножницы, вы выиграли!')
    elif player_one == actions[2] and player == actions[0]:
        print('Камень бьет ножницы, вы проиграли!')
    elif player_one == actions[2] and player == actions[1]:
        print('Ножницы бьют бумагу, вы выиграли!')
    elif player_one == actions[1] and player == actions[2]:
        print('Ножницы бьют бумагу, вы проиграли!')
    else:
        print('Выберите предложенные значения')


player = random.randint(0, 10)


def guess_the_number():
    player_one = int(input('Угадай число: '))
    # if player_one == player:
    #     print('Поздравляю! Ты угадал!')
    while player != player_one:
        print('Не угадал! Попробуй еще.')
        player_one = int(input('Угадай число: '))
    print('Поздравляю! Ты угадал!')


def mainMenu():
    game = int(input('Выбери игру: \n 1 - Камень, ножницы, бумага \n 2 - Угадай число\n'))
    if game == 1:
        rock_paper_scissors()
    else:
        guess_the_number()

mainMenu()