# Defining the Tic-Tac-Toe Matrix
  
# Defining the Display
def display(game_board):
    print(game_board[0])
    print(game_board[1])
    print(game_board[2])


#Player choses the position that they want

def user_choice(played):
    
    choice = 'test'
    game_range = range(1,10)
    within_range = False
    
    while (within_range or choice.isdigit()) == False:

    
        choice = input("Please select a posittion (1-9):  ")
        
        # Checking if it is a digit
        if choice.isdigit() == False:
            print('Sorry, that is not an available row.')
            
        # Checking if position has already been taken
        if choice in played:
            print('That position has already been taken. Please select another.')
        
        # Checking if it is in range
        if (choice.isdigit() and (int(choice) in game_range)) == True:
            return choice    
        else:
            print('Sorry, that number is not an integer between 1 and 9')
            within_range = False
    
 # Updates the board with valid player choice

def update_board(choice, character, game_matrix):
    column = (int(choice)%3 -1)
    if int(choice) in [1, 2, 3]:
        game_matrix[0][column] = character
    elif int(choice) in [4, 5, 6]:
        game_matrix[1][column] = character
    else:
        game_matrix[2][column] = character
    return game_matrix   


def win_game_check(player, game_matrix):
    if (game_matrix[0][0] == game_matrix[0][1] == game_matrix[0][2] or #row1
    game_matrix[1][0] == game_matrix[1][1] == game_matrix[1][2] or #row 2
    game_matrix[2][0] == game_matrix[2][1] == game_matrix[2][2] or # row 3
    game_matrix[0][0] == game_matrix[1][0] == game_matrix[2][0] or #column 1
    game_matrix[0][1] == game_matrix[1][1] == game_matrix[2][1] or #column 2
    game_matrix[0][2] == game_matrix[1][2] == game_matrix[2][2] or #column 3
    game_matrix[2][0] == game_matrix[1][1] == game_matrix[0][2] or #forward slash
    game_matrix[0][0] == game_matrix[1][1] == game_matrix[2][2]): #back slash
        print(f'Player {player} has won the game!')
        return True
    else:
        return False


# The tic-tac-toe complete game
def tic_tac_toe():
    user1_char = 'X'
    user2_char = 'O'
    game_matrix = [[1,2,3], [4,5,6], [7,8,9]]
    display(game_matrix)
    played = []
        
    for x in range(1,10):  # Creating a for loop to go through all 9 slections

            
        if x%2 != 0: #player 1 turn
            print('Player 1, it is your turn.')
            choice = user_choice(played)
            played.append(choice)
            game_matrix = update_board(choice, user1_char, game_matrix)
            display(game_matrix)
            win = win_game_check('Player 1', game_matrix)
            
        else: #player 2 turn
            print('Player 2, it is your turn.')
            choice = user_choice(played)
            played.append(choice)
            game_matrix = update_board(choice, user2_char, game_matrix)
            display(game_matrix)
            win = win_game_check('Player 2', game_matrix)
        if win is True:
            break

    return print('It is a TIE!!! Thank you for playing!')


def main():
    tic_tac_toe()
    return 0

if __name__ == '__main__':
    main()