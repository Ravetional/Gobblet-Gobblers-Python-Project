def display_field(size, game_board, field_numbers):

    '''
    Function 'display_field' displays game board with chosen size and
    proper co-ordinates where players are going to play.
    :param size: size of gameboard
    :type size: int
    :param game_board: gameboard
    :type game_board: dict
    :param field_numbers: assignment coordinates for each field marked as
        number
    :type field_numbers: dict
    '''

    row_coordinates = ' '
    columns_number = 0

    for a in range(65, 65 + size):
        row_coordinates += f'  {chr(a)}   '
        columns_number += 1

    print(f'  {row_coordinates}   ')

    field_number = 1

    for b in range(1, size + 1):

        field_divider = ''

        for c in range(1, size + 1):

            coordinate = field_numbers[field_number]

            if len(game_board[coordinate]) == 0:
                field_divider += '     |'

            else:

                if len(game_board[coordinate][-1]) == 2:
                    field_divider += f' {game_board[coordinate][-1]}  |'

                elif len(game_board[coordinate][-1]) == 3:
                    field_divider += f' {game_board[coordinate][-1]} |'

            field_number += 1

        separator = 6*columns_number*'-'

        print(f'  -{separator}')

        if b >= 10:
            print(f'{b}|{field_divider}')

        else:
            print(f'{b} |{field_divider}')

    print(f'  -{separator}')

    return ''
