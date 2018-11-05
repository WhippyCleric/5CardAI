'''
Created on 6 Oct 2018

@author: mdunn
'''
from cards.card import Card, Number, Suit
from random import shuffle
from cardai_exceptions.out_of_cards import OutOfCardsException
class Deck:
   

    def __init__(self):
        self.cards = []
        self.__createCards()
        
    def __createCards(self):
        for suit in Suit:
            self.__createSuit(suit)
        shuffle(self.cards)
            
    def __createSuit(self, suit):
        for number in Number:
            self.cards.append(Card(number, suit))
            
    def drawCard(self):
        if len(self.cards) > 0 :
            return self.cards.pop(0)
        else:
            raise OutOfCardsException()