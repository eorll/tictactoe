import os, random

# Zrobiono:
# easy AI
# medium AI
# poprawiono kod 

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
        move = input("Enter coordinates (e.g. A1): ").upper()
        if move in possible_moves:
            return move
        else: 
            print("Enter valid coordinates!")


def mark(used_moves):
    # oznacza x i o na tablicy
    used_moves_x = o_or_x(used_moves)[1]
    used_moves_o = o_or_x(used_moves)[0]
    table1 = table()
    for i in used_moves_o:
        table1[i] = "O"
    for i in used_moves_x:
        table1[i] = "X"

    return table1


def has_won(used_moves):
    win_moves = [['A1','A2','A3'], ['B1','B2','B3'], ['C1','C2','C3'], ['A1','B1','C1'], ['A2','B2','C2'], ['A3','B3','C3'], ['A1','B2','C3'],['A3','B2','C1']]
    smb_won = False
    used_moves_x = o_or_x(used_moves)[1]
    used_moves_o = o_or_x(used_moves)[0]
    for i in win_moves:
        result_o = all(elem in used_moves_o for elem in i)
        result_x = all(elem in used_moves_x for elem in i)
        if result_o:
            print("Player O won!")
            play_again()
            smb_won = True
            return smb_won
        elif result_x:
            print("Player X won!")
            play_again()
            smb_won = True
            return smb_won

    return smb_won


def o_or_x(used_moves):
    used_moves_o = []
    used_moves_x = []
    for i in used_moves:
        if (used_moves.index(i) + 1) % 2 == 0 :
            used_moves_x.append(i)
        else:
            used_moves_o.append(i)

    return used_moves_o, used_moves_x


def print_table(table):

    print('   ' + '1' + '   ' + '2' + '   ' + '3')
    print('A  ' + table['A1'] + ' |' + ' ' + table['A2'] + ' |' + ' ' + table['A3'])
    print('  ---+---+---')
    print('B  ' + table['B1'] + ' |' + ' ' + table['B2'] + ' |' + ' ' + table['B3'])
    print('  ---+---+---')
    print('C  ' + table['C1'] + ' |' + ' ' + table['C2'] + ' |' + ' ' + table['C3'])
    


def tictactoe_game(game_mode):
    possible_moves = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    used_moves = []
    flag = True

    while flag:
        os.system("cls || clear")
        
        if has_won(used_moves):
            break
        else:
            os.system("cls || clear")
            print('Player 1')
            player_move(possible_moves,used_moves)
        if possible_moves == []:
            print("It's a tie!")
            play_again()
            break
        if game_mode == "AI_easy":
            AI_easy(possible_moves,used_moves)
        if game_mode == 'AI_medium':
            AI_medium(possible_moves,used_moves)
        else:
            os.system("cls || clear")
            print('Player 2')
            player_move(possible_moves, used_moves)    

def player_move(possible_moves,used_moves):
    print_table(mark(used_moves))
    move = get_move(possible_moves)
    return possible_moves.remove(move), used_moves.append(move)
    
   
def AI_easy(possible_moves,used_moves):
    os.system("cls || clear")
    print_table(mark(used_moves))
    move = random.choice(possible_moves)
    return possible_moves.remove(move), used_moves.append(move)


def AI_medium(possible_moves, used_moves):
    win_moves = [['A1','A2','A3'], ['B1','B2','B3'], ['C1','C2','C3'], ['A1','B1','C1'], ['A2','B2','C2'], ['A3','B3','C3'], ['A1','B2','C3'],['A3','B2','C1']]
    os.system("cls || clear")
    print_table(mark(used_moves))
    for i in win_moves:
        for j in used_moves:
            if j in i:
                i.remove(j)
    for i in win_moves:
        if len(i) == 1:
            return possible_moves.remove(i[0]), used_moves.append(i[0])
    move = random.choice(possible_moves)
    return possible_moves.remove(move), used_moves.append(move)
    

def menu():
    os.system("cls || clear")
    print("Welcome to Tic Tac Toe game!")
    print("1 - Player vs Player \n2 - Player vs AI")
    flag = True
    while flag:
        user_input = input('Choose game mode:')
        if user_input == '2':
            flag_2 = True
            while flag_2:
                os.system("cls || clear")
                user_input_2 = input("Choose difficulty level:\n1 - Easy\n2 - Medium\n")
                if user_input_2 == '1':
                    game_mode = 'AI_easy'
                    return game_mode 
                if user_input_2 == '2':
                    game_mode = 'AI_medium'
                    return game_mode 
                else:
                    print("Enter valid number!")
        if user_input == '1':
            return game_mode
        else:
            print("Enter valid number!")


def play_again():
    user_input=input("Play again? Y/N: ").upper()
    if user_input == "Y":
        return tictactoe_game(menu())
    else:
        print("Bye!")


                
   
tictactoe_game(menu())
    





