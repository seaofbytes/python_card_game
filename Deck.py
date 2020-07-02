import random

# Deck class


class Deck:
    def __init__(self):
        self.suites = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
        self.cards = []
        self.build_deck()

    # Wasnt sure if I was supposed to make a Shuffle class to make the shuffling more customizable
    def shuffle_deck(self):
        random.shuffle(self.cards)
        print('Cards have been shuffled.')

    # Maybe put this in init ?
    def build_deck(self):
        self.cards = []
        for val in range(13):
            for suite in self.suites:
                self.cards.append([val+1, suite])

        print(self.cards, len(self.cards), " AAAAAAAAAAAAAAAAAAAAAAAAAAAA")

            

    def deal_card(self):
        return self.cards.pop()

    def print_deck(self):
        print(self.cards)
        print(len(self.cards), 'cards in deck left')

    def vals_to_suites(self, hand):
        for card in hand:
            if card[0] == 11 : print(f'J of {card[1]}')
            elif card[0] == 12 : print(f'Q of {card[1]}')
            elif card[0] == 13 : print(f'K of {card[1]}')
            elif card[0] == 1 : print(f'A of {card[1]}')
            else :
                print(f'{card[0]} of {card[1]}')
            
