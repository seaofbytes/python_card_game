# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.total_score = 0

    # Deal cards to players
    # NOTE: In the instructions it is written that PLAYER deals the cards, that was my reasoning for putting this method in the Player class. :)
    
    # Deal cards and show them after everyone has 5 cards
    def deal_cards(self, deck, players, num_of_cards=5):
        for player in players:
            player.hand.append(deck.deal_card())
            print(f'Card dealt to {player.name}')
            

        if num_of_cards - 1 > 0:
            self.deal_cards(deck, players, num_of_cards-1)
