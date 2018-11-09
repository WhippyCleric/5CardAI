'''
Created on 3 Nov 2018

@author: mdunn
'''


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def give_cards(self, cards):
        self.hand = cards

    def print_state(self):
        print("Name: " + self.name)
        print("Hand: ")
        for card in self.hand:
            print(card.__str__())
