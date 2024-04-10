from Project_Classes import Player, GenerateField, Computer
from unittest.mock import Mock


def test_generate_field_length():
    field = GenerateField(15)
    assert field.get_length() == 15


def test_generate_field():
    field = GenerateField(3)
    assert field.get_length() == 3
    assert field.generate_field() == {
        'A1': [],
        'A2': [],
        'A3': [],
        'B1': [],
        'B2': [],
        'B3': [],
        'C1': [],
        'C2': [],
        'C3': []
    }


def test_generate_field_give_coords_numbers():
    field = GenerateField(3)
    assert field.give_coordinates_number() == {
        1: 'A1',
        2: 'B1',
        3: 'C1',
        4: 'A2',
        5: 'B2',
        6: 'C2',
        7: 'A3',
        8: 'B3',
        9: 'C3',
    }


def test_player_set_symbol_and_pawns_number():
    player = Player('x', 6)
    assert player.get_symbol() == 'x'
    assert player.get_number_of_pawns() == 6


def test_create_available_pawns():
    board_size = 3
    player = Player('o', 2 * board_size)
    assert player.make_list_of_pawns() == ['1o', '1o', '2o', '2o', '3o', '3o']
    assert player._pawns == ['1o', '1o', '2o', '2o', '3o', '3o']
    assert player.get_pawns() == ['1o', '1o', '2o', '2o', '3o', '3o']


def test_moving_pawn():
    field = GenerateField(3)
    assert field.get_length() == 3
    assert field.generate_field() == {
        'A1': [],
        'A2': [],
        'A3': [],
        'B1': [],
        'B2': [],
        'B3': [],
        'C1': [],
        'C2': [],
        'C3': [],
    }
    player = Player('x', 2 * field.get_length())
    assert player._field == {}
    player._field = field.generate_field()
    player.make_list_of_pawns()
    assert player._pawns == ['1x', '1x', '2x', '2x', '3x', '3x']
    player.move_pawn_from_list('B1', '3x')
    assert player._field == {
        'A1': [],
        'A2': [],
        'A3': [],
        'B1': ['3x'],
        'B2': [],
        'B3': [],
        'C1': [],
        'C2': [],
        'C3': [],
    }
    assert player._pawns == ['1x', '1x', '2x', '2x', '3x']


def test_moving_pawn_from_list_to_field_where_lower_rank_pawn_lies():
    field = GenerateField(3)
    assert field.get_length() == 3
    assert field.generate_field() == {
        'A1': [],
        'A2': [],
        'A3': [],
        'B1': [],
        'B2': [],
        'B3': [],
        'C1': [],
        'C2': [],
        'C3': [],
    }
    game_board = field.generate_field()
    player1 = Player('x', 2 * field.get_length())
    player2 = Player('o', 2 * field.get_length())
    player1._field = game_board
    player1.make_list_of_pawns()
    player2._field = game_board
    player2.make_list_of_pawns()
    player2.move_pawn_from_list('B1', '1o')
    assert player2._pawns == ['1o', '2o', '2o', '3o', '3o']
    assert player1._pawns == ['1x', '1x', '2x', '2x', '3x', '3x']
    assert game_board == {
        'A1': [],
        'A2': [],
        'A3': [],
        'B1': ['1o'],
        'B2': [],
        'B3': [],
        'C1': [],
        'C2': [],
        'C3': [],
    }
    player1.move_pawn_from_list('B1', '2x')
    assert game_board == {
        'A1': [],
        'A2': [],
        'A3': [],
        'B1': ['1o', '2x'],
        'B2': [],
        'B3': [],
        'C1': [],
        'C2': [],
        'C3': [],
    }
    assert player1._pawns == ['1x', '1x', '2x', '3x', '3x']
    assert player2._pawns == ['1o', '2o', '2o', '3o', '3o']


def test_moving_pawn_from_field_to_empty_field():
    field = GenerateField(4)
    game_board = field.generate_field()
    player1 = Player('x', 2 * field.get_length())
    player1._field = game_board
    player1.make_list_of_pawns()
    player1.move_pawn_from_list('B1', '1x')
    player1.move_pawn_to_other_field('B1', 'D4')
    assert game_board == {
        'A1': [],
        'A2': [],
        'A3': [],
        'A4': [],
        'B1': [],
        'B2': [],
        'B3': [],
        'B4': [],
        'C1': [],
        'C2': [],
        'C3': [],
        'C4': [],
        'D1': [],
        'D2': [],
        'D3': [],
        'D4': ['1x'],
    }
    assert player1._pawns == ['1x', '2x', '2x', '3x', '3x', '4x', '4x']


def test_moving_pawn_from_field_to_field_where_opponent_has_lower_rank_pawn():
    field = GenerateField(3)
    game_board = field.generate_field()
    player1 = Player('x', 2 * field.get_length())
    player2 = Player('o', 2 * field.get_length())
    player1._field = game_board
    player2._field = game_board
    player1.make_list_of_pawns()
    player2.make_list_of_pawns()
    player1.move_pawn_from_list('A1', '1x')
    player2.move_pawn_from_list('B1', '3o')
    player1.move_pawn_from_list('C1', '2x')
    player2.move_pawn_to_other_field('B1', 'C1')
    player1._field = game_board
    player2._field = game_board
    assert game_board == {
        'A1': ['1x'],
        'A2': [],
        'A3': [],
        'B1': [],
        'B2': [],
        'B3': [],
        'C1': ['2x', '3o'],
        'C2': [],
        'C3': [],
    }
    assert player1._pawns == ['1x', '2x', '3x', '3x']
    assert player2._pawns == ['1o', '1o', '2o', '2o', '3o']


def test_computer_set_symbol_and_pawns_number():
    comp = Computer('o', 6)
    assert comp.get_symbol() == 'o'
    assert comp._number_of_pawns == 6


def test_computer_create_available_pawns():
    board_size = 3
    comp = Computer('o', 2 * board_size)
    assert comp.make_list_of_pawns() == ['1o', '1o', '2o', '2o', '3o', '3o']
    assert comp._pawns == ['1o', '1o', '2o', '2o', '3o', '3o']
    assert comp.get_pawns() == ['1o', '1o', '2o', '2o', '3o', '3o']


def test_computer_moving_pawn(monkeypatch):
    field = GenerateField(3)
    game_board = field.generate_field()
    player = Player('x', 2 * field.get_length())
    comp = Computer('o', 2 * field.get_length())
    player._field = game_board
    comp._field = game_board
    player.make_list_of_pawns()
    comp.make_list_of_pawns()
    player.move_pawn_from_list('A1', '1x')
    chosen_pawn = Mock(return_value='1o')
    chosen_field = Mock(return_value=['B1'])
    monkeypatch.setattr('Project_Classes.choice', chosen_pawn)
    monkeypatch.setattr('Project_Classes.sample', chosen_field)
    comp.move_pawn_from_list()
    assert game_board == {
        'A1': ['1x'],
        'A2': [],
        'A3': [],
        'B1': ['1o'],
        'B2': [],
        'B3': [],
        'C1': [],
        'C2': [],
        'C3': [],
    }


def test_computer_moving_pawn_to_field_where_lower_rank_pawn_lies(monkeypatch):
    field = GenerateField(3)
    game_board = field.generate_field()
    player = Player('x', 2 * field.get_length())
    comp = Computer('o', 2 * field.get_length())
    player._field = game_board
    comp._field = game_board
    player.make_list_of_pawns()
    comp.make_list_of_pawns()
    player.move_pawn_from_list('A1', '1x')
    chosen_pawn = Mock(return_value='2o')
    chosen_field = Mock(return_value=['A1'])
    monkeypatch.setattr('Project_Classes.choice', chosen_pawn)
    monkeypatch.setattr('Project_Classes.sample', chosen_field)
    comp.move_pawn_from_list()
    assert game_board == {
        'A1': ['1x', '2o'],
        'A2': [],
        'A3': [],
        'B1': [],
        'B2': [],
        'B3': [],
        'C1': [],
        'C2': [],
        'C3': [],
    }


def test_computer_moving_pawn_from_field_to_empty_field(monkeypatch):
    field = GenerateField(3)
    game_board = field.generate_field()
    player = Player('x', 2 * field.get_length())
    comp = Computer('o', 2 * field.get_length())
    player._field = game_board
    comp._field = game_board
    player.make_list_of_pawns()
    comp.make_list_of_pawns()
    player.move_pawn_from_list('A1', '1x')
    chosen_pawn = Mock(return_value='1o')
    chosen_field = Mock(return_value=['B1'])
    monkeypatch.setattr('Project_Classes.choice', chosen_pawn)
    monkeypatch.setattr('Project_Classes.sample', chosen_field)
    comp.move_pawn_from_list()
    assert game_board == {
        'A1': ['1x'],
        'A2': [],
        'A3': [],
        'B1': ['1o'],
        'B2': [],
        'B3': [],
        'C1': [],
        'C2': [],
        'C3': [],
    }
    chosen_first_field = Mock(return_value='B1')
    chosen_second_field = Mock(return_value=['A2'])
    monkeypatch.setattr('Project_Classes.choice', chosen_first_field)
    monkeypatch.setattr('Project_Classes.sample', chosen_second_field)
    comp.move_pawn_to_other_field()
    assert game_board == {
        'A1': ['1x'],
        'A2': ['1o'],
        'A3': [],
        'B1': [],
        'B2': [],
        'B3': [],
        'C1': [],
        'C2': [],
        'C3': [],
    }


def test_com_move_pawn_from_field_to_field_where_opponent_lower_pawn_lies(
        monkeypatch):
    field = GenerateField(3)
    game_board = field.generate_field()
    player = Player('x', 2 * field.get_length())
    comp = Computer('o', 2 * field.get_length())
    player._field = game_board
    comp._field = game_board
    player.make_list_of_pawns()
    comp.make_list_of_pawns()
    player.move_pawn_from_list('A1', '1x')
    chosen_pawn = Mock(return_value='3o')
    chosen_field = Mock(return_value=['B1'])
    monkeypatch.setattr('Project_Classes.choice', chosen_pawn)
    monkeypatch.setattr('Project_Classes.sample', chosen_field)
    comp.move_pawn_from_list()
    player.move_pawn_from_list('C1', '2x')
    chosen_first_field = Mock(return_value='B1')
    chosen_second_field = Mock(return_value=['C1'])
    monkeypatch.setattr('Project_Classes.choice', chosen_first_field)
    monkeypatch.setattr('Project_Classes.sample', chosen_second_field)
    comp.move_pawn_to_other_field()
    player._field = game_board
    comp._field = game_board
    assert game_board == {
        'A1': ['1x'],
        'A2': [],
        'A3': [],
        'B1': [],
        'B2': [],
        'B3': [],
        'C1': ['2x', '3o'],
        'C2': [],
        'C3': [],
    }
    assert player._pawns == ['1x', '2x', '3x', '3x']
    assert comp._pawns == ['1o', '1o', '2o', '2o', '3o']
