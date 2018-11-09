'''
Created on 3 Nov 2018

@author: mdunn
'''


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def give_card(self, card):
        self.hand.append(card)

    def clear_hand(self):
        self.hand = []

    def take_cards(self, card_indexes):
        for index in sorted(card_indexes, reverse=True):
            self.hand.pop(index)

    def print_state(self):
        print("Name: " + self.name)
        print("Hand: ")
        for card in self.hand:
            print(card.__str__())
