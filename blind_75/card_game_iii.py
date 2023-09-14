
"""
Game
- Players
- Leaderboard
Deck
- Cards
Card
- rank
- suite
"""
import random

class Player:
    def __init__(self, playerNum):
        self.hand = []
        self.playerNum = playerNum
    
    def draw(self, card):
        self.hand.append(card)
    def playCard(self):
        cardIndex = -1
        maxRank = -1
        
        for index, (rank, _) in enumerate(self.hand):
            if rank > maxRank:
                maxRank = rank
                cardIndex = index
        
        return self.hand.pop(cardIndex)

class Game:
    def __init__(self, numPlayer: int):
        self.players = self.createPlayers(numPlayer)
        self.deck = []
        self.leaderboard = [0] * numPlayer

    def play(self):
        self.dealCards()
        
        self.takeTurns()

        self.declareWinner()

    def createPlayers(self, numPlayers):
        players = []
        for i in range(numPlayers):
            players.append(Player(i))
        return players
    
    def dealCards(self):
        print("dealing cards")
        for rank in range(1,14):
            for suite in range(4):
                self.deck.append((rank,suite))
        
        print("shuffling cards", len(self.deck))
        # shuffle
        for i in range(len(self.deck)):
            j = random.randint(i, len(self.deck) - 1)
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]
        
        # deal to players
        for _ in range(5):
            for player in self.players:
                player.draw(self.deck.pop())

    def takeTurns(self):
        for i in range(52 // len(self.players)):
            highestRank = -1
            winner = -1
            for index in range(len(self.players)):
                p = self.players[index]
                rank, suite = p.playCard()
                if rank > highestRank:
                    winner = index
                    highestRank = rank
                if self.deck:
                    card = self.deck.pop()
                    p.draw(card)
            self.leaderboard[winner] += 1
    
    def declareWinner(self):
        maxWins = -1
        winnderIndex = -1
        for index, win in enumerate(self.leaderboard):
            if win > maxWins:
                winnderIndex = index
                maxWins = win
        print(f"player {winnderIndex + 1} is the winner!")

game = Game(4)
game.play()