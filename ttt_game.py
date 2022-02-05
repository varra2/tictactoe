import random

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
        player = input('Вы хотите играть за X или O?').upper()

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

# Тело кода

print('Добро пожаловать в игру "Крестики-нолики"!')

play_board = generate_board()
display_board(play_board)

PLAYER, players_turn = player_input()
RIVAL = 'O' if PLAYER=='X' else 'X'

while True:

    if players_turn:
        print(f"Ваш ход!")
        cell_empty = False
        while not cell_empty:
            CELL = player_choice(play_board, PLAYER)
            cell_empty = space_check(play_board, CELL[0], CELL[1])
        place_marker(play_board, PLAYER, CELL)
        play_board, game_lost = loss_check(play_board, PLAYER)
    else:
        print("Ход противника: ")
        CELL = rival_choice(play_board)
        place_marker(play_board,RIVAL, CELL)
        play_board, game_lost = loss_check(play_board, RIVAL)

    display_board(play_board)
    
    if full_board_check(play_board):
        print('Ничья!')
        break
    if game_lost:
        LINE = "Вы проиграли!" if game_lost == PLAYER else "Вы победили!"
        print(LINE)
        break

    players_turn = switch()
    
print("Игра окончена.")