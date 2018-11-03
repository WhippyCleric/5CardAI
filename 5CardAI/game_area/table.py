'''
Created on 3 Nov 2018

@author: mdunn
'''
from game_area.seat import Seat;

class Table:
    
    seats = []
    
    def __init__(self, numberOfSeats):
         for i in numberOfSeats:
            self.seats.append(Seat(i))