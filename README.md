# With The Power Of The King
Logic for a card game written in python, following a strict set of rules. Object Oriented approach.
On the bottom of this document there are some example hands with their corresponding points.

The goal of this project is to build a simple card game where each player draws 5 cards from a
deck of cards and gets points based on those cards.

##To play the game you do the following.
- Get a deck of normal playing cards. This deck should have 52 cards in four suits:
Diamonds, Hearts, Clubs and Spades. For each of these suits you have: an Ace, the
numbers 2 to 10, a Jack, a Queen and a King
- Shuffle the deck thoroughly
- One of the players is the dealer and gives cards to the others. This he does by giving
each player (including himself) 1 card, then go to the next, until each player has 5 cards
- Once everybody has their cards they calculate the score, which their cards have, based
on the rules defined later
- Each player shows it’s cards and the player with the highest total score wins the round.
In case two or more players have the same highest score, it’s a draw between those
players
The rules for calculating the score:
1. First they calculate the sum of the numerical values of their cards. The Ace counts as 1,
a Jack as 11, a Queen as 12 and a King as 13.
2. The second rule is that whenever they have multiple cards of the same numerical value,
they add points for each duplicate: <numerical value>^<amount of that value>. For
example, if there are two 5s and three 7s they get 5*5 + 7*7*7 = 25 + 343 = 368 points
3. For the third rule the same applies for having multiple of the same suit except the
calculation goes like <amount of suit> * <lowest numerical value of suit>. For example,with the cards. 2 Clubs, 6 Clubs, 8 Hearts, 10 Hearts, Jack of Clubs they get:
3 (Clubs) * 2 + 2 (Hearts) * 8 = 6 + 16 = 22 points
4. The fourth rule is regarding sequential numerical values. The order of cards received
does not matter for this. For each row of sequential values they’ll get <amount of
sequential> * <highest of the row> points. For example having the cards: 2 of Diamonds,
3 of Hearts, 5 of Clubs, 6 of Clubs and 7 of Spades will give the player 2 * 3 + 3 * 7 = 6 +
21 = 27 points
5. The last (fifth) rule is adding the difference between the highest card and the lowest
card. With the same cards as the previous rule (2 of Diamonds, 3 of Hearts, 5 of Clubs, 6
of Clubs and 7 of Spades) it will add an additional 7 - 2 = 5 points.
  
  
![](https://i.imgur.com/VKOF2mr.png)

