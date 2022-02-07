"""Написать программу, где две функции -- "Игрок 1" и "Игрок 2"
играют в игру, а третья функция -- "Судья" -- следит за ходом игры
и ведёт счёт.

Правила игры:
Оба игрока кажый раунд выдают случайное целое число
в некотором диапазоне. Судья сравнивает эти числа и начисляет игрокам очки:
Если числа равны, оба игрока получают 1 очко (+1). Когда число одно из игроков
больше другого, игрок, который выдал большее число, получает 1 очко (+1),
другой игрок штрафуется на 1 очко (-1). Игра продолжается до тех пор, пока
один из игроков не наберёт 50 очков, но не более 100 раундов."""

from random import randint

points = [0] * 2
ranges = [[-1000, 1000]] * 2
defeats_in_row = [0] * 2
cheat_chance = [0] * 2


def player(player_num):
    player_num -= 1

    if defeats_in_row[player_num] >= 3:
        cheat_chance[player_num] += 5
        if cheat_chance[player_num] > 95:
            cheat_chance[player_num] = 95
        if cheat_chance[player_num] <= randint(0, 100):
            ranges[player_num][0] += 1000
            ranges[player_num][1] += 1000

    return randint(*(ranges[player_num]))


def try_cheat(player_num):
    pass


def judge(choice1, choice2):
    if choice1 == choice2:
        points[0] += 1
        points[1] += 1
    elif choice1 > choice2:
        points[0] += 1
        points[1] -= 1
        defeats_in_row[1] += 1
    else:
        points[0] -= 1
        points[1] += 1
        defeats_in_row[0] += 1


for i in range(1000):
    judge(player(1), player(2))

    if points[0] >= 50 and points[1] >= 50:
        print('Ничья!')
        break
    elif points[0] >= 50:
        print('1-ый игрок выиграл!')
        break
    elif points[1] >= 50:
        print('2-ой игрок выиграл!')
        break
else:
    print('Раунды кончились!')
