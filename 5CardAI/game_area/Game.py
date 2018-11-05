'''
Created on 3 Nov 2018

@author: mdunn
'''
class Game:
    
    def __init__(self, dealer):
        self.dealer = dealer;
        
    def sitPlayer(self, player):
        self.dealer.seatPlayer(player);
        
    def startGame(self):
        self.dealer.go()