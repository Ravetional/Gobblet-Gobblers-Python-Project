from Project_Exceptions import OutOfPawnsError
from Project_Exceptions import CannotMovePawnError, WrongFieldError
from Project_Exceptions import HigherOrTheSameRankError
from Project_Exceptions import CoveringYourOwnPawnError
from Project_Exceptions import TakingOpponentPawnError
from Project_Exceptions import ChosingEmptyFieldError
from Project_CheckWinner import check_records, check_columns, check_diagonals
from random import choice
from Project_HelpingGamemodesFunctions import pvp_print_game_state
from Project_HelpingGamemodesFunctions import pve_print_game_state
from Project_HelpingGamemodesFunctions import player_chosen_field
from Project_HelpingGamemodesFunctions import player_chosen_pawn
from Project_HelpingGamemodesFunctions import clear


def pvp_round1(total_player_moves,
               plr1,
               plr2,
               game_board,
               board_size,
               fields_numbers,
               cannot_move_pawn):
    '''
    Function 'pvp_round1' services first round in pvp mode.
    :param game_board: gameboard
    :type game_board: dict
    :param field_numbers: assignment coordinates for each field marked as
        number
    :type field_numbers: dict
    :param board_size: length of side of the square gameboard
    :type board_size: int
    :param cannot_move_pawn: communicate telling that player tries to cover a
        pawn with the same or higher rank
    :type cannot_move_pawn: str
    :param total_player_moves: the overall number of moves done by both players
    :type total_players_moves: int
    :param prl1: player1 object
    :type prl1: class Player
    :param prl2: player2 object
    :type prl2: class Player
    '''
    while True:

        # Creating proper communicates:
        plr_field_choice = ', choose field:'
        plr_pawn_choice = ', choose pawn:'

        if total_player_moves % 2 == 1:
            plr_field_choice = f'Player 1{plr_field_choice}'
            plr_pawn_choice = f'Player 1{plr_pawn_choice}'
            plr = plr1
        else:
            plr_field_choice = f'Player 2{plr_field_choice}'
            plr_pawn_choice = f'Player 2{plr_pawn_choice}'
            plr = plr2

        # Inputing data:
        plr_chosen_field = player_chosen_field(
            game_board, plr_field_choice)
        plr_chosen_pawn = player_chosen_pawn(plr, plr_pawn_choice)

        # Moving pawn action:
        try:
            plr.move_pawn_from_list(
                plr_chosen_field, plr_chosen_pawn)
            clear()
            plr._field = game_board
            pvp_print_game_state(
                board_size, game_board, fields_numbers, plr1, plr2)
            total_player_moves += 1
            break

        except HigherOrTheSameRankError:
            print(cannot_move_pawn)


def pvp_next_rounds(total_player_moves,
                    plr1,
                    plr2,
                    game_board,
                    board_size,
                    fields_numbers,
                    cannot_move_pawn,
                    round_number):
    '''
    Function 'pvp_next_rounds' services other rounds in pvp mode.
    :param game_board: gameboard
    :type game_board: dict
    :param field_numbers: assignment coordinates for each field marked as
        number
    :type field_numbers: dict
    :param board_size: length of side of the square gameboard
    :type board_size: int
    :param cannot_move_pawn: communicate telling that player tries to cover a
        pawn with the same or higher rank
    :type cannot_move_pawn: str
    :param total_player_moves: the overall number of moves done by both players
    :type total_players_moves: int
    :param prl1: player1 object
    :type prl1: class Player
    :param prl2: player2 object
    :type prl2: class Player
    '''
    while True:

        # Adding proper communicates for proper player:
        plr_field_choice = ', choose field:'
        plr_pawn_choice = ', choose pawn:'
        move_pawn_from_list_or_field = (
            ', put pawn from list[L] or move one from field[F]: ')
        move_pawn_from = (
            ', choose field where you want to move pawn from: ')
        move_pawn_to = (
            ', choose field where you want to move pawn to: ')

        # Configurating proper communicates:
        if total_player_moves % 2 == 1:
            plr_field_choice = f'Player 1{plr_field_choice}'
            plr_pawn_choice = f'Player 1{plr_pawn_choice}'
            move_pawn_from_list_or_field = (
                f'Player 1{move_pawn_from_list_or_field}')
            move_pawn_from = f'Player 1{move_pawn_from}'
            move_pawn_to = f'Player 1{move_pawn_to}'
            plr = plr1

        else:
            plr_field_choice = f'Player 2{plr_field_choice}'
            plr_pawn_choice = f'Player 2{plr_pawn_choice}'
            move_pawn_from_list_or_field = (
                f'Player 2{move_pawn_from_list_or_field}')
            move_pawn_from = f'Player 2{move_pawn_from}'
            move_pawn_to = f'Player 2{move_pawn_to}'
            plr = plr2

        # Choosing move type:
        list_of_field = input(move_pawn_from_list_or_field)

        if list_of_field == 'l' or list_of_field == 'L':
            break
        elif list_of_field == 'f' or list_of_field == 'F':
            break
        else:
            print('Wrong input!')

    while True:

        # Action when move type is list:
        if list_of_field == 'l' or list_of_field == 'L':

            plr_chosen_field = player_chosen_field(
                game_board, plr_field_choice)
            plr_chosen_pawn = player_chosen_pawn(plr, plr_pawn_choice)

            try:
                plr.move_pawn_from_list(
                    plr_chosen_field, plr_chosen_pawn)
                clear()
                plr._field = game_board
                pvp_print_game_state(
                    board_size, game_board, fields_numbers, plr1, plr2)
                total_player_moves += 1
                win_record = check_records(board_size, game_board)
                win_column = check_columns(board_size, game_board)
                win_diagonal = check_diagonals(board_size, game_board)
                break

            except HigherOrTheSameRankError:
                print(cannot_move_pawn)
            except CoveringYourOwnPawnError:
                print('Cannot cover your own pawn!')
            except OutOfPawnsError:
                list_of_field = 'f'
                break

        # Action when move type is field:
        elif list_of_field == 'f' or list_of_field == 'F':
            first_coordinate = input(move_pawn_from)
            second_coordinate = input(move_pawn_to)

            try:
                plr.move_pawn_to_other_field(
                    first_coordinate, second_coordinate)
                clear()
                plr._field = game_board
                pvp_print_game_state(
                    board_size, game_board, fields_numbers, plr1, plr2)
                total_player_moves += 1
                win_record = check_records(board_size, game_board)
                win_column = check_columns(board_size, game_board)
                win_diagonal = check_diagonals(board_size, game_board)
                break

            except HigherOrTheSameRankError:
                print(cannot_move_pawn)
            except CoveringYourOwnPawnError:
                print('Cannot cover your own pawn!')
            except ChosingEmptyFieldError:
                print('First chosen field is empty!')
            except TakingOpponentPawnError:
                print('You cannot take opponent pawn!')
            except WrongFieldError:
                print('Wrong field!')

    # Increasing round indicator:
    round_number += 1

    # Checking if there is a winner:
    if win_record is not None:
        clear()
        print(f'The winning symbol is: {win_record}')
        return win_record

    elif win_column is not None:
        clear()
        print(f'The winning symbol is: {win_column}')
        return win_column

    elif win_diagonal is not None:
        clear()
        print(f'The winning symbol is: {win_diagonal}')
        return win_diagonal


def pve_round1(game_board,
               plr, comp,
               total_player_moves,
               cannot_move_pawn,
               board_size,
               fields_numbers):

    '''
    Function 'pve_round1' services first round in pve mode.
    :param prl: player object
    :type prl: class Player
    :param comp: computer object
    :type comp: class Computer
    :param board_size: length of side of the square gameboard
    :type board_size: int
    :param game_board: gameboard
    :type game_board: dict
    :param field_numbers: assignment coordinates for each field marked as
        number
    :type field_numbers: dict
    :param total_player_moves: the overall number of moves done by both players
    :type total_players_moves: int
    :param cannot_move_pawn: communicate telling that player tries to cover a
        pawn with the same or higher rank
    :type cannot_move_pawn: str
    '''

    # Player's move
    while True:

        plr_field_choice = 'Player, choose field:'
        plr_pawn_choice = 'Player, choose pawn:'

        plr_chosen_field = player_chosen_field(
            game_board, plr_field_choice)
        plr_chosen_pawn = player_chosen_pawn(plr, plr_pawn_choice)

        try:
            plr.move_pawn_from_list(
                plr_chosen_field, plr_chosen_pawn)
            total_player_moves += 1
            break

        except HigherOrTheSameRankError:
            print(cannot_move_pawn)

    # Computer's move
    while True:
        try:
            comp.move_pawn_from_list()
            total_player_moves += 1
            break
        except CannotMovePawnError:
            continue

    # Displaying game board:
    clear()
    plr._field = game_board
    comp._field = game_board
    pve_print_game_state(board_size, game_board, fields_numbers, plr, comp)


def pve_next_rounds(plr,
                    game_board,
                    board_size,
                    fields_numbers,
                    total_player_moves,
                    cannot_move_pawn,
                    round_number,
                    comp):
    '''
    Function 'pve_next_rounds' services other rounds in pve mode.
    :param prl: player object
    :type prl: class Player
    :param comp: computer object
    :type comp: class Computer
    :param board_size: length of side of the square gameboard
    :type board_size: int
    :param game_board: gameboard
    :type game_board: dict
    :param field_numbers: assignment coordinates for each field marked as
        number
    :type field_numbers: dict
    :param total_player_moves: the overall number of moves done by both players
    :type total_players_moves: int
    :param cannot_move_pawn: communicate telling that player tries to cover a
        pawn with the same or higher rank
    :type cannot_move_pawn: str
    :param round_number: indicates round's number
    :type round_number: int
    '''
    # Next rounds:
    while True:

        # Creating proper communicates:
        plr_field_choice = 'Player, choose field:'
        plr_pawn_choice = 'Player, choose pawn:'
        move_pawn_from_list_or_field = (
            'Player, put pawn from list[L] or move one from field[F]:')
        move_pawn_from = (
            'Player, choose field where you want to move pawn from: ')
        move_pawn_to = (
            'Player, choose field where you want to move pawn to: ')

        list_of_field = input(move_pawn_from_list_or_field)
        if list_of_field == 'l' or list_of_field == 'L':
            break
        elif list_of_field == 'f' or list_of_field == 'F':
            break
        else:
            print('Wrong input!')

    # Player's move:
    while True:

        if plr._pawns == []:
            list_of_field = 'f'

        if list_of_field == 'l' or list_of_field == 'L':

            plr_chosen_field = player_chosen_field(
                game_board, plr_field_choice)
            plr_chosen_pawn = player_chosen_pawn(plr, plr_pawn_choice)

            try:
                plr.move_pawn_from_list(
                    plr_chosen_field, plr_chosen_pawn)
                total_player_moves += 1
                win_record = check_records(board_size, game_board)
                win_column = check_columns(board_size, game_board)
                win_diagonal = check_diagonals(board_size, game_board)
                break

            except HigherOrTheSameRankError:
                print(cannot_move_pawn)
            except CoveringYourOwnPawnError:
                print('Cannot cover your own pawn!')
            except OutOfPawnsError:
                list_of_field = 'f'
                break

        elif list_of_field == 'f' or list_of_field == 'F':
            first_coordinate = input(move_pawn_from)
            second_coordinate = input(move_pawn_to)

            try:
                plr.move_pawn_to_other_field(
                    first_coordinate, second_coordinate)
                clear()
                total_player_moves += 1
                win_record = check_records(board_size, game_board)
                win_column = check_columns(board_size, game_board)
                win_diagonal = check_diagonals(board_size, game_board)
                break

            except HigherOrTheSameRankError:
                print(cannot_move_pawn)
            except CoveringYourOwnPawnError:
                print('Cannot cover your own pawn!')
            except ChosingEmptyFieldError:
                print('First chosen field is empty!')
            except TakingOpponentPawnError:
                print('You cannot take opponent pawn!')
            except WrongFieldError:
                print('Wrong field!')

    plr._field = game_board
    comp._field = game_board
    pve_print_game_state(board_size, game_board, fields_numbers, plr, comp)

    if win_record is not None:
        clear()
        print(f'The winning symbol is: {win_record}')
        return win_record

    elif win_column is not None:
        clear()
        print(f'The winning symbol is: {win_column}')
        return win_column

    elif win_diagonal is not None:
        clear()
        print(f'The winning symbol is: {win_diagonal}')
        return win_diagonal

    # Computers move:
    while True:
        exception = False
        computer_moving_pawn_mode = choice(['l', 'f'])
        if computer_moving_pawn_mode == 'l':
            while True:
                try:
                    comp.move_pawn_from_list()
                    clear()
                    plr._field = game_board
                    pve_print_game_state(
                        board_size, game_board, fields_numbers, plr, comp)
                    total_player_moves += 1
                    win_record = check_records(board_size, game_board)
                    win_column = check_columns(board_size, game_board)
                    win_diagonal = check_diagonals(board_size, game_board)
                    break
                except CannotMovePawnError:
                    exception = True
                    break

        elif computer_moving_pawn_mode == 'f':
            while True:
                try:
                    comp.move_pawn_to_other_field()
                    clear()
                    plr._field = game_board
                    pve_print_game_state(
                        board_size, game_board, fields_numbers, plr, comp)
                    total_player_moves += 1
                    win_record = check_records(board_size, game_board)
                    win_column = check_columns(board_size, game_board)
                    win_diagonal = check_diagonals(board_size, game_board)
                    exception = False
                    break
                except CannotMovePawnError:
                    exception = True
                    continue
        if exception is True:
            continue
        else:
            break

    # Displaying game board:
    clear()
    plr._field = game_board
    comp._field = game_board
    pve_print_game_state(board_size, game_board, fields_numbers, plr, comp)
    round_number += 1

    # Checking if there is a winner.
    if win_record is not None:
        clear()
        print(f'The winning symbol is: {win_record}')
        return win_record

    elif win_column is not None:
        clear()
        print(f'The winning symbol is: {win_column}')
        return win_column

    elif win_diagonal is not None:
        clear()
        print(f'The winning symbol is: {win_diagonal}')
        return win_diagonal
