from Player import Player
from Deck import Deck
from Game import Game
from Rules import Rules


# Heya :)
# Here is my completed game, it took me about 10~ hours to complete I believe.
# In the requirements it is said not to treat this as a start of a bigger project, but I really hated having so much code in
# one file so I separated it into small modules so it looks cleaner. Hope you dont mind !

# You can just run index.py and check the terminal for the output ! 
# ( I left the numerical values of each card in the terminal history output so it is easier for you to check the math. )

# I really hope you like it !  :)
#-Sandi

# Init Players
p1 = Player('P1')
p2 = Player('P2')
p3 = Player('P3')
p4 = Player('P4')
p5 = Player('P5')

players = [p1, p2, p3, p4, p5]

# Init rules
rules = Rules()

# Init deck
deck = Deck()

# New Game
newGame = Game(players, deck, rules)
newGame.play_round()
