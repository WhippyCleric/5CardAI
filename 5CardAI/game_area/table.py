'''
Created on 3 Nov 2018

@author: mdunn
'''
from game_area.seat import Seat
from cardai_exceptions.no_free_seat import NoFreeSeatException


class Table(object):

    def __init__(self, number_of_seats):
        self.seats = []
        for i in range(number_of_seats):
            self.seats.append(Seat(i))

    def seat_player(self, player):
        freeSeat = self.find_free_seat()
        if freeSeat is not None:
            freeSeat.seat_player(player)
        else:
            raise NoFreeSeatException()

    def _find_free_seat(self):
        for seat in self.seats:
            if seat.is_free:
                return seat
        return None

    def print_state(self):
        for seat in self.seats:
            print("Seat: ")
            seat.print_state()
