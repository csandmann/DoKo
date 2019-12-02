from GameEngines.Common.Cards import *
from GameEngines.Common.Player import Player
from GameEngines.Common.Exceptions import CardForbidden, OutOfOrder

class Trick:

    def __init__(self, first_card: BaseCard, player: Player):
        if first_card.is_trump:
            self.trumps_played = True
        else:
            self.trumps_played = False
        self.suit = first_card.suit
        self.players = [player]
        self.cards = [first_card]
        self.is_complete = False
        self.winning_player = None

    def update(self, card, player):
        #simple rule violations
        if self.is_complete:
            raise RuntimeError("This trick is complete. You cannot add any more cards")
        expected_player = (self.players[-1].index + 1) % 4
        if player.index != expected_player:
            raise OutOfOrder(f"It is Player {expected_player}'s turn")
        #forbidden cards
        if self.trumps_played and not card.is_trump:
            if any([card.is_trump for card in player.cards]):
                raise CardForbidden(f"Player {player.index} must play trumps!")
        elif not self.trumps_played and card.is_trump:
            if any(card.suit == self.suit for card in player.cards):
                raise CardForbidden(f"Player {player.index} must play {self.suit}!")
        #everything is fine
        self.players.append(player)
        self.cards.append(card)
        if len(self.cards) == 4:
            self._finish()

    @property
    def value(self):
        return sum([card.value for card in self.cards])

    def __str__(self):
        return f"Trick ({len(self.cards)} cards, {self.value} points)"

    @property
    def info(self):
        cards_str = '\n'.join([str(card) for card in self.cards])
        if len(self.cards) < 4:
            return f"Trick ({len(self.cards)} cards, {self.value} points):\n {cards_str}"
        else:
            return f"Trick (won by {self.winning_player}, {len(self.cards)} cards, {self.value} points):\n {cards_str}"

    def _finish(self):
        self.winning_player = self._determine_winning_player()
        self.is_complete = True

    def _determine_winning_player(self):
        highest_card, winning_player = self.cards[0], self.players[0]
        for card, player in zip(self.cards[1:], self.players[1:]):
            if card == highest_card:
                continue
            if card > highest_card: #order of comparison matters
                highest_card = card
                winning_player = player
        return winning_player
