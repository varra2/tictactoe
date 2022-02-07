
def display_board(board):
# Отображение поля на экране

    def make_row(row):
        print(f'\u2502  {row} ', end='')
        for i in board[row]:
            if len(i) == 1:
                print(f' \u2502  {i} ', end='')
            else:
                print(f' \u2502 {i} ', end='')
        print(' '+'\u2502')

    sep = '\u251c'+('\u2500'*5+'\u253c')*10+'\u2500'*5+'\u2524'
    
    print('\u250c'+('\u2500'*5+'\u252c')*10+'\u2500'*5+'\u2510')
    for key in board:
        if key == '#':
            make_row(key)
        else:
            print(sep)
            make_row(key)
    print('\u2514'+('\u2500'*5+'\u2534')*10+'\u2500'*5+'\u2518')
