class InvalidMove(Exception):
    pass

class CardForbidden(InvalidMove):
    pass

class OutOfOrder(InvalidMove):
    pass

class CardNotFound(InvalidMove):
    pass