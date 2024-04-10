class OutOfPawnsError(Exception):
    pass


class WrongLengthError(Exception):
    pass


class CannotMovePawnError(Exception):
    pass


class WrongFieldError(KeyError):
    pass


class HigherOrTheSameRankError(Exception):
    pass


class CoveringYourOwnPawnError(Exception):
    pass


class TakingOpponentPawnError(Exception):
    pass


class ChosingEmptyFieldError(Exception):
    pass
