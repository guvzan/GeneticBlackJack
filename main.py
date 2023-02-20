import random as r

import genetic

BET_AMOUNT = 10
SAMPLE_DECK = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

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
        self.chromosome = genetic.Chromosome()

        self.money = 100
        self.hand = []
        self.points = [0, 0]
        self.stand = False
        self.bet_placed = 0
        self.buffer_hand = []
        self.splitted = False


    def show_hand(self):
        """pass"""
        print(self.hand)

    def get_hand(self):
        """works"""
        self.new_deck = DeckOfCards().deck
        deck_lenght = len(self.new_deck)
        self.hand = [self.new_deck.pop(r.randint(0, deck_lenght-1)) for i in range(2)]
        self.count_points()

    def count_points(self):
        """pass"""
        self.points = [0, 0]
        for card in self.hand:
            if card == 'A':
                if self.hand.count('A') < 2:
                    self.points[0] += 1
                    self.points[1] += 11
                else:
                    self.points[0] += 1
                    self.points[1] += 1
            elif card in ['T', 'J', 'Q', 'K']:
                self.points[0] += 10
                self.points[1] += 10
            else:
                self.points[0] += int(card)
                self.points[1] += int(card)

    def hit(self):
        """pass"""
        self.hand.append(self.new_deck.pop(r.randint(0, len(self.new_deck))))
        self.count_points()


    def double_down(self):
        """pass"""
        self.hit()
        self.money -= BET_AMOUNT
        self.bet_placed += BET_AMOUNT
        self.stand = True

    def split(self):
        """pass"""
        self.splitted = True
        self.money -= BET_AMOUNT
        self.bet_placed += BET_AMOUNT
        self.buffer_hand = [self.hand[1]]
        self.hand = [self.hand[0]]
        self.hit()

    def surrender(self):
        """pass"""
        self.money += BET_AMOUNT / 2
        self.bet_placed = 0
        self.stand = True

    def make_choice(self, action):
        """pass"""
        if action == 1:
            self.hit()
        elif action == 2:
            self.stand = True
        elif action == 3:
            self.split()
        elif action == 4:
            self.double_down()
        elif action == 5:
            self.surrender()



    def show_action(self, action):
        """pass"""
        if action == 1:
            print('hit')
        elif action == 2:
            print('stand')
        elif action == 3:
            print('split')
        elif action == 4:
            print('double down')
        elif action == 5:
            print('surrender')


    def check_points(self):
        """pass"""
        if self.points[0] > 21 and self.points[1] > 21:
            return 'busted'
        return 'ok'

    def play(self):
        """pass"""
        #Технічні змінні
        self.stand = False
        self.money -= BET_AMOUNT
        self.bet_placed = BET_AMOUNT
        self.splitted = False
        self.get_hand()

        #Фаза двох карт
        print(f"your hand is{self.hand}, {self.points}")
        index_1 = SAMPLE_DECK.index(self.hand[0])
        index_2 = SAMPLE_DECK.index(self.hand[1])
        action = self.chromosome.start_layer[index_1][index_2]
        self.show_action(action)
        self.make_choice(action)
        print(self.hand, self.points)

        #Фаза добору
        while not self.stand:
            if self.points[0] < 22 and self.points[1] < 22:
                point_index = r.randint(0, 1)
            else:
                point_index = self.points.index(min(self.points))
            status = self.check_points()
            if status == 'ok':
                action = self.chromosome.second_layer[self.points[point_index]-1]
                self.show_action(action)
                self.make_choice(action)
                print(self.hand, self.points)
            else:
                print(self.hand, self.points)
                break



        #Сплітова рука


    def play2(self):
        """pass"""
        self.stand = False
        self.money -= BET_AMOUNT
        self.bet_placed = BET_AMOUNT
        self.splitted = False
        self.get_hand()

        print(f"your hand is{self.hand}, {self.points}")
        print("1.hit\n2.double down\n")
        while not self.stand:

            action = int(input())
            if action == 1:
                self.hit()
            elif action == 2:
                self.double_down()
            elif action == 3:
                self.split()
            else:
                self.stand = True

            print(f"your hand is{self.hand}, {self.points}")
            print("1.hit\n2.double down\n")

        if self.splitted:
            print('yes')
            self.hand = self.buffer_hand
            self.hit()
            print(self.hand)
            print(self.points)






playa = Player()
playa.play()


