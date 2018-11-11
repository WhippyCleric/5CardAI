'''
Created on 11 Nov 2018

@author: mdunn
'''
import unittest
from cards.card import Card
from cards.card import Number
from cards.card import Suit
from beans.hand_result import HandResult, HandType


class HandResultTest(unittest.TestCase):

    def test_flush_check(self):
        suit = Suit.DIAMONDS
        card = Card(Number.ACE, suit)
        card1 = Card(Number.TWO, suit)
        card2 = Card(Number.TEN, suit)
        card3 = Card(Number.KING, suit)
        card4 = Card(Number.JACK, suit)
        flush = [card, card1, card2, card3, card4]
        flush_result = HandResult(flush)
        self.assertTrue(flush_result.hand_type == HandType.FLUSH, "Expected Flush")
        
    def test_straight_check(self):
        suit = Suit.DIAMONDS
        suit1 = Suit.CLUBS
        card = Card(Number.FOUR, suit)
        card1 = Card(Number.TWO, suit1)
        card2 = Card(Number.THREE, suit)
        card3 = Card(Number.SIX, suit1)
        card4 = Card(Number.FIVE, suit)
        straight = [card, card1, card2, card3, card4]
        straight_result = HandResult(straight)
        self.assertTrue(straight_result.hand_type == HandType.STRAIGHT, "Expected Straight")
        
    def test_straight_check_ace_begin(self):
        suit = Suit.DIAMONDS
        suit1 = Suit.CLUBS
        card = Card(Number.FOUR, suit)
        card1 = Card(Number.TWO, suit1)
        card2 = Card(Number.THREE, suit)
        card3 = Card(Number.ACE, suit1)
        card4 = Card(Number.FIVE, suit)
        straight = [card, card1, card2, card3, card4]
        straight_result = HandResult(straight)
        self.assertTrue(straight_result.hand_type == HandType.STRAIGHT, "Expected Straight")
        
    def test_straight_check_ace_end(self):
        suit = Suit.DIAMONDS
        suit1 = Suit.CLUBS
        card = Card(Number.JACK, suit)
        card1 = Card(Number.TEN, suit1)
        card2 = Card(Number.QUEEN, suit)
        card3 = Card(Number.ACE, suit1)
        card4 = Card(Number.KING, suit)
        straight = [card, card1, card2, card3, card4]
        straight_result = HandResult(straight)
        self.assertTrue(straight_result.hand_type == HandType.STRAIGHT, "Expected Straight")
        
    def test_straight_flush(self):
        suit = Suit.DIAMONDS
        card = Card(Number.JACK, suit)
        card1 = Card(Number.TEN, suit)
        card2 = Card(Number.QUEEN, suit)
        card3 = Card(Number.ACE, suit)
        card4 = Card(Number.KING, suit)
        straight_flush = [card, card1, card2, card3, card4]
        straight_flush_result = HandResult(straight_flush)
        self.assertTrue(straight_flush_result.hand_type == HandType.STRAIGHT_FLUSH, "Expected Straight Flush")
        
    def test_pair(self):
        suit = Suit.DIAMONDS
        suit1 = Suit.CLUBS
        card = Card(Number.QUEEN, suit)
        card1 = Card(Number.TEN, suit)
        card2 = Card(Number.QUEEN, suit1)
        card3 = Card(Number.FIVE, suit1)
        card4 = Card(Number.JACK, suit1)
        pair = [card, card1, card2, card3, card4]
        pair_result = HandResult(pair)
        self.assertTrue(pair_result.hand_type == HandType.PAIR, "Expected Pair")
        
    def test_two_pair(self):
        suit = Suit.DIAMONDS
        suit1 = Suit.CLUBS
        card = Card(Number.QUEEN, suit)
        card1 = Card(Number.TEN, suit)
        card2 = Card(Number.QUEEN, suit1)
        card3 = Card(Number.TEN, suit1)
        card4 = Card(Number.JACK, suit1)
        two_pair = [card, card1, card2, card3, card4]
        two_pair_result = HandResult(two_pair)
        self.assertTrue(two_pair_result.hand_type == HandType.TWO_PAIR, "Expected Two Pair")
        
    def test_high_card(self):
        suit = Suit.DIAMONDS
        suit1 = Suit.CLUBS
        card = Card(Number.QUEEN, suit)
        card1 = Card(Number.TEN, suit)
        card2 = Card(Number.FIVE, suit1)
        card3 = Card(Number.THREE, suit1)
        card4 = Card(Number.JACK, suit1)
        high_card = [card, card1, card2, card3, card4]
        high_card_result = HandResult(high_card)
        self.assertTrue(high_card_result.hand_type == HandType.HIGH_CARD, "Expected High Card")
        
    def test_three_of_a_kind(self):
        suit = Suit.DIAMONDS
        suit1 = Suit.CLUBS
        three_of_a_kind = [Card(Number.ACE, suit), Card(Number.ACE, suit1), Card(Number.ACE, Suit.SPADES), Card(Number.THREE, suit), Card(Number.TWO, suit1)]
        three_of_a_kind_result = HandResult(three_of_a_kind)
        self.assertTrue(three_of_a_kind_result.hand_type == HandType.TRIPS, "Expected Trips")
        
    def test_full_house(self):
        suit = Suit.DIAMONDS
        suit1 = Suit.CLUBS
        card = Card(Number.THREE, suit)
        card1 = Card(Number.TEN, suit)
        card2 = Card(Number.TEN, suit1)
        card3 = Card(Number.THREE, suit1)
        card4 = Card(Number.TEN, Suit.HEARTS)
        full_house = [card, card1, card2, card3, card4]
        full_house_result = HandResult(full_house)
        self.assertTrue(full_house_result.hand_type == HandType.FULL_HOUSE, "Expected Full House")
        
    def test_four_of_a_kind(self):
        suit = Suit.DIAMONDS
        suit1 = Suit.CLUBS
        card = Card(Number.TEN, Suit.SPADES)
        card1 = Card(Number.TEN, suit)
        card2 = Card(Number.TEN, suit1)
        card3 = Card(Number.THREE, suit1)
        card4 = Card(Number.TEN, Suit.HEARTS)
        four_of_a_kind = [card, card1, card2, card3, card4]
        four_of_a_kind_result = HandResult(four_of_a_kind)
        self.assertTrue(four_of_a_kind_result.hand_type == HandType.QUADS, "Expected Quads")
        
if __name__ == '__main__':
    unittest.main()
