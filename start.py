board_size = 3 #кол-во клеток
board = [1,2,3,4,5,6,7,8,9]
def draw_board(): #функция будет выводить игровое поле
    print('-' * 4 * board_size)
    for i in range(board_size):
        print((' ' * 3 + '|') *3)
        print('',board[i*3], '|', board[1 + i*3], '|', board[2 + i*3], '|')
        print(('_' * 3 + '|') *3)
    pass
def game_step(index, char): #выполнение хода
    if (index > 9 or index < 1 or board[index-1] in ('X', 'O')):
        return False
    board[index - 1] = char
    return True
    pass
def check_win(): # проверка победившего
    win = False

    win_comb = (0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,7)
    for pos in win_comb:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]):
            win = board[pos[0]]
    return win
def start_game(): #начало игры
    current_player = 'X' #кто ходит
    step = 1 #номер хода
    draw_board()
    while (step < 10) and (check_win() == False):
        index = input('Ходит игрок ' + current_player + ' Введите номер поля (0-выход):')
        if(index == '0'):
            break

        if (game_step(int(index), current_player)):
            print('Ход совершён')
            if (current_player == 'X'):
                current_player = 'O'
            else:
                current_player = 'X'
            draw_board()
            step += 1 #увеличим номер хода
        else:
            print('Неверный номер клетки,попробуйте снова')
    if (step == 10):
     print("Игра окончена, у вас ничья!")
    else:
     print('Выйграл ' + check_win())

print('Игра в крестики-нолики началась!')
start_game()