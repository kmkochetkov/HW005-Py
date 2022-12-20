# Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# 2021 21 ---> 2000 бот4 -> 1996 .... бот --->29 --> 27 >> 2конф

from random import randint as random

# Конфеты на столе
existsCandy = 120

#Количество конфет, которое забирает человек и бот не подсчитывается, так как признаком победы считаетс ятот, кто забирает последнюю конфету
#playerTook = 0
#botTook = 0

# Количество конфет, которое поднимают со стола в данный момент
candyMoment = 0

# Выбор того, кто ходит первый производится случайно
def firstStep():
    whoseStep = random(1,2)
    if whoseStep == 1:
        playerStep()
    else:
        botStep()

# Функция - шаг игрока
def playerStep():
    global existsCandy
    global candyMoment

    print(f'\nХод игрока. На столе {existsCandy} конфет')
    candyMoment = int(input('Сколько конфет возьмёте?: '))
    while candyMoment < 1 or candyMoment > 28 or candyMoment > existsCandy:
        candyMoment = int(input(f'Вы взяли недопустимое количество конфет. По правилам можно брать не более 28ми, и не более {existsCandy}\n Сколько конфет возьмете?: '))
    existsCandy -= candyMoment
    if existsCandy > 0:
        botStep()
    else:
        print(f'Выиграл игрок, взяв {candyMoment} конфет')

# Функция - шаг бота
def botStep():
    global existsCandy
    global candyMoment
    print(f'\nХод бота. На столе {existsCandy} конфет')
    maxCandy = existsCandy - 28
    if maxCandy <= 0:
        maxCandy = existsCandy
    else:
        maxCandy = 28

    candyMoment = random(1,maxCandy)
    existsCandy -= candyMoment
    if existsCandy > 0:
        print(f'Бот взял {candyMoment} конфет и ход переходит к игроку')
        playerStep()
    else:
        print(f'Выиграл бот, взяв {candyMoment} конфет')

# Первый шаг, выбор - чей ход
firstStep()