import matplotlib.pyplot as plt
import random as r
import copy as c

import genetic

f = open('results.txt', 'a')

GENERATIONS_NEEDED = 10000
CROSSING_CHANCE = 0.9
MUTATION_CHANCE = 0.1
POPULATION_SIZE = 50
GAMES_TO_PLAY = 100
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
        self.made_turn = False


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
        self.dealer_busted = False

    def deal_cards(self):
        if len(self.deck) < 15:
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
        self.player.hand = []
        self.dealer.hand = []
        self.player.money -= BET_AMOUNT
        self.player_bet = BET_AMOUNT
        self.player.stand = False
        self.dealer.stand = False
        self.splitted = False
        self.player.surrended = False
        # self.dealer_busted = False
        self.dealer.made_turn = False
        for i in range(2):
            self.player.hand.append(self.deck.pop(r.randint(0, len(self.deck)-1)))
            self.dealer.hand.append(self.deck.pop(r.randint(0, len(self.deck)-1)))
        self.count_points(self.player)
        self.count_points(self.dealer)
        f.write(str(self.player.hand))
        f.write('\n')

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
        person.hand.append(self.deck.pop(r.randint(0, len(self.deck)-1)))
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
            f.write('player hits')
            f.write('\n')
        elif action == 2:
            f.write('player stands')
            f.write('\n')
        elif action == 3:
            f.write('player doubling down')
            f.write('\n')
        elif action == 4:
            f.write('player surrenders')
            f.write('\n')
        elif action == 5:
            f.write('player splits')
            f.write('\n')

    def win(self):
        if not self.splitted:
            self.player.money += self.player_bet * 2
        else:
            self.player.money += self.player_bet
        f.write('win')
        f.write('\n')

    def busted(self):
        f.write('busted')
        f.write('\n')

    def blackjack(self):
        self.player.money += self.player_bet
        self.player.money += self.player_bet / 2 * 3
        f.write('blackjack')
        f.write('\n')

    def draw(self):
        if not self.splitted:
            self.player.money += self.player_bet
        else:
            self.player.money += self.player_bet / 2
        f.write('draw')
        f.write('\n')

    def sur(self):
        f.write('surrender')
        f.write('\n')



    def play_split_game(self):
        self.player.hand = self.player.buffer_hand
        self.hit(self.player)
        self.player.stand = False

        # Перевірка по другому рівню хромосом
        while not self.player.stand:
            # Перевірка на перебір + підрахунок очок
            self.count_points(self.player)
            if self.player.points[0] < 22 and self.player.points[1] < 22:
                point_index = r.randint(0, 1)
            else:
                point_index = self.player.points.index(min(self.player.points))
                if self.player.points[point_index] > 21:
                    return self.busted()

            # Прийняття рішення
            card_index_3 = self.player.points[point_index]
            dealer_card_index = SAMPLE_DECK.index(self.dealer.hand[0])
            action = self.player.genome.second_layer[dealer_card_index][card_index_3 - 1]
            self.show_choice(action)
            self.make_choice(action)
            if self.player.points[0] > 21 and self.player.points[1] > 21:
                return self.busted()

        if self.player.surrended:
            return self.sur()
        if self.player.points[0] > 21 and self.player.points[1] > 21:
            return self.busted()

        if not self.dealer.made_turn:
            # Хід дилера
            self.made_turn = True
            while not self.dealer.stand:
                if self.dealer.points[0] > 21 and self.dealer.points[1] > 21:
                    return self.win()
                elif self.dealer.points[0] > 16 or (self.dealer.points[1] > 16 and self.dealer.points[1] < 22):
                    self.dealer.stand = True
                else:
                    self.hit(self.dealer)

        # Порівняння очок
        player_points = self.player.points[1] if self.player.points[1] < 22 else self.player.points[0]
        dealer_points = self.dealer.points[1] if self.dealer.points[1] < 22 else self.dealer.points[0]
        if player_points > dealer_points or dealer_points > 21:
            return self.win()
        elif player_points < dealer_points and dealer_points < 22:
            return self.busted()
        else:
            return self.draw()

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
        self.show_choice(action)

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
            dealer_card_index = SAMPLE_DECK.index(self.dealer.hand[0])
            action = self.player.genome.second_layer[dealer_card_index][card_index_3 - 1]
            self.show_choice(action)
            self.make_choice(action)
            if self.player.points[0] > 21 and self.player.points[1] > 21:
                return self.busted()

        if self.player.surrended:
            return self.sur()
        if self.player.points[0] > 21 and self.player.points[1] > 21:
            return self.busted()

        #Хід дилера
        self.dealer.made_turn = True
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




class Population():
    def __init__(self):
        self.players = [Player() for i in range(POPULATION_SIZE)]
        self.list_of_best = []
        self.list_of_mean = []

    def test_player(self, person):
        table = Table()
        table.player = person
        for i in range(GAMES_TO_PLAY):
            f.write(f"Player {self.players.index(table.player)+1}, Game {i+1}\n")
            table.play_one_game()
            f.write(f"player{table.player.hand, table.player.points}\n")
            f.write(f"dealer{table.dealer.hand, table.dealer.points}\n")
            if table.splitted:
                f.write('split hand')
                f.write('\n')
                table.play_split_game()
                f.write(f"player{table.player.hand, table.player.points}\n")
                f.write(f"dealer{table.dealer.hand, table.dealer.points}\n")
            f.write(f"Money: {table.player.money}\n")
            f.write("----------------------------")
            f.write('\n')

    def tournament(self):
        best_players = []
        for i in range(POPULATION_SIZE):
            a1 = a2 = a3 = 0
            while a1 == a2 or a1 == a3 or a2 == a3:
                a1, a2, a3 = r.randint(0, POPULATION_SIZE-1), r.randint(0, POPULATION_SIZE-1), r.randint(0, POPULATION_SIZE-1)
            best = max(self.players[a1], self.players[a2], self.players[a3], key=lambda player: player.money)
            best_players.append(c.deepcopy(best))
        self.players = best_players

    def cross_two_players(self, list, pl1, pl2):
        start_layer_map = [[r.randint(0, 1) for i in range(13)] for j in range(13)]
        second_layer_map = [[r.randint(0, 1) for i in range(21)] for j in range(13)]

        #Схрещення першого слоя
        for i in range(13):
            for j in range(13):
                if start_layer_map[i][j] == 1:
                    pl1.genome.start_layer[i][j], pl2.genome.start_layer[i][j] = pl2.genome.start_layer[i][j], pl1.genome.start_layer[i][j]

        # Схрещення другого слоя
        for i in range(13):
            for j in range(21):
                if second_layer_map[i][j] == 1:
                    pl1.genome.second_layer[i][j], pl2.genome.second_layer[i][j] = pl2.genome.second_layer[i][j], pl1.genome.second_layer[i][j]

        #Додання потомків у список
        list.append(pl1)
        list.append(pl2)



    def crossing(self):
        new_players = []
        for i in range(0, POPULATION_SIZE, 2):
            if r.random() <= CROSSING_CHANCE:
                self.cross_two_players(new_players, self.players[i], self.players[i+1])
            else:
                new_players.append(self.players[i])
                new_players.append(self.players[i+1])
        print(len(new_players))
        self.players = new_players

    def mutate(self):
        for player in self.players:
            if r.random() <= MUTATION_CHANCE:
                first_row = r.randint(0, 12)
                first_col = r.randint(0, 12)
                second_row = r.randint(0, 12)
                second_col = r.randint(0, 20)
                if first_row == first_col:
                    player.genome.start_layer[first_row][first_col] = r.randint(1, 5)
                else:
                    player.genome.start_layer[first_row][first_col] = r.randint(1, 4)
                player.genome.second_layer[second_row][second_col] = 1 if player.genome.second_layer[second_row][second_col] == 2 else 2

    def start_project(self):
        for i in range(GENERATIONS_NEEDED):
            buffer = []
            f.write(f"Generation {i}")
            for p in range(POPULATION_SIZE):
                self.test_player(self.players[p])
                f.write('~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~\n')
            best_playa = max(self.players, key=lambda playa: playa.money)

            if best_playa.money >= 100:
                print(f"\nAt generation {i} player #{self.players.index(best_playa)+1} with {best_playa.money} money")
                best_playa.genome.show_start_gene()
                print()
                best_playa.genome.show_second_layer()

            self.list_of_best.append(best_playa.money)
            for p in self.players:
                buffer.append(p.money)
            self.list_of_mean.append(sum(buffer) / POPULATION_SIZE)
            self.tournament()
            self.mutate()
            self.resume_money()

        # Графік
        fig, ax = plt.subplots()
        plt.plot(self.list_of_best, color="red")
        plt.plot(self.list_of_mean, color="green")
        plt.show()

    def resume_money(self):
        for player in self.players:
            player.money = 100




pop = Population()
pop.start_project()
f.close()
# for i in range(POPULATION_SIZE):
#     pop.test_player(pop.players[i])
#     f.write('~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~\n')
# for i in pop.players:
#     print(i.money)


# tb = Table()
# print(tb.player.money)
# tb.play_one_game()
# print(f"player{tb.player.hand, tb.player.points}")
# print(f"dealer{tb.dealer.hand, tb.dealer.points}")
# if tb.splitted:
#     print('split hand')
#     tb.play_split_game()
#     print(f"player{tb.player.hand, tb.player.points}")
#     print(f"dealer{tb.dealer.hand, tb.dealer.points}")
# print(tb.player.money)





