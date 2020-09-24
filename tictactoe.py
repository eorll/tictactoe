import os

# Rzeczy do zrobienia:
# menu 
# personalizacja - typu nickname i jakieś inne
# dodatkowe tryby gry - player vs AI + poziomy trudności 
# dodać kolory? dzwiek? jakies inne pierdoly?
# ????




def table():
    table = {'A1': ' ' , 'A2': ' ' , 'A3': ' ' ,
            'B1': ' ' , 'B2': ' ' , 'B3': ' ' ,
            'C1': ' ' , 'C2': ' ' , 'C3': ' ' }

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

    


def mark(used_moves_o, used_moves_x):
    # oznacza x i o na tablicy
    table1 = table()
    for i in used_moves_o:
        table1[i] = "O"
    for i in used_moves_x:
        table1[i] = "X"

    return table1


def has_won(used_moves_o, used_moves_x):
    win_moves = [['A1','A2','A3'], ['B1','B2','B3'], ['C1','C2','C3'], ['A1','B1','C1'], ['A2','B2','C2'], ['A3','B3','C3'], ['A1','B2','C3'],['A3','B2','C1']]
    smb_won = False
    for i in win_moves:
        result_o = all(elem in used_moves_o for elem in i)
        result_x = all(elem in used_moves_x for elem in i)
        if result_o:
            print("Player O won!")
            smb_won = True
            return smb_won
        elif result_x:
            print("Player X won!")
            smb_won = True
            return smb_won

    return smb_won
    
        
def print_table(table):

    print('   ' + '1' + '   ' + '2' + '   ' + '3')
    print('A  ' + table['A1'] + ' |' + ' ' + table['A2'] + ' |' + ' ' + table['A3'])
    print('  ---+---+---')
    print('B  ' + table['B1'] + ' |' + ' ' + table['B2'] + ' |' + ' ' + table['B3'])
    print('  ---+---+---')
    print('C  ' + table['C1'] + ' |' + ' ' + table['C2'] + ' |' + ' ' + table['C3'])
    

def tictactoe_game():
    possible_moves = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    used_moves_x = []
    used_moves_o = []
    
    flag = True

    while flag:
        os.system("cls || clear")
        print_table(mark(used_moves_o, used_moves_x))
        if possible_moves == []:
            print("Remis")
            flag = False
        else:
            if has_won(used_moves_o,used_moves_x):
                flag = False
            else:
                print('Player O')
                move = get_move(possible_moves)
                possible_moves.remove(move)
                used_moves_o.append(move)
                os.system("cls || clear")
            if has_won(used_moves_o,used_moves_x):
                flag = False
            else:
                print_table(mark(used_moves_o, used_moves_x))
                print('Player X')
                move = get_move(possible_moves)
                possible_moves.remove(move)
                used_moves_x.append(move)
                
                
   
tictactoe_game()
    





