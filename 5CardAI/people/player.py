'''
Created on 3 Nov 2018

@author: mdunn
'''
class Player:
    
    def __init__(self, name):
        self.name = name;
        self.hand = [];
        
    def giveCards(self, cards):
        self.hand = cards;