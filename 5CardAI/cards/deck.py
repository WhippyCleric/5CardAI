'''
Created on 6 Oct 2018

@author: mdunn
'''
from cards.card import Card
from random import shuffle
from cardai_exceptions.out_of_cards import OutOfCardsException
class Deck:
    cards = []
    suits = ["DIAMONDS", "CLUBS", "HEARTS", "SPADES"]

    def __init__(self):
        self.__createCards()
        
    def __createCards(self):
        for suit in self.suits:
            self.__cerateSuit(suit)
        shuffle(self.cards)
            
    def __cerateSuit(self, suit):
        for i in range(13):
            self.cards.append(Card(i, suit))
            
    def drawCard(self):
        if len(self.cards) > 0 :
            return self.cards.pop(0)
        else:
            raise OutOfCardsException()