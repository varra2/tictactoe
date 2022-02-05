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

def loose_check(board, mark):
    # Условие поражения

    winner = False
    rows = 'ABCDEFGHIJ'
    for idx, row in enumerate(rows):
        for i in range(10):
            if i < 6:

                #Проверка строк
                if board[row][i] == board[row][i+1] == board[row][i+2] == board[row][i+3] == board[row][i+4] == mark:
                    board[row][i] = board[row][i+1] = board[row][i+2] = board[row][i+3] = board[row][i+4] = 'Z'
                    winner = mark         
                
                #Проверка главных диагоналей
                elif idx<=5 and board[row][i] == board[rows[idx+1]][i+1] == board[rows[idx+2]][i+2] == board[rows[idx+3]][i+3] == board[rows[idx+4]][i+4] == mark:
                    board[row][i] = board[rows[idx+1]][i+1] = board[rows[idx+2]][i+2] = board[rows[idx+3]][i+3] = board[rows[idx+4]][i+4] = 'Z'
                    winner = mark   
            
                #Проверка побочных диагоналей
                elif idx >=4 and board[row][i] == board[rows[idx-1]][i+1] == board[rows[idx-2]][i+2] == board[rows[idx-3]][i+3] == board[rows[idx-4]][i+4] == mark:
                    board[row][i] = board[rows[idx-1]][i+1] = board[rows[idx-2]][i+2] = board[rows[idx-3]][i+3] = board[rows[idx-4]][i+4] = 'Z'
                    winner = mark
            #проверка cтолбцов
            elif idx <= 5 and board[row][i] == board[rows[idx+1]][i] == board[rows[idx+2]][i] == board[rows[idx+3]][i] == board[rows[idx+4]][i] == mark:
                board[row][i] = board[rows[idx+1]][i] = board[rows[idx+2]][i] = board[rows[idx+3]][i] = board[rows[idx+4]][i] = 'Z'
                winner = mark
            
    return board, winner

def full_board_check(board):
    # Условие ничьей (заполненность доски)

    full = set()
    for value in board.values():
        full = full.union(set(value))
    return ' ' not in full

def switch():
    # Смена хода

    return not PLAYERS_TURN

# Тело кода

print('Добро пожаловать в игру "Крестики-нолики"!')

PLAY_BOARD = generate_board()
display_board(PLAY_BOARD)

PLAYER, PLAYERS_TURN = player_input()
RIVAL = 'O' if PLAYER=='X' else 'X'

while True:

    if PLAYERS_TURN:
        print(f"Ваш ход!")
        EMPTY = False
        while not EMPTY:
            CELL = player_choice(PLAY_BOARD, PLAYER)
            EMPTY = space_check(PLAY_BOARD, CELL[0], CELL[1])
        place_marker(PLAY_BOARD, PLAYER, CELL)
        PLAY_BOARD, WINNER = loose_check(PLAY_BOARD, PLAYER)
    else:
        print("Ход противника: ")
        CELL = rival_choice(PLAY_BOARD)
        place_marker(PLAY_BOARD,RIVAL, CELL)
        PLAY_BOARD, WINNER = loose_check(PLAY_BOARD, RIVAL)

    display_board(PLAY_BOARD)
    
    if full_board_check(PLAY_BOARD):
        print('Ничья!')
        break
    if WINNER:
        line = "Вы проиграли!" if WINNER == PLAYER else "Вы победили!"
        print(line)
        break

    PLAYERS_TURN = switch()
    
print("Игра окончена.")