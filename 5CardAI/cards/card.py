'''
Created on 23 Sep 2018

@author: mdunn
'''
class Card:
    number = -1
    suit = "UNKNOWN"
    
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
        
    def __str__(self):
        return str(self.number) + " " + self.suit