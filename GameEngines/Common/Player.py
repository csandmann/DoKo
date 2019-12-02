from GameEngines.Common.Exceptions import CardNotFound

class Player:

    def __init__(self, initial_cards, index):
        self.cards = initial_cards
        self.index = index
        self.tricks = []

    def remove(self, card):
        try:
            self.cards.remove(card)
        except ValueError as e:
            raise CardNotFound(f"I do not have card {str(card)}")
        return card

    def __str__(self):
        return f"Player {self.index}"

    @property
    def info(self):
        return f"Player {self.index} with {len(self.cards)} cards:\n" + "\n".join(str(card) for card in self.cards)