'''
Created on 6 Oct 2018

@author: mdunn
'''
from cards.card import Card, Number, Suit
from random import shuffle
from cardai_exceptions.out_of_cards import OutOfCardsError


class Deck:

    def __init__(self):
        self.cards = []
        self._create_cards()

    def _create_cards(self):
        for suit in Suit:
            self._create_suit(suit)
        shuffle(self.cards)

    def _create_suit(self, suit):
        for number in Number:
            self.cards.append(Card(number, suit))

    def draw_card(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            raise OutOfCardsError()

    def reset(self):
        self.__init__()
