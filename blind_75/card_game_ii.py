
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

class Player:
    def __init__(self):
        self.hand = []
    
    def draw(self, card):
        self.hand.append(card)
    
    def play(self):
        best = -1
        result = (-1,-1)
        remove = -1
        for index, (rank, suite) in enumerate(self.hand):
            if rank > best:
                result = (rank,suite)
                best = rank
                remove = index
        self.hand.pop(remove)
        return result

class Deck:
    def __init__(self):
        self.deck = self.createDeck()
        self.shuffleDeck()
    
    # create and shuffle the deck
    def createDeck(self):
        suites = ["HEART", "SPADE", "DIAMOND", "CLUB"]
        # (rank, suite)
        deck = []
        for i in range(52):
            rank = i % 13
            suite = suites[i%4]
            deck.append((rank, suite))
        return deck
    
    def shuffleDeck(self):
        random.shuffle(self.deck)
        for i in range(51, -1, -1):
            j = random.randint(0, i)
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]
    
    def draw(self):
        return self.deck.pop()

class Game:
    def __init__(self, numPlayers: int):
        # self.player1 = Player()
        # self.player2 = Player()
        self.players = [Player() for i in range(numPlayers)]
        self.leaderboard = [0] * numPlayers
        self.deck = self.buildDeck()
        
    def initPlayers(self, n):
        players = []
        for i in range(n):
            players.append(Player())
        return players

    def buildDeck(self):
        suites = ["HEART", "SPADE", "DIAMOND", "CLUB"]
        # (rank, suite)
        deck = []
        for i in range(52):
            rank = i % 13
            suite = suites[i%4]
            deck.append((rank, suite))
        random.shuffle(deck)
        return deck        
    
    def dealCards(self):
        for i in range(5):
            for player in self.players:
                player.draw(self.deck.pop())
    def canPlay(self):
        for p in self.players:
            if not len(p.hand):
                return False
        return True
    def takeTurns(self):        
        while self.canPlay():
            winner = -1
            bestRank = -1
            for playerIdx in range(len(self.players)):
                player = self.players[playerIdx]
                rank, _ = player.play()
                if rank > bestRank:
                    bestRank = rank
                    winner = playerIdx
                if len(self.deck) > 0:
                    card = self.deck.pop()
                    player.draw(card)
            self.leaderboard[winner] += 1

    def playGame(self):
        # deal cards
        self.dealCards()
        # take turns
        self.takeTurns()
        # declare winner
        print(self.leaderboard)
g = Game(3)
g.playGame()