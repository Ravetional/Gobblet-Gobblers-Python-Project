from Project_Classes import GenerateField, WrongLengthError
from Project_GamemodesFunctions import pvp, pve
from Project_HelpingGamemodesFunctions import clear


def actual_game():
    '''
    Function actual_game supervise gameplay
    '''

    # Base of displayed comminucates:
    gamemode_choice = (
        '(Player vs Player)[1] or (Player vs Computer)[2] or Leave[Any Key]:')
    board_size_choice = 'How large game board shall be:'
    plr1_symbol_choice = 'Player 1, choose symbol: (x/o):'
    move_pawn_from_list_or_field = (
        ', put pawn from list[L] or move one from field[F]: ')
    cannot_move_pawn = 'You cannot cover pawn with the same or higher rank!'
    move_pawn_from = 'Choose field where you want to move pawn from: '
    move_pawn_to = 'Choose field where you want to move pawn to: '

    # Choosing gamemode option:
    while True:
        computer_or_player = input(gamemode_choice)
        if (computer_or_player == '1') or (computer_or_player == '2'):
            break
        else:
            print('Bye :)')
            return ''

    # Choosing board size:
    while True:
        try:
            board_size = int(input(board_size_choice))
        except ValueError:
            print('Wrong input!')
            continue

        try:
            board = GenerateField(board_size)
            game_board = board.generate_field()
            fields_numbers = board.give_coordinates_number()
            break
        except WrongLengthError:
            if board_size < 3:
                print("Field's length cannot be negative,zero,one or two!")
            elif board_size > 26:
                print('Max available size is 26!')
            continue

    # Choosing symbol for player1:
    while True:
        plr1_symbol = input(plr1_symbol_choice)
        if plr1_symbol == 'x' or plr1_symbol == 'X':
            break
        elif plr1_symbol == 'o' or plr1_symbol == 'O':
            break
        else:
            print('This symbol is not available!')

    # Getting necessary data:
    round_number = 1
    total_player_moves = 1

    plr_field_choice = ', choose field:'
    plr_pawn_choice = ', choose pawn:'

###############################################################################

    # PvP Mode:
    if computer_or_player == '1':
        clear()
        pvp(game_board,
            fields_numbers,
            board_size,
            round_number,
            cannot_move_pawn,
            plr1_symbol,
            total_player_moves,
            move_pawn_from_list_or_field,
            move_pawn_from, move_pawn_to)

###############################################################################

    elif computer_or_player == '2':
        clear()
        pve(plr1_symbol,
            board_size,
            game_board,
            fields_numbers,
            round_number,
            total_player_moves,
            cannot_move_pawn,
            move_pawn_from_list_or_field,
            move_pawn_from, move_pawn_to,
            plr_field_choice,
            plr_pawn_choice)


if __name__ == '__main__':
    clear()
    actual_game()
