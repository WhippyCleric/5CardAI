'''
Created on 3 Nov 2018

@author: mdunn
'''
class Seat:
    
    number = -1;
    player = None;
    isFree = True;
    
    def __init__(self, number):
        self.number = number;
    
    def seatPlayer(self, player):
        self.isFree = False;
        self.player = player;