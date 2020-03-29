#!/usr/bin/env python
# coding: utf-8

# In[8]:


import random
from IPython.display import Image 
from PIL import Image                                                                               

# Global
handValue = []
dealerValue = []
autoWin = 21
cardValues = {}
fullDeck =[]
valueCheck = {}
cardTypes = []
drawCard =""

#Global card setup
cardTypes = ['Hearts','Spades','Clubs','Diamonds']
cardValues = {'Ace':1,'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10, 'Queen':10,'King':10}

# Global value check
for cardNums in cardValues:
    for cardFace in cardTypes:
        valueCheck.update({cardNums + " of " + cardFace : cardValues[cardNums]})


# In[9]:


imageDict = {'Ace of Hearts': 'AH.png',
             'Ace of Spades': 'AS.png',
             'Ace of Clubs': 'AC.png',
             'Ace of Diamonds': 'AD.png',
             'Two of Hearts' : '2H.png',
             'Two of Spades' : '2S.png',
             'Two of Clubs' : '2C.png',
             'Two of Diamonds' : '2D.png',
             'Three of Hearts' : '3H.png',
             'Three of Spades' : '3D.png',
             'Three of Clubs' : '3C.png',
             'Three of Diamonds' : '3D.png',
             'Four of Hearts' : '4H.png',
             'Four of Spades' : '4S.png',
             'Four of Clubs' : '4C.png',
             'Four of Diamonds' : '4D.png',
             'Five of Hearts' : '5H.png',
             'Five of Spades' : '5S.png',
             'Five of Clubs' : '5C.png',
             'Five of Diamonds' : '5D.png',
             'Six of Hearts': '6H.png',
             'Six of Spades' : '6S.png',
             'Six of Clubs' : '6C.png',
             'Six of Diamonds' : '6D.png',
             'Seven of Hearts' : '7H.png',
             'Seven of Spades' : '7S.png',
             'Seven of Clubs' : '7C.png',
             'Seven of Diamonds' : '7D.png',
             'Eight of Hearts' : '8H.png',
             'Eight of Spades' : '8S.png',
             'Eight of Clubs' : '8C.png',
             'Eight of Diamonds' : '8D.png',
             'Nine of Hearts' : '9H.png',
             'Nine of Spades' : '9S.png',
             'Nine of Clubs' : '9C.png',
             'Nine of Diamonds' : '9D.png',
             'Ten of Hearts' : '10H.png',
             'Ten of Spades' : '10S.png',
             'Ten of Clubs' : '10C.png',
             'Ten of Diamonds' : '10D.png',
             'Jack of Hearts' : 'JH.png',
             'Jack of Spades' : 'JD.png',
             'Jack of Clubs' : 'JC.png',
             'Jack of Diamonds' : 'JD.png',
             'Queen of Hearts' : 'QH.png',
             'Queen of Spades' : 'QS.png',
             'Queen of Clubs' : 'QC.png',
             'Queen of Diamonds': 'QD.png',
             'King of Hearts' : 'KH.png',
             'King of Spades' :'KS.png',
             'King of Clubs' : 'KC.png',
             'King of Diamonds' : 'KD.png'
            }


# In[10]:


# Card class and functions of the game
class cards:
    def __init__ (self, cardTypes, cardValues, fullDeck, fresh, valueCheck, draw, handValue, dealerValue):
        self.cardTypes = cardTypes
        self.cardValues = cardValues
        self.fullDeck = fullDeck
        self.fresh = fresh
        self.valueCheck = valueCheck
        self.draw = draw
        self.handValue = handvalue
        self.dealerValue = dealerValue
        self.endGame = endGame
    
    endGame = False
     
    for cardNums in cardValues:
        for cardFace in cardTypes:
            fullDeck.append(cardNums + " of " + cardFace)
    
    def playerHand():
        handValue.append(cards.value)
    
    def dealerHand():
        dealerValue.append(cards.value)
        
    def fresh():
        cards.fullDeck = random.sample(fullDeck,52)
        
    def drawCard():
        cards.draw = cards.fullDeck.pop()
    
    def valueCheck():
        cards.value = valueCheck[cards.draw]
        
    def statusCheck():
        if sum(handValue) > 21 or sum(dealerValue) > 21:
            cards.endGame = True
            if sum(handValue) > 21:
                print('Player bust!')
            else:
                print('Dealer bust, you win!')
        elif sum(handValue) > 21 or sum(dealerValue) == 21:
            cards.endGame = True
            if sum(handValue) == 21:
                print('Player has Blackjack!')
            else:
                print('Dealer has Blackjack!')
                


# In[11]:


cards.fresh()
cards.statusCheck()


# In[12]:


while cards.endGame == False:
    response = input('Would you like to draw a card?')
    if response.lower() in ['yes','y']:
        cards.drawCard()
        cards.valueCheck()
        cards.playerHand()
        print('Player draws a ' + cards.draw + ' for a hand value of ' + str(sum(handValue)))
        p1 = Image.open('/Users/juanpacheco/Desktop/Python/BlackJack/images/'+imageDict[cards.draw])
        display(p1.resize((150,180)))
        
        cards.drawCard()
        cards.valueCheck()
        cards.dealerHand()
        print('Dealer draws a ' + cards.draw + ' for a hand value of ' + str(sum(dealerValue)))
        cards.statusCheck()
        d1 = Image.open('/Users/juanpacheco/Desktop/Python/BlackJack/images/'+imageDict[cards.draw])
        display(d1.resize((150,180)))
        
    elif response.lower() in ['no','n']:
        print('Dealer will always hit')
        cards.drawCard()
        cards.valueCheck()
        cards.dealerHand()
        print('Dealer draws a ' + cards.draw + ' for a hand value of ' + str(sum(dealerValue)))
        cards.statusCheck()
        d1 = Image.open('/Users/juanpacheco/Desktop/Python/BlackJack/images/'+imageDict[cards.draw])
        display(d1.resize((150,180)))


# In[ ]:




