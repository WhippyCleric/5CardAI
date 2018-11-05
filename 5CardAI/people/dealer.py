'''
Created on 3 Nov 2018

@author: mdunn
'''
from game_area.table import Table
from cards.deck import Deck
class Dealer:
    
    def __init__(self):
        self.table = Table(2);
        self.deck = Deck();
        
    def seatPlayer(self, player):
        self.table.seatPlayer(player);
        
    def go(self):
        print("Game is starting");