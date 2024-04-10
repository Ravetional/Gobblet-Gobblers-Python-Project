from unittest.mock import Mock
from Project_Exceptions import ChosingEmptyFieldError, CoveringYourOwnPawnError
from Project_Exceptions import WrongLengthError, OutOfPawnsError
from Project_Exceptions import HigherOrTheSameRankError
from Project_Exceptions import TakingOpponentPawnError
from Project_Exceptions import CannotMovePawnError, WrongFieldError
from Project_Classes import Computer, Player, GenerateField
import pytest


def test_generate_field_negative_length():
    with pytest.raises(WrongLengthError):
        GenerateField(-2)


def test_generate_field_zero_length():
    with pytest.raises(WrongLengthError):
        GenerateField(0)


def test_generate_field_with_only_one_piece():
    with pytest.raises(WrongLengthError):
        GenerateField(1)


def test_generate_field_with_only_two_pieces():
    with pytest.raises(WrongLengthError):
        GenerateField(2)


def test_generate_field_with_more_length_than_26():
    with pytest.raises(WrongLengthError):
        GenerateField(27)


def test_moving_pawn_from_list_on_field_where_higher_pawn_lies():
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
    player2.move_pawn_from_list('B1', '3o')
    assert player2._pawns == ['1o', '1o', '2o', '2o', '3o']
    assert player1._pawns == ['1x', '1x', '2x', '2x', '3x', '3x']
    assert game_board == {
        'A1': [],
        'A2': [],
        'A3': [],
        'B1': ['3o'],
        'B2': [],
        'B3': [],
        'C1': [],
        'C2': [],
        'C3': [],
    }
    with pytest.raises(HigherOrTheSameRankError):
        player1.move_pawn_from_list('B1', '2x')
    assert player1._pawns == ['1x', '1x', '2x', '2x', '3x', '3x']


def test_moving_pawn_from_list_on_field_with_your_own_pawn():
    field = GenerateField(3)
    game_board = field.generate_field()
    player2 = Player('o', 2 * field.get_length())
    player2._field = game_board
    player2.make_list_of_pawns()
    player2.move_pawn_from_list('B1', '1o')
    with pytest.raises(CoveringYourOwnPawnError):
        player2.move_pawn_from_list('B1', '3o')
    assert player2._pawns == ['1o', '2o', '2o', '3o', '3o']


def test_moving_pawn_from_list_but_we_are_ran_out_of_pawns():
    field = GenerateField(3)
    game_board = field.generate_field()
    player1 = Player('x', 2 * field.get_length())
    player1._field = game_board
    player1.make_list_of_pawns()
    player1._pawns = []
    with pytest.raises(OutOfPawnsError):
        player1.move_pawn_from_list('C3', '1x')


def test_moving_pawn_from_field_to_field_where_opponent_has_higher_rank_pawn():
    field = GenerateField(3)
    game_board = field.generate_field()
    player1 = Player('x', 2 * field.get_length())
    player2 = Player('o', 2 * field.get_length())
    player1._field = game_board
    player2._field = game_board
    player1.make_list_of_pawns()
    player2.make_list_of_pawns()
    player1.move_pawn_from_list('A1', '1x')
    player2.move_pawn_from_list('B1', '2o')
    player1.move_pawn_from_list('C1', '3x')
    player1._field = game_board
    player2._field = game_board
    assert game_board == {
        'A1': ['1x'],
        'A2': [],
        'A3': [],
        'B1': ['2o'],
        'B2': [],
        'B3': [],
        'C1': ['3x'],
        'C2': [],
        'C3': [],
    }
    assert player1._pawns == ['1x', '2x', '2x', '3x']
    assert player2._pawns == ['1o', '1o', '2o', '3o', '3o']
    with pytest.raises(HigherOrTheSameRankError):
        player2.move_pawn_to_other_field('B1', 'C1')
    assert game_board == {
        'A1': ['1x'],
        'A2': [],
        'A3': [],
        'B1': ['2o'],
        'B2': [],
        'B3': [],
        'C1': ['3x'],
        'C2': [],
        'C3': [],
    }


def test_moving_pawn_from_field_to_field_where_opponent_has_same_rank_pawn():
    field = GenerateField(3)
    game_board = field.generate_field()
    player1 = Player('x', 2 * field.get_length())
    player2 = Player('o', 2 * field.get_length())
    player1._field = game_board
    player2._field = game_board
    player1.make_list_of_pawns()
    player2.make_list_of_pawns()
    player1.move_pawn_from_list('A1', '1x')
    player2.move_pawn_from_list('B1', '2o')
    player1.move_pawn_from_list('C1', '2x')
    player1._field = game_board
    player2._field = game_board
    assert game_board == {
        'A1': ['1x'],
        'A2': [],
        'A3': [],
        'B1': ['2o'],
        'B2': [],
        'B3': [],
        'C1': ['2x'],
        'C2': [],
        'C3': [],
    }
    assert player1._pawns == ['1x', '2x', '3x', '3x']
    assert player2._pawns == ['1o', '1o', '2o', '3o', '3o']
    with pytest.raises(HigherOrTheSameRankError):
        player2.move_pawn_to_other_field('B1', 'C1')
    assert game_board == {
        'A1': ['1x'],
        'A2': [],
        'A3': [],
        'B1': ['2o'],
        'B2': [],
        'B3': [],
        'C1': ['2x'],
        'C2': [],
        'C3': [],
    }


def test_first_chosen_coordinate_is_empty():
    field = GenerateField(3)
    game_board = field.generate_field()
    player1 = Player('x', 2 * field.get_length())
    player2 = Player('o', 2 * field.get_length())
    player1._field = game_board
    player2._field = game_board
    player1.make_list_of_pawns()
    player2.make_list_of_pawns()
    player1.move_pawn_from_list('A1', '1x')
    player2.move_pawn_from_list('B1', '2o')
    player1.move_pawn_from_list('C1', '2x')
    player1._field = game_board
    player2._field = game_board
    assert game_board == {
        'A1': ['1x'],
        'A2': [],
        'A3': [],
        'B1': ['2o'],
        'B2': [],
        'B3': [],
        'C1': ['2x'],
        'C2': [],
        'C3': [],
    }
    with pytest.raises(ChosingEmptyFieldError):
        player2.move_pawn_to_other_field('B2', 'C1')


def test_first_coordinate_has_opponents_pawn():
    field = GenerateField(3)
    game_board = field.generate_field()
    player1 = Player('x', 2 * field.get_length())
    player2 = Player('o', 2 * field.get_length())
    player1._field = game_board
    player2._field = game_board
    player1.make_list_of_pawns()
    player2.make_list_of_pawns()
    player1.move_pawn_from_list('A1', '1x')
    player2.move_pawn_from_list('B1', '2o')
    player1._field = game_board
    player2._field = game_board
    assert game_board == {
        'A1': ['1x'],
        'A2': [],
        'A3': [],
        'B1': ['2o'],
        'B2': [],
        'B3': [],
        'C1': [],
        'C2': [],
        'C3': [],
    }
    with pytest.raises(TakingOpponentPawnError):
        player1.move_pawn_to_other_field('B1', 'C3')


def test_in_moving_from_field_to_field_first_coordinate_is_wrong():
    field = GenerateField(3)
    game_board = field.generate_field()
    player1 = Player('x', 2 * field.get_length())
    player2 = Player('o', 2 * field.get_length())
    player1._field = game_board
    player2._field = game_board
    player1.make_list_of_pawns()
    player2.make_list_of_pawns()
    player1.move_pawn_from_list('A1', '1x')
    player2.move_pawn_from_list('B1', '2o')
    player1._field = game_board
    player2._field = game_board
    assert game_board == {
        'A1': ['1x'],
        'A2': [],
        'A3': [],
        'B1': ['2o'],
        'B2': [],
        'B3': [],
        'C1': [],
        'C2': [],
        'C3': [],
    }
    with pytest.raises(WrongFieldError):
        player1.move_pawn_to_other_field('sdf', 'C3')


def test_in_moving_from_field_to_field_second_coordinate_is_wrong():
    field = GenerateField(3)
    game_board = field.generate_field()
    player1 = Player('x', 2 * field.get_length())
    player2 = Player('o', 2 * field.get_length())
    player1._field = game_board
    player2._field = game_board
    player1.make_list_of_pawns()
    player2.make_list_of_pawns()
    player1.move_pawn_from_list('A1', '1x')
    player2.move_pawn_from_list('B1', '2o')
    player1._field = game_board
    player2._field = game_board
    assert game_board == {
        'A1': ['1x'],
        'A2': [],
        'A3': [],
        'B1': ['2o'],
        'B2': [],
        'B3': [],
        'C1': [],
        'C2': [],
        'C3': [],
    }
    with pytest.raises(WrongFieldError):
        player1.move_pawn_to_other_field('A1', 'aaa')


def test_comp_moving_pawn_from_list_to_field_where_higher_pawn_lies(
        monkeypatch):
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
    player = Player('x', 2 * field.get_length())
    comp = Computer('o', 2 * field.get_length())
    player._field = game_board
    player.make_list_of_pawns()
    comp._field = game_board
    comp.make_list_of_pawns()
    player.move_pawn_from_list('B1', '3x')
    assert player._pawns == ['1x', '1x', '2x', '2x', '3x']
    assert comp._pawns == ['1o', '1o', '2o', '2o', '3o', '3o']
    assert game_board == {
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
    chosen_field = Mock(return_value=['B1'])
    chosen_pawn = Mock(return_value='2o')
    monkeypatch.setattr('Project_Classes.choice', chosen_pawn)
    monkeypatch.setattr('Project_Classes.sample', chosen_field)
    with pytest.raises(CannotMovePawnError):
        comp.move_pawn_from_list()
    assert comp._pawns == ['1o', '1o', '2o', '2o', '3o', '3o']


def test_comp_moving_pawn_from_list_where_on_field_with_your_own_pawn(
        monkeypatch):
    field = GenerateField(3)
    game_board = field.generate_field()
    comp = Computer('o', 2 * field.get_length())
    comp._field = game_board
    comp.make_list_of_pawns()
    chosen_field = Mock(return_value=['B1'])
    chosen_pawn = Mock(return_value='1o')
    monkeypatch.setattr('Project_Classes.choice', chosen_pawn)
    monkeypatch.setattr('Project_Classes.sample', chosen_field)
    comp.move_pawn_from_list()
    chosen_field = Mock(return_value=['B1'])
    chosen_pawn = Mock(return_value='3o')
    monkeypatch.setattr('Project_Classes.choice', chosen_pawn)
    monkeypatch.setattr('Project_Classes.sample', chosen_field)
    with pytest.raises(CannotMovePawnError):
        comp.move_pawn_from_list()
    assert comp._pawns == ['1o', '2o', '2o', '3o', '3o']


def test_comp_moving_pawn_from_list_but_we_are_ran_out_of_pawns(monkeypatch):
    field = GenerateField(3)
    game_board = field.generate_field()
    comp = Computer('x', 2 * field.get_length())
    comp._field = game_board
    comp.make_list_of_pawns()
    comp._pawns = []
    chosen_field = Mock(return_value=['C3'])
    chosen_pawn = Mock(return_value='1x')
    monkeypatch.setattr('Project_Classes.choice', chosen_pawn)
    monkeypatch.setattr('Project_Classes.sample', chosen_field)
    with pytest.raises(OutOfPawnsError):
        comp.move_pawn_from_list()


def test_comp_move_pawn_from_field_to_field_where_opponent_has_higher_pawn(
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
    chosen_field = Mock(return_value=['B1'])
    chosen_pawn = Mock(return_value='2o')
    monkeypatch.setattr('Project_Classes.choice', chosen_pawn)
    monkeypatch.setattr('Project_Classes.sample', chosen_field)
    comp.move_pawn_from_list()
    player.move_pawn_from_list('C1', '3x')
    player._field = game_board
    comp._field = game_board
    assert game_board == {
        'A1': ['1x'],
        'A2': [],
        'A3': [],
        'B1': ['2o'],
        'B2': [],
        'B3': [],
        'C1': ['3x'],
        'C2': [],
        'C3': [],
    }
    assert player._pawns == ['1x', '2x', '2x', '3x']
    assert comp._pawns == ['1o', '1o', '2o', '3o', '3o']
    chosen_first_field = Mock(return_value='B1')
    chosen_second_field = Mock(return_value=['C1'])
    monkeypatch.setattr('Project_Classes.choice', chosen_first_field)
    monkeypatch.setattr('Project_Classes.sample', chosen_second_field)
    with pytest.raises(CannotMovePawnError):
        comp.move_pawn_to_other_field()
    assert game_board == {
        'A1': ['1x'],
        'A2': [],
        'A3': [],
        'B1': ['2o'],
        'B2': [],
        'B3': [],
        'C1': ['3x'],
        'C2': [],
        'C3': [],
    }


def test_comp_move_pawn_from_field_to_field_where_opponent_has_same_rank_pawn(
        monkeypatch):
    field = GenerateField(3)
    game_board = field.generate_field()
    player = Player('x', 2 * field.get_length())
    comp = Computer('o', 2 * field.get_length())
    player._field = game_board
    comp._field = game_board
    player.make_list_of_pawns()
    comp.make_list_of_pawns()
    player.move_pawn_from_list('A1', '2x')
    chosen_field = Mock(return_value=['B1'])
    chosen_pawn = Mock(return_value='2o')
    monkeypatch.setattr('Project_Classes.choice', chosen_pawn)
    monkeypatch.setattr('Project_Classes.sample', chosen_field)
    comp.move_pawn_from_list()
    player.move_pawn_from_list('C1', '3x')
    player._field = game_board
    comp._field = game_board
    assert game_board == {
        'A1': ['2x'],
        'A2': [],
        'A3': [],
        'B1': ['2o'],
        'B2': [],
        'B3': [],
        'C1': ['3x'],
        'C2': [],
        'C3': [],
    }
    assert player._pawns == ['1x', '1x', '2x', '3x']
    assert comp._pawns == ['1o', '1o', '2o', '3o', '3o']
    chosen_first_field = Mock(return_value='B1')
    chosen_second_field = Mock(return_value=['A1'])
    monkeypatch.setattr('Project_Classes.choice', chosen_first_field)
    monkeypatch.setattr('Project_Classes.sample', chosen_second_field)
    with pytest.raises(CannotMovePawnError):
        comp.move_pawn_to_other_field()
    assert game_board == {
        'A1': ['2x'],
        'A2': [],
        'A3': [],
        'B1': ['2o'],
        'B2': [],
        'B3': [],
        'C1': ['3x'],
        'C2': [],
        'C3': [],
    }


def test_comp_first_chosen_coordinate_is_empty(monkeypatch):
    field = GenerateField(3)
    game_board = field.generate_field()
    player = Player('x', 2 * field.get_length())
    comp = Computer('o', 2 * field.get_length())
    player._field = game_board
    comp._field = game_board
    player.make_list_of_pawns()
    comp.make_list_of_pawns()
    player.move_pawn_from_list('A1', '1x')
    chosen_field = Mock(return_value=['B1'])
    chosen_pawn = Mock(return_value='2o')
    monkeypatch.setattr('Project_Classes.choice', chosen_pawn)
    monkeypatch.setattr('Project_Classes.sample', chosen_field)
    comp.move_pawn_from_list()
    player.move_pawn_from_list('C1', '2x')
    player._field = game_board
    comp._field = game_board
    assert game_board == {
        'A1': ['1x'],
        'A2': [],
        'A3': [],
        'B1': ['2o'],
        'B2': [],
        'B3': [],
        'C1': ['2x'],
        'C2': [],
        'C3': [],
    }
    chosen_first_field = Mock(return_value='B2')
    chosen_second_field = Mock(return_value=['C1'])
    monkeypatch.setattr('Project_Classes.choice', chosen_first_field)
    monkeypatch.setattr('Project_Classes.sample', chosen_second_field)
    with pytest.raises(CannotMovePawnError):
        comp.move_pawn_to_other_field()


def test_comp_first_coordinate_has_opponents_pawn(monkeypatch):
    field = GenerateField(3)
    game_board = field.generate_field()
    player = Player('x', 2 * field.get_length())
    comp = Computer('o', 2 * field.get_length())
    player._field = game_board
    comp._field = game_board
    player.make_list_of_pawns()
    comp.make_list_of_pawns()
    player.move_pawn_from_list('A1', '1x')
    chosen_field = Mock(return_value=['B1'])
    chosen_pawn = Mock(return_value='2o')
    monkeypatch.setattr('Project_Classes.choice', chosen_pawn)
    monkeypatch.setattr('Project_Classes.sample', chosen_field)
    comp.move_pawn_from_list()
    player._field = game_board
    comp._field = game_board
    assert game_board == {
        'A1': ['1x'],
        'A2': [],
        'A3': [],
        'B1': ['2o'],
        'B2': [],
        'B3': [],
        'C1': [],
        'C2': [],
        'C3': [],
    }
    chosen_first_field = Mock(return_value='A1')
    chosen_second_field = Mock(return_value=['C3'])
    monkeypatch.setattr('Project_Classes.choice', chosen_first_field)
    monkeypatch.setattr('Project_Classes.sample', chosen_second_field)
    with pytest.raises(CannotMovePawnError):
        comp.move_pawn_to_other_field()
