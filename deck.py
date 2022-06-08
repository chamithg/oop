import random

#! OOP create some classes to represent 52 card deck
# aces through kings(aces, jacks , queens, kings), four standerd suits (hearts, diamonds, spades,clubs)

class Card:  # this is the list of cards, card has a suit and value, so it will be a dictionary
    def __init__(self, suit, value):
        self.suit = suit
        # self.value = value            ## method 1 if statement
        # if value == 1:
        #     self.rank = "Ace"
        # elif value == 11:
        #     self.rank = "Jack"
        # elif value == 12:
        #     self.rank = "Queen"
        # if value == 13:
        #     self.rank = "King"
        # else:
        #     self.rank = str(value)
    
        rank_conversion = {1:"Ace",11:"jack",12:"Queen", 13:"king"}      # method 2 if statement
    
        if value in rank_conversion:
            self.rank = rank_conversion[value]
        else:
            self.rank = str(value)
            
        
    
    def __str__(self):        #! __str__ use to return the user readable value
        return self.rank + " of "+  self.suit
    
    def __repr__(self):       #! __repr__ use to return the programmer friendly representation.
        return self.rank + " of "+  self.suit



class DeckOfCards:
    def __init__ (self):
        # what properties does a deck of card have?.
        self.content = [] # this is the list of cards, card has a suit and value, so it will be a dictionary
        
        suits = ["heart", "diamonds", "spades", "clubs"]
        values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        
        for suit in suits:
            for value in values:
                self.content.append(Card(suit, value))
                
        self.shuffle_deck()
        
    def shuffle_deck(self):    
        #random.shuffle(self.content)        #!-------> shuffle method 1      
        
        for i in range(0, len(self.content)):     #!-------> shuffle method 2      
            x = random.randint(0, len(self.content)-1)
            self.content[i], self.content[x] = self.content[x], self.content[i]       
    
    def draw_card(self):
        if len(deck.content) != 0:
            return deck.content.pop() 
        else:
            pass
    


deck = DeckOfCards()

player_a = []
player_b = []

for i in range(0,51):
    player_a.append(deck.draw_card())
    player_b.append(deck.draw_card())
    
print(player_a)
print(player_b)
    