# Крестики-нолики


# Список начальных клеток
board = list(range(1, 10))

# Выигрышные комбинации - горизонтали + вертикали + диагонали
wins = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9)]


# Рисуем доску 3*3
def game_board():
    print(' -----------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|', '\n', '-----------')


# game_board()

# Ввод пользователя. Обозначается токеном "0" либо "X"
def user_input(token):
    while True:
        value = input('Куда ставим ' + token + '?: ')
        if not (value in '123456789'):
            print('Ошибочный ввод расположения. Пожалуйста, повторите:')
            continue
        value = int(value)
        if str(board[value - 1]) in 'X0':
            print('Клетка занята!')
            continue
        board[value - 1] = token
        break


# Проверка победителя
def winners():
    for each in wins:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[1] - 1]
    else:
        return False


# Основной метод
def main():
    counter = 0
    while True:
        game_board()
        if counter % 2 == 0:
            user_input('X')
        else:
            user_input('0')
        if counter > 3:
            winner = winners()
            if winner:
                game_board()
                print(winner, 'выиграл !')
                break
        counter += 1
        if counter > 8:
            game_board()
            print('Ничья')
            break


# Основная программа
main()
