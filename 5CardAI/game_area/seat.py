'''
Created on 3 Nov 2018

@author: mdunn
'''


class Seat:

    def __init__(self, number):
        self.number = number
        self.player = None
        self.is_free = True

    def seat_player(self, player):
        self.is_free = False
        self.player = player

    def print_state(self):
        print("Number: " + str(self.number))
        print("Player: ")
        if not self.is_free:
            self.player.print_state()
