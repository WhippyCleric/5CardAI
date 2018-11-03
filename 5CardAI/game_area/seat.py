'''
Created on 3 Nov 2018

@author: mdunn
'''
class Seat:
    
    number = -1;
    player = None;
    
    def __init__(self, number):
        self.number = number;
    
    def seatPlayer(self, player):
        self.player = player;