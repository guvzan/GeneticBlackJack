import random as r

import genetic

BET_AMOUNT = 10
SAMPLE_DECK = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

class Player:
    def __init__(self):
        #Основні змінні
        self.hand = []
        self.points = [0, 0]
        self.money = 100
        self.genome = genetic.Chromosome()

        #Допоміжні змінні
        self.bufer_hand = []
        self.games_played = 0
        self.stand = False
        self.surrended = False


class Dealer:
    def __init__(self):
        # Основні змінні
        self.hand = []
        self.points = [0, 0]

        # Допоміжні змінні
        self.stand = False


class Table:
    def __init__(self):
        #Основні змінні
        self.deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K',
                     'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K',
                     'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K',
                     'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K',

                     'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K',
                     'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K',
                     'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K',
                     'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K',

                     'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K',
                     'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K',
                     'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K',
                     'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K',

                     'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K',
                     'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K',
                     'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K',
                     'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K',]
        self.player = Player()
        self.dealer = Dealer()

        #Допоміжні змінні
        self.player_bet = 0
        self.splitted = False

    def deal_cards(self):
        self.player.hand = []
        self.dealer.hand = []
        self.player.money -= BET_AMOUNT
        self.player_bet = BET_AMOUNT
        self.player.stand = False
        self.dealer.stand = False
        self.splitted = False
        self.player.surrended = False
        for i in range(2):
            self.player.hand.append(self.deck.pop(r.randint(0, len(self.deck)-1)))
            self.dealer.hand.append(self.deck.pop(r.randint(0, len(self.deck)-1)))
        self.count_points(self.player)
        self.count_points(self.dealer)

    def count_points(self, person):
        person.points = [0, 0]
        for card in person.hand:
            if card == 'A':
                if person.hand.count('A') < 2:
                    person.points[0] += 1
                    person.points[1] += 11
                else:
                    person.points[0] += 1
                    person.points[1] += 1
            elif card in ['T', 'J', 'Q', 'K']:
                person.points[0] += 10
                person.points[1] += 10
            else:
                person.points[0] += int(card)
                person.points[1] += int(card)

    def hit(self, person):
        person.hand.append(self.deck.pop(r.randint(0, len(self.deck))))
        self.count_points(person)

    def double_down(self):
        self.player.money -= BET_AMOUNT
        self.player_bet += BET_AMOUNT
        self.hit(self.player)
        self.player.stand = True

    def surrender(self):
        self.player.money += BET_AMOUNT / 2
        self.player_bet = 0
        self.player.stand = True
        self.player.surrended = True

    def split(self):
        self.splitted = True
        self.player.money -= BET_AMOUNT
        self.player_bet += BET_AMOUNT
        self.player.buffer_hand = [self.player.hand[1]]
        self.player.hand = [self.player.hand[0]]
        self.hit(self.player)

    def check_if_blackjack(self):
        p_has_21 = True if 21 in self.player.points else False
        d_has_21 = True if 21 in self.dealer.points else False
        if p_has_21 and not d_has_21:
            return True
        return False

    def make_choice(self, action):
        """pass"""
        if action == 1:
            self.hit(self.player)
        elif action == 2:
            self.player.stand = True
        elif action == 3:
            self.double_down()
        elif action == 4:
            self.surrender()
        elif action == 5:
            self.split()

    def show_choice(self, action):
        """pass"""
        if action == 1:
            print('hit')
        elif action == 2:
            print('stand')
        elif action == 3:
            print('double down')
        elif action == 4:
            print('surrender')
        elif action == 5:
            print('split')

    def win(self):
        self.player.money += self.player_bet * 2
        print('win')

    def busted(self):
        print('busted')

    def blackjack(self):
        self.player.money += self.player_bet
        self.player.money += self.player_bet / 2 * 3
        print('blackjack')

    def draw(self):
        self.player.money += self.player_bet
        print('draw')

    def sur(self):
        print('surrender')

    def play_one_game(self):
        #Роздача карт і перевірка на блекджек
        self.deal_cards()
        if self.check_if_blackjack():
            return self.blackjack()

        #Перевірка по першому рівню хромосом
        card_index_1 = SAMPLE_DECK.index(self.player.hand[0])
        card_index_2 = SAMPLE_DECK.index(self.player.hand[1])
        action = self.player.genome.start_layer[card_index_1][card_index_2]
        self.make_choice(action)
        print(action)

        # Перевірка по другому рівню хромосом
        while not self.player.stand:
            #Перевірка на перебір + підрахунок очок
            self.count_points(self.player)
            if self.player.points[0] < 22 and self.player.points[1] < 22:
                point_index = r.randint(0, 1)
            else:
                point_index = self.player.points.index(min(self.player.points))
                if self.player.points[point_index] > 21:
                    return self.busted()

            #Прийняття рішення
            card_index_3 = self.player.points[point_index]
            action = self.player.genome.second_layer[card_index_3 - 1]
            print(action)
            self.make_choice(action)
            if self.player.points[0] > 21 and self.player.points[1] > 21:
                return self.busted()

        if self.player.surrended:
            return self.sur()
        if self.player.points[0] > 21 and self.player.points[1] > 21:
            return self.busted()

        #Хід дилера
        while not self.dealer.stand:
            if self.dealer.points[0] > 21 and self.dealer.points[1] > 21:
                return self.win()
            elif self.dealer.points[0] > 16 or (self.dealer.points[1] > 16 and self.dealer.points[1] < 22):
                self.dealer.stand = True
            else:
                self.hit(self.dealer)


        #Порівняння очок
        player_points = self.player.points[1] if self.player.points[1] < 22 else self.player.points[0]
        dealer_points = self.dealer.points[1] if self.dealer.points[1] < 22 else self.dealer.points[0]
        if player_points > dealer_points:
            return self.win()
        elif player_points < dealer_points:
            return self.busted()
        else:
            return self.draw()





tb = Table()
print(tb.player.money)
tb.play_one_game()
print(f"player{tb.player.hand, tb.player.points}")
print(f"dealer{tb.dealer.hand, tb.dealer.points}")
print(tb.player.money)





