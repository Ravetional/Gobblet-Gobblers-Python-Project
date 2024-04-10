def check_records(size, gameboard):

    '''
    Function 'records_checking' checks records with purpose of
    searching the winner.
    :param size: size of gameboard
    :type size: int
    :param gameboard: gameboard
    :type gameboard: dict
    '''

    for i in range(1, size + 1):

        record_pawns = []

        for j in range(ord("A"), ord("A") + size):

            if gameboard[f'{chr(j)}{i}'] == []:
                record_pawns.append('-')

            else:
                record_pawns.append(gameboard[f'{chr(j)}{i}'][-1][1])

        if len(set(record_pawns)) == 1:

            winner = record_pawns[0]

            if winner == '-':
                continue

            else:
                return winner

        else:
            pass

###############################################################################
###############################################################################


def check_columns(size, gameboard):

    '''
    Function 'colums_checking' checks colums with purpose of
    searching the winner.
    :param size: size of gameboard
    :type size: int
    :param gameboard: gameboard
    :type gameboard: dict
    '''

    for i in range(ord("A"), ord("A") + size):

        columns_pawns = []

        for j in range(1, size + 1):

            if gameboard[f'{chr(i)}{j}'] == []:
                columns_pawns.append('-')

            else:
                columns_pawns.append(gameboard[f'{chr(i)}{j}'][-1][1])

        if len(set(columns_pawns)) == 1:

            winner = columns_pawns[0]

            if winner == '-':
                continue

            else:
                return winner

        else:
            pass

###############################################################################
###############################################################################


def check_diagonals(size, gameboard):

    '''
    Function 'diagonals_checking' checks both diagonals with purpose of
    searching the winner.
    :param size: size of gameboard
    :type size: int
    :param gameboard: gameboard
    :type gameboard: dict
    '''

    # First option (From UP to DOWN)

    diagonals_pawns = []

    for i in range(1, size + 1):

        if gameboard[f'{chr(65 + i - 1)}{i}'] == []:
            diagonals_pawns.append('-')

        else:
            diagonals_pawns.append(gameboard[f'{chr(65 + i - 1)}{i}'][-1][1])

    if len(set(diagonals_pawns)) == 1:

        winner = diagonals_pawns[0]

        if winner == '-':
            winner = None

        else:
            return winner

    # Second option (From DOWN to UP)

    diagonals_pawns = []

    for i in range(1, size + 1):

        if gameboard[f'{chr(65 + i - 1)}{size + 1 - i}'] == []:
            diagonals_pawns.append('-')

        else:
            diagonals_pawns.append(
                gameboard[f'{chr(65 + i - 1)}{size + 1 - i}'][-1][1])

    if len(set(diagonals_pawns)) == 1:

        winner = diagonals_pawns[0]

        if winner == '-':
            winner = None

        else:
            return winner
