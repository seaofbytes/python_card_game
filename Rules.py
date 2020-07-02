import math

# The Rules class is in charge of calculating the score based on a set of rules.

# Game rules class


class Rules:
    # Get numerical score
    @staticmethod
    def get_numerical_score(player):
        numerical_score = 0

        for card in player.hand:
            numerical_score += card[0]

        print(
            f'Player {player.name} has scored {numerical_score} NUMERICAL score')
        return numerical_score

    # Get the duplicate score
    @staticmethod
    def get_duplicates_score(player):

        duplicate_score = 0
        count = {}
        for card in player.hand:
            if card[0] in count:
                count[card[0]] = count[card[0]] + 1
            else:
                count[card[0]] = 1

        for value in count:
            if count[value] > 1:
                count[value] = value**count[value]
                duplicate_score += count[value]

        print(
            f'Player {player.name} has scored {duplicate_score} DUPLICATE score')
        return duplicate_score

    # Get single suite score
    @staticmethod
    def get_single_suite_score(suite, hand):
        x = []
        m = math.inf
        result = 0

        for card in hand:
            if suite in card[1]:
                x.append(card)
                if int(card[0]) < m:
                    m = int(card[0])

        if len(x) > 1:
            result = int(min(x[0] for x in x)) * len(x)
        return result

    # Get the suite score
    @staticmethod
    def get_suite_score(player):
        s = sum([Rules.get_single_suite_score(suite, player.hand)
                 for suite in ["Diamonds", "Spades", "Clubs", "Hearts"]])
        player.suite_score = s
        print(f'Player {player.name} has scored {s} SUITE score')

        return s

    # Get sequential score
    @staticmethod
    def get_sequential_score(player):
        cards = [c[0] for c in player.hand]
        cards.sort()
        total = 0
        sequence_count = 1

        for i in range(len(cards)):
            # skip first
            if i == 0:
                continue

            # get if this card is previous + 1
            if cards[i-1] == cards[i] - 1:
                sequence_count += 1

                # Check if next card is in sequence, if not, calculate score
                if i+1 == len(cards) or cards[i+1] != cards[i]+1:
                    total += sequence_count * cards[i]
                    sequence_count = 1

        player.sequential_score = total
        print(
            f'Player {player.name} has scored {player.sequential_score} SEQUENTIAL score')
        return total

    # Get the difference between biggest / smallest card
    @staticmethod
    def get_diff_score(player):
        hand = [c[0] for c in player.hand]
        min_val = min(n for n in hand)
        max_val = max(n for n in hand)
        result = max_val - min_val
        player.diff_score = result
        print(
            f'Player {player.name} has scored {player.diff_score} DIFFERENCE score')
        return result

    # Get total score from all scores

    @staticmethod
    def get_total_score(player):
        total = player.total_score = player.duplicate_score + player.numerical_score + \
            player.suite_score + player.sequential_score + player.diff_score
        #total = Rules.get_numerical_score(player) + Rules.get_duplicates_score(player) + Rules.get_sequential_score(player) + Rules.get_suite_score(player) + Rules.get_diff_score(player)
        print(
            f'Player {player.name} has scored a TOTAL of {player.total_score}')
        return total

    # Get the winner of the round
    @staticmethod
    def get_winner(players):
        ranking = sorted(players, key=lambda p: p.total_score, reverse=True)
        first_place = list(filter(lambda p: p.total_score ==
                                  ranking[0].total_score, ranking))

        return first_place
