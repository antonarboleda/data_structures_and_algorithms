
"""
Card 
- rank. There are 13 ranks from 2 to Ace
- suit. clubs, diamonds, heards spades

Deck
- 52 cards
draw()
# randomizes order
shuffle() 

Player
- hand 5 cards

takes the top card from the deck and adds to hand
draw()

plays a card
play() 

Game
   - round
   init_game()
    - prepare the deck
    - shuffle the deck()
    - create player 1 and player 2
    - draw cards for each player in the deck
    - print out cards for each player

   play() 
    - Plays a single hand
    - depending on what round it is
    - first player draws their highest card
    - Second player sees if they can beat it
       1. see if they have a card that can beat player 1's card
       2. draw if they have less than 5 cards
       3. otherwise discard their worst card
    whether they can play another hand
    canPlay() 

Game
- 2 players
- Give them 5 cards each
- Each turn, each player will reveal their top card
   - If the second player doesn't have a better card than what has been 
   played and they have < 5 cards, they can draw from the deck
- The player with the higher card will win
- Adds a point to the leaderboard
- Players will alternate rounds. I.e. player1 plays first in round 1, player 2 
plays first in round 2
"""

import random
from heapq import heappush, heapify, heappop

class Player:
    def __init__(self):
        self.hand = []
        heapify(self.hand)
        self.points = 0
    
    # plays their best card
    def play(self):
        val = heappop(self.hand)        
        return val

    def draw(self, deck):
        heappush(self.hand, deck.draw())

    def getPoints(self):
        return self.points
    
    def canPlay(self):
        return len(self.hand) > 0
    
    def incrementPoints(self):
        self.points += 1


class Deck:
    def __init__(self):
        self.deck = self.createDeck()
        self.shuffle()
        
    def createDeck(self):
        deck = []
        for suit in ["HEART", "DIAMOND", "CLUB", "SPADE"]:
            for card in range(1,14):
                deck.append((card, suit))
        return deck
    
    def canDraw(self):
        return len(self.deck) > 0
    
    def shuffle(self):
        random.shuffle(self.deck)
        for i in range(len(self.deck)):
            j = random.randint(0,len(self.deck)-1)
            tmp = self.deck[i]
            self.deck[i] = self.deck[j]
            self.deck[j] = tmp
        print(self.deck)
    
    def draw(self):
        res = self.deck.pop()
        return res


# Game>Player, Deck, Card
class Game:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.deck = Deck()
        self.round = 0
    
    def canPlay(self):
        if not self.deck.canDraw() and not self.player1.canPlay() and not self.player2.canPlay():
            return False
        return True

    
    def playHand(self):
        player1Val = self.player1.play()
        player2Val = self.player2.play()
        if player1Val > player2Val:
            self.player1.incrementPoints()
        else:
            self.player2.incrementPoints()
        
        self.round += 1
        if not self.canPlay():
            print("Game over")
            print("P1", self.player1.getPoints())
            print("P2", self.player2.getPoints())
            return    
        if self.deck.canDraw():
            self.player1.draw(self.deck)
            self.player2.draw(self.deck)

    def play(self):
        # deal cards
        for _ in range(5):
            self.player1.draw(self.deck)
            self.player2.draw(self.deck)
        # take turns        
        for i in range(26):
            self.playHand()
        
        # declare winner
        if self.player2.points > self.player1.points:
            print("Player2 Wins")
        elif self.player1.points > self.player2.points:
            print("Player1 Wins")
        else:
            print("Tie!")

    def initGame(self):
        for _ in range(5):
            self.player1.draw(self.deck)
            self.player2.draw(self.deck)
        print("p1 hand", self.player1.hand)
        print("p2 hand", self.player2.hand)


game = Game()
game.initGame()
game.play()
print(game.round)
# game.playHand() # player 1 wins
# game.getScore() # {Player 1: 1, Player 2: 0}
# game.playHand()
# game.playHand()
# game.playHand()
# game.playHand()
# game.playHand()
# game.playHand()
# game.playHand()
# game.playHand()
# game.playHand()
# game.playHand()
# game.playHand()

