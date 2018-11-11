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

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
    
    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented
    
    def __ge__(self, other):
        if self.__class__ is other.__class__:
            if self.value > other.value:
                return True
            else:
                return self.value == other.value
        return NotImplemented
    
    def __le__(self, other):
        if self.__class__ is other.__class__:
            if self.value < other.value:
                return True
            else:
                return self.value == other.value
        return NotImplemented


class Number(Enum):
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
    QUEEN = 12
    KING = 13
    ACE = 14

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
    
    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented
    
    def __ge__(self, other):
        if self.__class__ is other.__class__:
            if self.value > other.value:
                return True
            else:
                return self.value == other.value
        return NotImplemented
    
    def __le__(self, other):
        if self.__class__ is other.__class__:
            if self.value < other.value:
                return True
            else:
                return self.value == other.value
        return NotImplemented

class Card:

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __str__(self):
        return str(self.number) + " " + str(self.suit)

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.number < other.number
        return NotImplemented

    def __le__(self, other):
        if self.__class__ is other.__class__:
            if self.number < other.number:
                return True
            elif self.number == other.number:
                return self.suit < other.suit
            else:
                return False
        return NotImplemented
    
    def __ge__(self, other):
        if self.__class__ is other.__class__:
            if self.number > other.number:
                return True
            elif self.number == other.number:
                return self.suit > other.suit
            else:
                return False
        return NotImplemented
    
    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.number > other.number
        return NotImplemented