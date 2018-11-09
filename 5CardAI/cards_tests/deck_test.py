'''
Created on 6 Oct 2018

@author: mdunn
'''
import unittest
from cards.deck import Deck
from cardai_exceptions.out_of_cards import OutOfCardsException


class DeckTest(unittest.TestCase):

    def test_deck_creation(self):
        deck = Deck()
        for i in range(52):
            deck.drawCard()
        with self.assertRaises(OutOfCardsException) as context:
            deck.drawCard()


if __name__ == '__main__':
    unittest.main()
