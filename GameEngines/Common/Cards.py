from enum import Enum


class Rank(Enum):
    Nine = 0
    Ten = 1
    Jack = 2
    Queen = 3
    King = 4
    Ace = 5


class Suit(Enum):
    Diamonds = 0
    Hearts = 1
    Spades = 2
    Clubs = 3


_rank_values = {Rank.Ace: 11,
                Rank.Ten: 10,
                Rank.King: 4,
                Rank.Queen: 3,
                Rank.Jack: 2 }


class BaseCard:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @property
    def value(self):
        try:
            return _rank_values[self.rank]
        except KeyError:
            return 0

    @property
    def is_trump(self):
        raise NotImplemented

    def __gt__(self, other):
        raise NotImplemented()

    def __lt__(self, other):
        return not self > other

    def __ge__(self, other):
        if self.suit == other.suit and self.rank == other.rank:
            return True
        return self > other

    def __le__(self, other):
        if self.suit == other.suit and self.rank == other.rank:
            return True
        return not self > other

    def __str__(self):
        return f"{self.rank.name} of {self.suit.name}"

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit