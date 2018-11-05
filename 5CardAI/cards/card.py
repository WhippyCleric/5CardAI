'''
Created on 23 Sep 2018

@author: mdunn
'''
from enum import Enum

class Suit(Enum):
    CLUBS = 1
    HEARTS = 2
    DIAMONDS = 3
    SPADES = 4
    
class Number(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEENS = 12
    KING = 13

class Card:

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
        
    def __str__(self):
        return str(self.number) + " " + str(self.suit)