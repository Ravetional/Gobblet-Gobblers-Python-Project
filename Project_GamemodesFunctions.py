from Project_Classes import Player, Computer
from Project_HelpingGamemodesFunctions import pvp_print_game_state
from Project_HelpingGamemodesFunctions import pve_print_game_state
from Project_GamemodeRounds import pvp_next_rounds, pvp_round1
from Project_GamemodeRounds import pve_round1, pve_next_rounds


def pvp(game_board,
        fields_numbers,
        board_size,
        round_number,
        cannot_move_pawn,
        plr1_symbol,
        total_player_moves,
        move_pawn_from_list_or_field,
        move_pawn_from, move_pawn_to):

    '''
    Function 'pvp' services gameplay between two players.
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
    :param plr1_symbol: chosen symbol by player1
    :type plr1_symbol: str
    :param total_player_moves: the overall number of moves done by both players
    :type total_players_moves: int
    :param move_pawn_from_list_or_field: chosen option of move type
    :type move_pawn_from_list_or_field: str
    :param move_pawn_from: field where player wants to move pawn from
    :type move_pawn_from: str
    :param move_pawn_to: field where player wants to move pawn to
    :type move_pawn_to: str
    '''

    # Giving players proper symbols:
    if plr1_symbol == 'x' or plr1_symbol == 'X':
        plr1 = Player('x', 2 * board_size)
        plr2 = Player('o', 2 * board_size)

    elif plr1_symbol == 'o' or plr1_symbol == 'O':
        plr1 = Player('o', 2 * board_size)
        plr2 = Player('x', 2 * board_size)

    # Displaying game board and lists of pawns:
    plr1._field = game_board
    plr2._field = game_board
    plr1.make_list_of_pawns()
    plr2.make_list_of_pawns()
    pvp_print_game_state(board_size, game_board, fields_numbers, plr1, plr2)

    # First round without possibility to move pawn from field to field.
    while round_number == 1:
        pvp_round1(total_player_moves,
                   plr1, plr2,
                   game_board,
                   board_size,
                   fields_numbers,
                   cannot_move_pawn)
        total_player_moves += 1
        # Modyfing game data:
        if total_player_moves >= 3:
            round_number += 1

    # Next rounds:
    while round_number > 1:
        winner = pvp_next_rounds(total_player_moves,
                                 plr1, plr2,
                                 game_board,
                                 board_size,
                                 fields_numbers,
                                 cannot_move_pawn,
                                 round_number)
        total_player_moves += 1
        round_number += 1
        if winner is not None:
            return winner

###############################################################################
###############################################################################


def pve(plr1_symbol,
        board_size, game_board,
        fields_numbers, round_number,
        total_player_moves, cannot_move_pawn,
        move_pawn_from_list_or_field,
        move_pawn_from, move_pawn_to,
        plr_field_choice, plr_pawn_choice):

    '''
    Function 'pve' services gameplay beetween player and computer.
    :param plr1_symbol: chosen symbol by player1
    :type plr1_symbol: str
    :param board_size: length of side of the square gameboard
    :type board_size: int
    :param game_board: gameboard
    :type game_board: dict
    :param field_numbers: assignment coordinates for each field marked as
        number
    :type field_numbers: dict
    :param round_number: number of finished rounds
    :type round_number: int
    :param total_player_moves: the overall number of moves done by both players
    :type total_players_moves: int
    :param cannot_move_pawn: communicate telling that player tries to cover a
        pawn with the same or higher rank
    :type cannot_move_pawn: str
    :param move_pawn_from_list_or_field: chosen option of move type
    :type move_pawn_from_list_or_field: str
    :param move_pawn_from: field where player wants to move pawn from
    :type move_pawn_from: str
    :param move_pawn_to: field where player wants to move pawn to
    :type move_pawn_to: str
    :param plr_field_choice: chosen field where player wants to put pawn from
        list
    :type plr_field_choice: str
    :param plr_pawn_choice: chosen pawn from list
    :type plr_pawn_choice: str
    '''

    # Giving proper symbols:
    if plr1_symbol == 'x' or plr1_symbol == 'X':
        plr = Player('x', 2 * board_size)
        comp = Computer('o', 2 * board_size)

    elif plr1_symbol == 'o' or plr1_symbol == 'O':
        plr = Player('o', 2 * board_size)
        comp = Computer('x', 2 * board_size)

    # Displaying game board:
    plr._field = game_board
    comp._field = game_board
    plr.make_list_of_pawns()
    comp.make_list_of_pawns()
    pve_print_game_state(board_size, game_board, fields_numbers, plr, comp)

    # First round without possibility to move pawn from field to field:
    while round_number == 1:
        pve_round1(game_board,
                   plr, comp,
                   total_player_moves,
                   cannot_move_pawn,
                   board_size,
                   fields_numbers)
        total_player_moves += 2
        # Modyfing data:
        if total_player_moves >= 3:
            round_number += 1

    while round_number > 1:
        winner = pve_next_rounds(plr,
                                 game_board,
                                 board_size,
                                 fields_numbers,
                                 total_player_moves,
                                 cannot_move_pawn, round_number, comp)
        total_player_moves += 2
        round_number += 1
        if winner is not None:
            return winner
