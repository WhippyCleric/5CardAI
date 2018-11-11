'''
Created on 9 Nov 2018

@author: mdunn
'''
import random


class RandomActionCollector():

    def collect_action(self, player):
        cards_to_draw = random.randint(0, 4)
        cards_to_throw_away = []
        for i in range(cards_to_draw):
            index = random.randint(0, 4)
            while cards_to_throw_away.__contains__(index):
                index = random.randint(0, 4)
            cards_to_throw_away.append(index)
        return cards_to_throw_away
    
    def tell_result(self, round_result):
        pass