import random
import numpy as np

def createBoard():
    colors = ['Red', 'Purple', 'Yellow', 'Blue', 'Orange', 'Green']
    candyPeople = {'Plumpy': 21, 'Mr. Mint': 33, 'Jolly': 57, 'Gramma Nutt': 84, 'Princess Lolly': 93, 
               'Queen Frostine': 120}
    board = colors * 25
    board = np.array(board, dtype="<U14")
    for key, value in candyPeople.items():
        board[value] = key
    return board

class Deck():
    
    def __init__(self):
        self.colors = ['Red', 'Purple', 'Yellow', 'Blue', 'Orange', 'Green']
        self.candyPeople = ['Plumpy', 'Mr. Mint', 'Jolly', 'Gramma Nutt', 'Princess Lolly', 'Queen Frostine']
        
        self.deck = []
        self.discard = []
        
        self.buildDeck()
        self.shuffleDeck()
        
    def buildDeck(self):
        for color in self.colors:
            for i in range(6):
                self.deck.append((color, 1))
            for i in range(4):
                self.deck.append((color, 2))
        for char in self.candyPeople:
            self.deck.append(('Pink', char))

    def shuffleDeck(self):
        random.shuffle(self.deck)
        random.shuffle(self.deck)
        random.shuffle(self.deck)
        
    def reshuffleDeck(self):
        self.deck = self.discard
        self.discard = []
        self.shuffleDeck()
        
    def isEmpty(self):
        return len(self.deck) == 0
    
    def drawCard(self):
        if self.isEmpty():
            self.reshuffleDeck()
        card = self.deck.pop()
        self.discard.append(card)
        return card 

class Player():
    def __init__(self, name):
        self.name = name
        self.pos = -1
        
    def printCard(self, card):
        if card[1] == 1:
            print(f'{self.name}: You drew a single {card[0]}! Advance to the next {card[0]}!')
        elif card[1] == 2:
            print(f'{self.name}: You drew a double {card[0]}! Advance two {card[0]}s!')
        else:
            print(f'{self.name}: You drew the {card[1]} card! Go to {card[1]}!')
            
        
    def move(self, card, board):
        if card[0] == 'Pink':
            self.pos = np.where(board == card[1])[0][0]
            print(f'Your new position is {self.pos}!')
            return
        spaces = np.where(board == card[0])[0]
        for i in range(card[1]):
            if np.any(spaces > self.pos):
                self.pos = spaces[np.argmax(spaces > self.pos)]
            else:
                self.pos = len(board)
        print(f'Your new position is {self.pos}!')
        return 

def findPlayers():
    characters = []
    numChars = int(input('How many players (2-4)? '))
    for i in range(numChars):
        name = input(f"Player {i + 1} name? ")
        characters.append(Player(name))
    return characters

def instructions():
    print("Welcome to Candyland. Reach the last space of the board before anybody else does.")
    print("Draw a card to advance.")
    print("Press ENTER to start each player's turn")
    print()
    print('----------------------------------------------------------------')
    print()

def main():
    instructions()
    deck = Deck()
    board = createBoard()
    characters = findPlayers()
    while characters:
        for character in characters:
            print()
            print(f'{character.name}: It is your turn')
            input()
            card = deck.drawCard()
            character.printCard(card)
            character.move(card, board)
            if character.pos == len(board):
                print(f'Congratulations {character.name}, you won!')
                return 

if __name__ == "__main__":
    main()