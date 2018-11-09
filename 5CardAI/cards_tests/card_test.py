'''
Created on 30 Sep 2018

@author: mdunn
'''
import unittest
from cards.card import Card


class TestCard(unittest.TestCase):

    def test_construction(self):
        sixOFDiamonds = Card(6, "DIAMONDS")
        self.assertEqual(sixOFDiamonds.__str__(), '6 DIAMONDS')


if __name__ == '__main__':
    unittest.main()
