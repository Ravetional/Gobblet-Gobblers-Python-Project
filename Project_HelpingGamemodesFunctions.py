import os
from Project_DisplayField import display_field


def clear():
    '''
    Function 'clear' clears terminal
    '''
    os.system('clear')


def player_chosen_field(game_board, plr_field_choice):
    '''
    Function 'player_chosen_field' gets field from user's input
    :param game_board: gameboard
    :type game_board: dict
    :param plr_field_choice: chosen field
    :type plr_field_choice: str
    '''
    while True:
        plr_chosen_field = input(plr_field_choice)
        if plr_chosen_field in game_board.keys():
            return plr_chosen_field
        else:
            print('Wrong coordinate!')


def player_chosen_pawn(plr, plr_pawn_choice):
    '''
    Function 'player_chosen_pawn' gets pawn from user's input
    :param game_board: gameboard
    :type game_board: dict
    :param plr_pawn_choice: chosen pawn
    :type plr_pawn_choice: str
    '''
    while True:
        plr_chosen_pawn = input(plr_pawn_choice)
        if plr_chosen_pawn in plr._pawns and len(plr._pawns) != 0:
            return plr_chosen_pawn
        else:
            print(
                'You do not have that pawn as available one!')


def pvp_print_game_state(board_size, game_board, fields_numbers, plr1, plr2):
    '''
    Function 'pvp_print_game_state' shows current game's state in pvp mode
    :param game_board: gameboard
    :type game_board: dict
    :param field_numbers: assignment coordinates for each field marked as
        number
    :type field_numbers: dict
    :param board_size: length of side of the square gameboard
    :type board_size: int
    :param prl1: player1 object
    :type prl1: class Player
    :param prl2: player2 object
    :type prl2: class Player
    '''
    print(display_field(board_size, game_board, fields_numbers))
    print(f'Player 1 pawns:{plr1._pawns}')
    print(f'Player 2 pawns:{plr2._pawns}')


def pve_print_game_state(board_size, game_board, fields_numbers, plr, comp):
    '''
    Function 'pve_print_game_state' shows current game's state in pve mode
    :param game_board: gameboard
    :type game_board: dict
    :param field_numbers: assignment coordinates for each field marked as
        number
    :type field_numbers: dict
    :param board_size: length of side of the square gameboard
    :type board_size: int
    :param prl: player object
    :type prl: class Player
    :param comp: computer object
    :type comp: class Computer
    '''
    print(display_field(board_size, game_board, fields_numbers))
    print(f'Player pawns:{plr._pawns}')
    print(f'Computer pawns:{comp._pawns}')
