from random import choice, sample
from Project_Exceptions import OutOfPawnsError, WrongLengthError
from Project_Exceptions import CannotMovePawnError, WrongFieldError
from Project_Exceptions import HigherOrTheSameRankError
from Project_Exceptions import CoveringYourOwnPawnError
from Project_Exceptions import TakingOpponentPawnError
from Project_Exceptions import ChosingEmptyFieldError

###############################################################################
###############################################################################


class GenerateField():

    '''
    Class GenerateField. Contains attributes:
    :param name: length of the square field
    :type length: int
    '''

    def __init__(self, length=3):
        if length < 3 or length > 26:
            raise WrongLengthError()
        self._length = length

    def get_length(self):
        return self._length

    def generate_field(self):

        '''
        Method 'generate_field' creates dictionary where:
            -keys are proper co-ordinates, for example (A1, A2, B1, B2, ...),
            -values are empty lists that are able to store pawns.
        '''

        field = {}

        for horizontal_coordinate in range(ord("A"), ord(
                chr(65 + self._length))):

            for vertical_coordinate in range(1, self._length + 1):
                field[
                    f"{chr(horizontal_coordinate)}{vertical_coordinate}"] = []

        return field

    def give_coordinates_number(self):

        '''
        Method 'give_coordinates_number' helps displaying field function to
        organize how it is presented.
        '''

        field = {}
        position_number = 0

        for vertical_coordinate in range(1, self._length + 1):
            for horizontal_coordinate in range(
                    ord("A"), ord(chr(65 + self._length))):
                position_number += 1
                field[position_number] = (
                    f'{chr(horizontal_coordinate)}{vertical_coordinate}')

        return field

###############################################################################
###############################################################################


class Player():

    '''
    Class Player. Contains attributes:
    :param symbol: player's symbol
    :type symbol: str
    :param number_of_pawns: player's number of pawns
    :type number_of_pawns: int
    '''

    def __init__(self, symbol=None, number_of_pawns=None):
        self._symbol = symbol
        self._number_of_pawns = number_of_pawns
        self._pawns = []
        self._field = {}

    def get_symbol(self):
        return self._symbol

    def get_number_of_pawns(self):
        return self._number_of_pawns

    def make_list_of_pawns(self):

        '''
        Function 'make_list_of_pawns' creates list of pawns for player.
        Then player can use this created pawns in game.
        '''

        pawns = []

        for pawn_rank in range(1, self._number_of_pawns // 2 + 1):
            for i in range(2):
                pawns.append(f'{pawn_rank}{self._symbol}')

        self._pawns = pawns

        return pawns

    def get_pawns(self):
        return self._pawns

    def move_pawn_from_list(self, coordinate, pawn):

        '''
        Function 'move_pawn_from_list':
            -takes pawn chosen by player,
            -takes co-ordinate chosen by player,
            -checks if player can move this pawn or on certain field,
            -if player can move, function moves proper pawn to chosen field
                and then removes this pawn from list of available ones.
        :param coordinate: chosen coordinate as destination by player
        :type coordinate: str
        :param pawn: chosen pawn by player
        :type pawn: str
        '''

        piece = self._field[coordinate]

        # This condition checks if list is empty.
        if self._pawns == []:
            raise OutOfPawnsError()

        # This condition checks if pawn destination field is not empty.
        if len(piece) != 0:

            # This condition checks if lying pawn has the same symbol as...
            # your chosen one.
            if piece[-1][-1] == pawn[-1]:
                raise CoveringYourOwnPawnError()

            # This condition checks if pawn, which lies on destination...,
            # has higher rank than your pawn or the same rank as yours.
            elif int(piece[-1][:-1]) >= int(pawn[:-1]):
                raise HigherOrTheSameRankError()

            else:
                piece.append(pawn)
                self._pawns.remove(pawn)

        else:
            piece.append(pawn)
            self._pawns.remove(pawn)
        return self._field

    def move_pawn_to_other_field(self, first_coordinate, second_coordinate):

        '''
        Function 'move_pawn_to_other_field' gives possibility to move pawn that
        is already on game board to other game board's field.
        :param first_coordinate: field where, player wants to move pawn from
        :type first_coordinate: str
        :param second_coordinate: field where, player wants to move pawn to
        :type second_coordinate: str
        '''

        # This condition checks if the given field exists.
        if first_coordinate not in self._field.keys():
            raise WrongFieldError()
        if second_coordinate not in self._field.keys():
            raise WrongFieldError()

        # This condition checks if the field where, you want to move pawn...
        # from, is empty.
        if self._field[first_coordinate] == []:
            raise ChosingEmptyFieldError()

        # This condition checks if on the field, where you want to move pawn...
        # from, lies your own pawn.
        if self._field[first_coordinate][-1][-1] == self._symbol:
            pawn_to_move = self._field[first_coordinate][-1]
            self._field[first_coordinate].remove(pawn_to_move)

            # This condition checks if the field, where yout want to move...
            # pawn to, is empty.
            if len(self._field[second_coordinate]) == 0:
                self._field[second_coordinate].append(pawn_to_move)

            # This condition checks if on the field, where you want to move...
            # pawn to, lies pawn with lower rank than yours.
            elif pawn_to_move[:-1] > self._field[second_coordinate][-1][:-1]:

                # This condition checks if on the second field lies your pawn.
                if pawn_to_move[-1] == self._field[second_coordinate][-1][-1]:
                    self._field[first_coordinate].append(pawn_to_move)
                    raise CoveringYourOwnPawnError()

                else:
                    self._field[second_coordinate].append(pawn_to_move)

            else:
                self._field[first_coordinate].append(pawn_to_move)
                if pawn_to_move[-1] == self._field[second_coordinate][-1][-1]:
                    raise CoveringYourOwnPawnError
                else:
                    raise HigherOrTheSameRankError()

        else:
            raise TakingOpponentPawnError()

###############################################################################
###############################################################################


class Computer(Player):

    '''
    Class Computer - subclass of class Player.
    Contains attributes:
    :param symbol: computer's symbol
    :type symbol: str
    :param number_of_pawns: computer's number of pawns
    :type number_of_pawns: int
    '''

    def __init__(self, symbol=None, number_of_pawns=None):
        super().__init__(symbol, number_of_pawns)
        self._symbol = symbol
        self._number_of_pawns = number_of_pawns
        self._pawns = []
        self._field = {}

    def move_pawn_from_list(self):

        '''
        Method 'move_pawn_from_list' for computer works almost the same
        as player's method with the same name, but computer choses randomly
        pawn from list and randomly destination field.
        '''

        # This condition checks if list is empty.
        if self._pawns == []:
            raise OutOfPawnsError()

        else:
            pawn_to_move = choice(self._pawns)

        chosen_field = sample(list(self._field.keys()), 1)[0]

        # This condition checks if the field, which computer wants to move...
        # pawn from, is empty.
        if self._field[chosen_field] == []:
            self._field[chosen_field].append(pawn_to_move)
            self._pawns.remove(pawn_to_move)

        else:

            # This condition checks if on the field, where computer wants to...
            # move, is its own pawn.
            if self._field[chosen_field][-1][-1] == pawn_to_move[-1]:
                raise CannotMovePawnError()

            # This condition checks if on the field, where computer wants to...
            # move, lies opponent's pawn with higher or the same rank.
            if self._field[chosen_field][-1][:-1] >= pawn_to_move[:-1]:
                raise CannotMovePawnError()

            else:
                self._field[chosen_field].append(pawn_to_move)
                self._pawns.remove(pawn_to_move)

    def move_pawn_to_other_field(self):

        '''
        Method 'move_pawn_to_other_field' works similarly as the player's one
        but in this method computer randomly chooses both fields (field 'from'
        and field 'to') to move its pawn.
        '''

        fields = list(self._field.keys())
        chosen_first_field = choice(fields)
        fields.remove(chosen_first_field)
        chosen_second_field = sample(fields, 1)[0]

        # This condition checks if field, where computer wants to...
        # move pawn from, is empty.
        if self._field[chosen_first_field] == []:
            raise CannotMovePawnError()

        else:
            pawn_to_move = self._field[chosen_first_field][-1]

            # This condition checks if on the field, where computer...
            # wants to move pawn from, lies its pawn or not.
            if pawn_to_move[-1] != self._symbol:
                raise CannotMovePawnError()

            # This condition checks if the field, where computer...
            # wants to move pawn to, is empty.
            if self._field[chosen_second_field] == []:
                self._field[chosen_second_field].append(pawn_to_move)
                self._field[chosen_first_field].remove(pawn_to_move)

            # This condition checks if the field, where computer...
            # wants to move pawn to, lies opponet's pawn with higher...
            # or the same rank.
            elif self._field[
                    chosen_second_field][-1][:-1] >= pawn_to_move[:-1]:
                raise CannotMovePawnError()

            # This condition checks if the field, where computer...
            # wants to move pawn to, lies its own pawn.
            elif self._field[chosen_second_field][-1][-1] == self._symbol:
                raise CannotMovePawnError()

            else:
                self._field[chosen_second_field].append(pawn_to_move)
                self._field[chosen_first_field].remove(pawn_to_move)
