'''
Created on 3 Nov 2018

@author: mdunn
'''
from game_area.table import Table
from cards.deck import Deck
class Dealer:
    
    def __init__(self):
        self.table = Table(2);
        
    def seatPlayer(self, player):
        self.table.seatPlayer(player);
        
    def go(self):
        print("Game is starting");
        self._deal();
        
    def deal(self):
        seats = self.table.seats;
        deck = Deck();
        for seat in seats:
            if not seat.isFree:
                hand = [];
                for i in range (5):    
                    hand.append(deck.drawCard())
                seat.player.giveCards(hand);
        
    def _printGameState(self):
        self.table.printState();