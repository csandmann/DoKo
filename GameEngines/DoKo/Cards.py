from ..Common.Cards import *


class NoComparisonPossible(Exception):
    pass


class Card(BaseCard):

    def __init__(self, rank, suit):
        super(Card, self).__init__(rank, suit)

    @property
    def is_trump(self):
        if self.rank in [Rank.Jack, Rank.Queen] or self.suit == Suit.Diamonds or (self.rank == Rank.Ten and self.suit == Suit.Hearts):
            return True
        return False

    def __gt__(self, other):
        if self == other:
            raise NoComparisonPossible("I cannot compare equal cards without knowing which lay first.")
        if self.is_trump and not other.is_trump:
            return True
        elif not self.is_trump and other.is_trump:
            return False
        elif self.is_trump and other.is_trump:
            #ten of hearts
            if self.suit == Suit.Hearts and self.rank == Rank.Ten:
                return True
            elif other.suit == Suit.Hearts and other.rank == Rank.Ten:
                return False
            #queens
            if self.rank == Rank.Queen and other.rank != Rank.Queen:
                return True
            elif self.rank != Rank.Queen and other.rank == Rank.Queen:
                return False
            elif self.rank == Rank.Queen and other.rank == Rank.Queen:
                return self.suit.value > other.suit.value
            #jacks
            if self.rank == Rank.Jack and other.rank != Rank.Jack:
                return True
            elif self.rank != Rank.Jack and other.rank == Rank.Jack:
                return False
            elif self.rank == Rank.Jack and other.rank == Rank.Jack:
                return self.suit.value > other.suit.value
            #neither ten of hearts, queen, jack? must be all diamonds
            return self.value > other.value
        else: #no trump / no trump
            if self.suit != other.suit:
                raise NoComparisonPossible("I cannot compare different suits without knowing which lay first")
            else:
                return self.value > other.value

