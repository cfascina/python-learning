from os import system, name
import random

def clear_console():

    # For Windows
    if name == 'nt':
        _ = system('cls')

    # For Linux and MacOS
    elif(name == 'posix'):
        _ = system('clear')

def get_players_markers():

    marker = ''

    while marker not in ['X', 'O']:
        marker = input('Do you want to play with X or O? ').upper()

    if marker == 'X':
        return('X', 'O')
    else:
        return('O', 'X')

def set_start_player():

    initial_player = random.randint(1, 2)

    return initial_player

def show_position(position):

    if not position:
        return ' - '
    else:
        return ' ' + position + ' '

def display_board(board):

    print('-----------')
    print('-- BOARD --')
    print('-----------\n')
    print(show_position(board[7]) + '|' + show_position(board[8]) + '|' + show_position(board[9]))
    print(show_position(board[4]) + '|' + show_position(board[5]) + '|' + show_position(board[6]))
    print(show_position(board[1]) + '|' + show_position(board[2]) + '|' + show_position(board[3]) + '\n')

def set_board_marker(board, current_player, marker):

    # Check if user position is a number
    while True:
        try:
            position = int(input(f'Player {current_player}, choose where you want to place your \'{marker}\' (1-9): '))
            break
        except:
            print('Please, enter only numbers.\n')
            continue

    # Check if user position is a number between 1 and 9
    while position not in range(1, 10):
        position = int(input('P1ease, enter a position between 1 and 9: '))

    # Check if user position is available
    while board[position] != '':
        position = int(input('P1ease, enter a position thas is available: '))

    # Mark position on board
    board[position] = marker

def has_winner(board, mark):

    # Check diagonals
    if(mark == board[1] == board[5] == board[9]):
        return True
    elif(mark == board[3] == board[5] == board[7]):
        return True

    # Check lines and columns
    else:
        for position in [1, 4, 7]:
            if(mark == board[position] == board[position + 1] == board[position + 2]):
                return True
        for position in [1, 2, 3]:
            if(mark == board[position] == board[position + 3] == board[position + 6]):
                return True
        else:
            return False

def play_again():

    answer = ''

    while answer not in ['Y', 'N']:
        answer = input('Do you wan\'t to play again? (Y/N) ').upper()

    clear_console()

    return answer == 'Y'

# Game loop
while True:

    # Welcome and board creation
    print('Welcome to Tic Tac Toe!\n')
    board = [''] * 10

    # Set player's markers (X/O)
    marker_player_01, marker_player_02 = get_players_markers()
    print(f'\nPlayer 1 is using: {marker_player_01}.')
    print(f'Player 2 is using: {marker_player_02}.')

    # Set wich player will start
    current_player = set_start_player()
    print(f'\nPlayer {current_player} goes first.\n')

    # Asks if users are ready to play
    ready_to_play = ''
    while ready_to_play not in ['Y', 'N']:
        ready_to_play = input('Are you ready to play? (Y/N) ').upper()

    # If they are, set 'is_game_on' to True, clear the console and display the board
    # If not, set 'is_game_on' to False and it will call 'play_again()'
    if ready_to_play == 'Y':
        is_game_on = True
        clear_console()
        display_board(board)
    else:
        is_game_on = False

    while is_game_on:

        # Get current player marker (X/0)
        if current_player == 1:
            marker = marker_player_01
        elif current_player == 2:
            marker = marker_player_02

        # Get player position choice, clear the console and display updated board
        position = set_board_marker(board, current_player, marker)
        clear_console()
        display_board(board)

        # If some player won, shows it and finishes the game
        if has_winner(board, marker):
            print(f'Player {str(current_player)} won!\n')
            is_game_on = False
        else:
            # If the game finishes tied, shows it and finishes the game
            if '' not in board[1:]:
                print('The game was tied.\n')
                is_game_on = False

        # Reverses the player's turn
        if current_player == 1:
            current_player = 2
            marker = marker_player_02
        elif current_player == 2:
            current_player = 1
            marker = marker_player_01

    # If 'play_again()' returns False, it breaks the 'while True' loop and finishes the game
    if not play_again():
        break
