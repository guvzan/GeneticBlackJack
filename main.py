import random as r

class DeckOfCards:
    """works"""
    def __init__(self):
        self.deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K',
                     'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K',
                     'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K',
                     'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K',]

class Player:
    """pass"""
    def __init__(self):
        self.hand = []
        self.points = [0, 0]

    def get_hand(self):
        """works"""
        new_deck = DeckOfCards().deck
        deck_lenght = len(new_deck)
        self.hand = [new_deck.pop(r.randint(0, deck_lenght-1)) for i in range(2)]
        self.count_points()

    def count_points(self):
        """works"""
        self.points = [0, 0]
        for card in self.hand:
            if card == 'A':
                self.points[0] += 1
                self.points[1] += 11
            elif card in ['T', 'J', 'Q', 'K']:
                self.points[0] += 10
                self.points[1] += 10
            else:
                self.points[0] += int(card)
                self.points[1] += int(card)
        print(self.points)


playa = Player()


