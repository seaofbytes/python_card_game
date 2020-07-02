class Game():
    def __init__(self, players, deck, rules):
        self.name = 'With The Power of the King !'
        self.players = players
        self.rounds = {}
        self.deck = deck
        self.rounds = []
        self.round = 1
        self.rules = rules

    # Play one round
    def play_round(self):
        name = input('Welcome to With the Power of the King. Please enter your name :')
        self.deck.build_deck()
        self.deck.shuffle_deck()
        self.players[0].name = name
        print(f'Welcome, {self.players[0].name}, you are the dealer.')

        self.players[0].deal_cards(self.deck, self.players)
        print('Cards dealt. Everybody has 5 cards.')

        # Get all the scores
        for player in self.players:
            print(player.name, " hand")
            self.deck.vals_to_suites(player.hand)
            num_score = self.rules.get_numerical_score(player)
            dup_score = self.rules.get_duplicates_score(player)
            suite_score = self.rules.get_suite_score(player)
            seq_score = self.rules.get_sequential_score(player)
            diff_score = self.rules.get_diff_score(player)

            player.total_score = num_score + dup_score + \
                suite_score + seq_score + diff_score
            print(f'{player.name} has a TOTAL SCORE of {player.total_score}')
            print("-------------------------")

        winner = self.rules.get_winner(self.players)

        for p in winner:
            if len(winner) > 1:
                print("Draw between: ")
            print(
                f'{p.name} has won the round with a score of {p.total_score} \n-------------------------')

        self.save_round(self.players)

        # Return cards to deck
        for player in self.players:
            self.deck.cards += player.hand
            player.hand = []

        # get what the player wants to do next
        word = input("Thanks for playing. If you want to play another round, enter 'play', if you want to see the hand history, enter 'history', if you want to quit, enter 'quit' or press enter: ")

        if word == 'play':
            self.play_round()
        elif word == 'history':
            self.show_game_history()
            word = input("Game History. If you want to play another round, enter 'play',  if you want to quit, enter 'quit' or press enter : ")
            if word == 'play': self.play_round()
        elif word == 'quit' or '':
            print(f'Thanks for playing {self.name} !')


    # Save round to history
    def save_round(self, players):
        this_round = {
            "round_number": 0,
            "players": [],
            "winner": ''
        }

        for player in players:
            this_round["players"].append(
                {"name": player.name, "total_score": player.total_score, "hand": [player.hand]})

        this_round["round_number"] = len(self.rounds) + 1
        this_round["winner"] = self.rules.get_winner(players)
        self.rounds.append(this_round)

    def show_game_history(self):
        print("----------------- \n GAME HISTORY \n-----------------")

        for r in self.rounds:
            print(f'Round {r["round_number"]}  \n-----------------')

            for player in r["players"]:
                print("Player name: ", player["name"])

                for c in player["hand"]:
                    print("Player hand:")

                    for x in c:
                        print(f'- {x[0]} of {x[1]}')

                    print("-----------------",)
            print("Round winner :", r["winner"][0].name)
            print("Score :" , r["winner"][0].total_score, "\n \n ")
