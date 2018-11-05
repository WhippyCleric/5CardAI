'''
Created on 3 Nov 2018

@author: mdunn
'''
class Seat:
    
    def __init__(self, number):
        self.number = number;
        self.player = None;
        self.isFree = True;
    
    def seatPlayer(self, player):
        self.isFree = False;
        self.player = player;
        
    def printState(self):
        print("Number: " + str(self.number));
        print("Player: ");
        self.player.printState();