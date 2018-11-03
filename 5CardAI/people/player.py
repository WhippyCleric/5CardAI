'''
Created on 3 Nov 2018

@author: mdunn
'''
class Player:
    
    hand = [];
    name = "";
    
    def __init__(self, name):
        self.name = name;
        
    def giveCards(self, cards):
        self.hand = cards;