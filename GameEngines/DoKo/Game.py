import random
from GameEngines.DoKo.Cards import Suit, Rank, Card
from GameEngines.Common.Player import Player
from GameEngines.Common.Trick import Trick


class Game:

    def __init__(self, max_players, random_seed=42):
        random.seed(random_seed)
        self.max_players = max_players
        self.players = []
        self.trick = None
        self.active_player = None
        self.prepare_new_game()

    def prepare_new_game(self):
        all_cards = 2*list(Card(rank, suit) for rank in Rank for suit in Suit)
        random.shuffle(all_cards)
        cards_per_player = len(all_cards) // self.max_players
        for player_index in range(self.max_players):
            player_cards = all_cards[player_index*cards_per_player:(player_index+1)*cards_per_player]
            player = Player(player_cards, player_index)
            self.players.append(player)
        self.active_player = random.choice(self.players)

    def play_card(self, card):
        player = self.active_player
        player.remove(card)
        if self.trick is None or self.trick.is_complete:
            self.trick = Trick(card, player)
        else:
            self.trick.update(card, player)
        if self.trick.is_complete:
            self.active_player = self.trick.winning_player
            self.active_player.tricks.append(self.trick)
        else:
            active_player_idx = self.players.index(self.active_player)
            self.active_player = self.players[(active_player_idx + 1) % self.max_players]

    @property
    def is_finished(self):
        return all([len(player.cards) == 0 for player in self.players])

def runMinimalExample():
    game = Game(max_players=4)
    #first trick
    game.play_card(Card(Rank.Ace, Suit.Clubs))
    game.play_card(Card(Rank.King, Suit.Clubs))
    game.play_card(Card(Rank.King, Suit.Clubs))
    game.play_card(Card(Rank.Nine, Suit.Clubs))
    print(f"Points: {str(game.active_player.tricks[-1])}")
    #second trick
    game.play_card(Card(Rank.Ace, Suit.Hearts))
    game.play_card(Card(Rank.King, Suit.Hearts))
    game.play_card(Card(Rank.Ace, Suit.Hearts))
    game.play_card(Card(Rank.Nine, Suit.Hearts))
    print(f"Points: {str(game.active_player.tricks[-1])}")
    #third trick
    game.play_card(Card(Rank.Nine, Suit.Diamonds))
    game.play_card(Card(Rank.Queen, Suit.Diamonds))
    game.play_card(Card(Rank.Queen, Suit.Hearts))
    game.play_card(Card(Rank.Queen, Suit.Clubs))
    print(f"Points: {str(game.active_player.tricks[-1])}")


if __name__=='__main__':
    runMinimalExample()