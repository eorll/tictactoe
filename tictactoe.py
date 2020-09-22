def table():
    table = {'1': 'O' , '2': 'X' , '3': ' ' ,
            '4': ' ' , '5': 'O' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': 'O' }

    return table


def get_move():
    pass


def mark():
    pass


def has_won():
    pass


def is_full():
    pass


def print_board(table):

    print('   ' + '1' + '   ' + '2' + '   ' + '3')
    print('A  ' + table['1'] + ' |' + ' ' + table['2'] + ' |' + ' ' + table['3'])
    print('  ---+---+---')
    print('B  ' + table['4'] + ' |' + ' ' + table['5'] + ' |' + ' ' + table['6'])
    print('  ---+---+---')
    print('C  ' + table['7'] + ' |' + ' ' + table['8'] + ' |' + ' ' + table['9'])
    


def print_result():
    pass


def tictactoe_game():
    pass

print_board(table())



