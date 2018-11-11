'''
Created on 3 Nov 2018

@author: mdunn
'''
from beans import round_result


class Player:

    def __init__(self, name, action_collector):
        self.name = name
        self.hand = []
        self.action_collector = action_collector

    def collect_action(self):
        return self.action_collector.collect_action(self)

    def give_card(self, card):
        self.hand.append(card)

    def clear_hand(self):
        self.hand = []

    def take_cards(self, card_indexes):
        for index in sorted(card_indexes, reverse=True):
            self.hand.pop(index)
            
    def tell_result(self, round_result):
        self.action_collector.tell_result(round_result)

    def print_state(self):
        print("Name: " + self.name)
        print("Hand: ")
        for card in self.hand:
            print(card.__str__())
