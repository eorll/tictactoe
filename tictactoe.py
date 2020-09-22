def table():
    table = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

    return table


def get_move(possible_moves):
    
    # sprawdza możliwe ruchy
    # possible_moves = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    flag = True

    while flag:
        move = input("Enter coordinates (e.g. A1): ")
        if move in possible_moves:
            return move
        else: 
            print("Enter valid coordinates!")

    


def mark(move):

    # rysuje X - tymczasowo tylko raz ;)
    possible_moves = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    used_moves = []
    used_moves.append(move)
    table1 = table()
    for i in used_moves:
            m = possible_moves.index(i) + 1
            table1[str(m)] = "X"
    return table1




def has_won():
    pass


def is_full():
    pass


def print_table(table):

    print('   ' + '1' + '   ' + '2' + '   ' + '3')
    print('A  ' + table['1'] + ' |' + ' ' + table['2'] + ' |' + ' ' + table['3'])
    print('  ---+---+---')
    print('B  ' + table['4'] + ' |' + ' ' + table['5'] + ' |' + ' ' + table['6'])
    print('  ---+---+---')
    print('C  ' + table['7'] + ' |' + ' ' + table['8'] + ' |' + ' ' + table['9'])
    


def print_result():
    pass


def tictactoe_game():
    possible_moves = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

    print_table(table())
    move = get_move(possible_moves)
    possible_moves.remove(move)
    print_table(mark(move))

   

    
tictactoe_game()




