import random

from torch import ge

def generate_board():
    # Генерация значений для ячеек пустого поля

    board = {'#': [str(num) for num in range(1,11)]}
    for letter in 'ABCDEFGHIJ':
        board[letter]= [' ' for num in range(10)]
    return board

def display_board(board):
# Отображение поля на экране

    def make_row(row):
        print(row, end='')
        for i in board[row]:
            print(' | ' + i, end='')
        print('')

    sep = '- | '*10+'-'
    
    print()
    for key in board:
        make_row(key)
        print(sep)
    print()

def player_input():
    #Выбор игровой роли (крестик или нолик)

    player = ""
    while player not in ('X', 'O'):
        player = input('Вы хотите играть за X или O? ').upper()

    if player == 'X':
        players_turn = True
    else:
        players_turn = False

    return player, players_turn

def player_choice(board, player_mark):
    # Выбор ячейи в ход игрока

    row = 'K'
    column = -1

    while (row not in board) or (column not in [num for num in range(1, 11)]):
        try:
            position = input("Выберите свободную ячейку с A1 по J10: ")
            if len(position)!=2 and position[1:]!='10':
                continue
            column = int(position[1:])
            row = position[0].upper()

        except ValueError as exc:
            print(f'Неверное значение: {exc}. Пожалуйста, попробуйте снова.')

    return row, column-1

def space_check(board, row, column):
    #Проверяем, свободна ли ячейка

    return board[row][column] == ' '

def rival_choice(board):
    #Ход противника

    while True:
        row, column = random.choice([key for key in board if key != '#']), random.choice([num for num in range(10)])
        if space_check(board, row, column):
            break
    return row, column

def place_marker(board, marker, cell):
    #Установка маркера в ячейку поля

    row, column = cell
    board[row][column] = marker

def loss_check(board, mark):
    # Проверка на выполнение условия поражения

    loser = False
    rows = 'ABCDEFGHIJ'
    for idx, row in enumerate(rows):
        for i in range(10):
            if i < 6:

                #Проверка строк
                if board[row][i] == board[row][i+1] == board[row][i+2] == board[row][i+3] == board[row][i+4] == mark:
                    board[row][i] = board[row][i+1] = board[row][i+2] = board[row][i+3] = board[row][i+4] = 'Z'
                    loser = mark         
                
                #Проверка главных диагоналей
                elif idx<=5 and board[row][i] == board[rows[idx+1]][i+1] == board[rows[idx+2]][i+2] == board[rows[idx+3]][i+3] == board[rows[idx+4]][i+4] == mark:
                    board[row][i] = board[rows[idx+1]][i+1] = board[rows[idx+2]][i+2] = board[rows[idx+3]][i+3] = board[rows[idx+4]][i+4] = 'Z'
                    loser = mark   
            
                #Проверка побочных диагоналей
                elif idx >=4 and board[row][i] == board[rows[idx-1]][i+1] == board[rows[idx-2]][i+2] == board[rows[idx-3]][i+3] == board[rows[idx-4]][i+4] == mark:
                    board[row][i] = board[rows[idx-1]][i+1] = board[rows[idx-2]][i+2] = board[rows[idx-3]][i+3] = board[rows[idx-4]][i+4] = 'Z'
                    loser = mark
            #Проверка cтолбцов
            if idx <= 5 and board[row][i] == board[rows[idx+1]][i] == board[rows[idx+2]][i] == board[rows[idx+3]][i] == board[rows[idx+4]][i] == mark:
                board[row][i] = board[rows[idx+1]][i] = board[rows[idx+2]][i] = board[rows[idx+3]][i] = board[rows[idx+4]][i] = 'Z'
                loser = mark
            
    return board, loser

def full_board_check(board):
    # Условие ничьей (заполненность доски)

    full = set()
    for value in board.values():
        full = full.union(set(value))
    return ' ' not in full

def switch():
    # Смена хода

    return not players_turn

def end(board, players_turn, player, rival):
    # Проверка на соблюдение условий окончания игры

    board, game_lost = loss_check(board, player) if players_turn else loss_check(board, rival)
    if (not game_lost) and full_board_check(board):
        return ' Ничья! '
    elif game_lost:
        line = ' Победа! :) ' if game_lost == rival else ' Проигрыш... :( '
        return line
    return False

def start():
    # Начало новой игры

    board = generate_board()
    player, players_turn = player_input()
    rival = 'O' if player == 'X' else 'X'

    return board, player, rival, players_turn

def replay():
    # Предложение перезапустить игру

    decision = ""
    while decision not in ('y', 'n', 'yes', 'no', 'д', 'н', 'да', 'нет'):
        decision = input(
            "Вы хотите продолжить игру? (y/n)"
        ).lower()

    return decision in ('y','yes', 'д', 'да')

# Тело кода

print('Добро пожаловать в игру "Крестики-нолики"!')

PLAY_BOARD, PLAYER, RIVAL, players_turn = start()

while True:

    display_board(PLAY_BOARD)

    if players_turn:
        print(f"Ваш ход!")
        cell_empty = False
        while not cell_empty:
            CELL = player_choice(PLAY_BOARD, PLAYER)
            cell_empty = space_check(PLAY_BOARD, CELL[0], CELL[1])
        place_marker(PLAY_BOARD, PLAYER, CELL)
        #PLAY_BOARD, game_lost = loss_check(PLAY_BOARD, PLAYER)
    else:
        print("Ход противника: ")
        CELL = rival_choice(PLAY_BOARD)
        place_marker(PLAY_BOARD,RIVAL, CELL)
        #PLAY_BOARD, game_lost = loss_check(PLAY_BOARD, RIVAL)
    
    game_over = end(PLAY_BOARD, players_turn, PLAYER, RIVAL)

    if game_over:
        display_board(PLAY_BOARD)
        print(game_over)
        if not replay():
            break
        PLAY_BOARD, PLAYER, RIVAL, players_turn = start()
    else:
        players_turn = switch()
    
print("Игра окончена.")