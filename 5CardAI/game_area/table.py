'''
Created on 3 Nov 2018

@author: mdunn
'''
from game_area.seat import Seat;
from cardai_exceptions.no_free_seat import NoFreeSeatException;
class Table:
    
    seats = []
    
    def __init__(self, numberOfSeats):
         
        for i in range(numberOfSeats):
            self.seats.append(Seat(i));
            
            
    def seatPlayer(self, player):
        freeSeat = self.findFreeSeat();
        if freeSeat != None:
            freeSeat.seatPlayer(player);
        else:
            raise NoFreeSeatException();
        
    def findFreeSeat(self):
        for seat in self.seats:
            if seat.isFree:
                return seat;
        return None;