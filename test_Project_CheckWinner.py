from Project_CheckWinner import check_columns, check_diagonals, check_records
from Project_Classes import GenerateField


def test_check_working_of_checking_records_where_is_a_winner():
    field = GenerateField(5)
    game_board = field.generate_field()
    game_board['A1'] = ['1x']
    game_board['B1'] = ['1o', '5x']
    game_board['C1'] = ['2o', '3x']
    game_board['D1'] = ['2o', '4x']
    game_board['E1'] = ['1o', '2x']
    winner = check_records(field.get_length(), game_board)
    assert winner == 'x'


def test_check_working_of_checking_column_where_is_a_winner():
    field = GenerateField(3)
    game_board = field.generate_field()
    game_board['B1'] = ['2x', '3o']
    game_board['B2'] = ['1x', '2o']
    game_board['B3'] = ['2x', '3o']
    winner = check_columns(field.get_length(), game_board)
    assert winner == 'o'


def test_check_working_of_checking_diagonals_where_is_a_winner_top_down():
    field = GenerateField(3)
    game_board = field.generate_field()
    game_board['A1'] = ['2x', '3o']
    game_board['B2'] = ['1o', '2x', '3o']
    game_board['C3'] = ['1o']
    winner = check_diagonals(field.get_length(), game_board)
    assert winner == 'o'


def test_check_working_of_checking_diagonals_where_is_a_winner_bottom_up():
    field = GenerateField(4)
    game_board = field.generate_field()
    game_board['D4'] = ['1o', '4x']
    game_board['C3'] = ['3x']
    game_board['B2'] = ['1o', '2x', '3o', '4x']
    game_board['A1'] = ['2o', '3x']
    winner = check_diagonals(field.get_length(), game_board)
    assert winner == 'x'


def test_no_winner():
    field = GenerateField(4)
    game_board = field.generate_field()
    game_board['D4'] = ['1o']
    game_board['C3'] = ['3x']
    game_board['B2'] = ['1o', '2x', '3o', '4x']
    game_board['A1'] = ['2o', '3x']
    winner = check_diagonals(field.get_length(), game_board)
    assert winner is None
