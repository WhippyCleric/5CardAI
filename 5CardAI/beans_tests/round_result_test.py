'''
Created on 11 Nov 2018

@author: mdunn
'''
import unittest
from cards.card import Card
from cards.card import Number
from cards.card import Suit
from beans.hand_result import HandResult, HandType
from beans.round_result import RoundResult
from people.player import Player
from action.manual_action_collector import ManualActionCollector


class RoundResultTest(unittest.TestCase):

    def test_high_card_comparison(self):
        player = Player("player", ManualActionCollector())
        player2 = Player("Player2", ManualActionCollector())
        suit = Suit.DIAMONDS
        suit1 = Suit.CLUBS
        hand1 = [Card(Number.ACE, suit), Card(Number.FOUR, suit), Card(Number.TWO, suit), Card(Number.THREE, suit), Card(Number.SIX, suit1)]
        hand2 = [Card(Number.KING, suit), Card(Number.QUEEN, suit), Card(Number.JACK, suit), Card(Number.TEN, suit), Card(Number.EIGHT, suit1)]
        round_result = RoundResult([HandResult(hand1, player), HandResult(hand2, player2)])
        winning_hand = round_result.find_winning_hands()[0].cards
        self.assertTrue(set(hand1).issubset(winning_hand))
        
    def test_high_card_pair_comparison(self):
        player = Player("player", ManualActionCollector())
        player2 = Player("Player2", ManualActionCollector())
        suit = Suit.DIAMONDS
        suit1 = Suit.CLUBS
        hand1 = [Card(Number.TWO, suit), Card(Number.TWO, suit1), Card(Number.THREE, suit), Card(Number.FOUR, suit), Card(Number.FIVE, suit1)]
        hand2 = [Card(Number.ACE, suit), Card(Number.KING, suit), Card(Number.QUEEN, suit), Card(Number.JACK, suit), Card(Number.NINE, suit1)]
        round_result = RoundResult([HandResult(hand1, player), HandResult(hand2, player2)])
        winning_hand = round_result.find_winning_hands()[0].cards
        self.assertTrue(set(hand1).issubset(winning_hand))
        
    def test_pair_comparison(self):
        player = Player("player", ManualActionCollector())
        player2 = Player("Player2", ManualActionCollector())
        suit = Suit.DIAMONDS
        suit1 = Suit.CLUBS
        hand1 = [Card(Number.THREE, suit), Card(Number.THREE, suit1), Card(Number.TWO, Suit.CLUBS), Card(Number.FOUR, suit), Card(Number.FIVE, suit1)]
        hand2 = [Card(Number.TWO, suit), Card(Number.TWO, suit1), Card(Number.KING, Suit.CLUBS), Card(Number.QUEEN, suit), Card(Number.ACE, suit1)]
        round_result = RoundResult([HandResult(hand1, player), HandResult(hand2, player2)])
        winning_hand = round_result.find_winning_hands()[0].cards
        self.assertTrue(set(hand1).issubset(winning_hand))

    def test_pair_two_pair_comparison(self):
        player = Player("player", ManualActionCollector())
        player2 = Player("Player2", ManualActionCollector())
        suit = Suit.DIAMONDS
        suit1 = Suit.CLUBS
        hand1 = [Card(Number.TWO, suit), Card(Number.TWO, suit1), Card(Number.THREE, suit), Card(Number.THREE, suit1), Card(Number.FOUR, suit1)]
        hand2 = [Card(Number.ACE, suit), Card(Number.ACE, suit1), Card(Number.KING, Suit.CLUBS), Card(Number.QUEEN, suit), Card(Number.JACK, suit1)]
        round_result = RoundResult([HandResult(hand1, player), HandResult(hand2, player2)])
        winning_hand = round_result.find_winning_hands()[0].cards
        self.assertTrue(set(hand1).issubset(winning_hand))
        
    def test_two_pair_comparison(self):
        player = Player("player", ManualActionCollector())
        player2 = Player("Player2", ManualActionCollector())
        suit = Suit.DIAMONDS
        suit1 = Suit.CLUBS
        hand1 = [Card(Number.TWO, suit), Card(Number.TWO, suit1), Card(Number.THREE, suit), Card(Number.ACE, suit), Card(Number.ACE, suit1)]
        hand2 = [Card(Number.KING, suit), Card(Number.KING, suit1), Card(Number.QUEEN, Suit.CLUBS), Card(Number.QUEEN, suit), Card(Number.JACK, suit1)]
        round_result = RoundResult([HandResult(hand1, player), HandResult(hand2, player2)])
        winning_hand = round_result.find_winning_hands()[0].cards
        self.assertTrue(set(hand1).issubset(winning_hand))

    def test_two_pair_trips_comparison(self):
        player = Player("player", ManualActionCollector())
        player2 = Player("Player2", ManualActionCollector())
        suit = Suit.DIAMONDS
        suit1 = Suit.CLUBS
        hand1 = [Card(Number.TWO, suit), Card(Number.TWO, suit1), Card(Number.TWO, suit.HEARTS), Card(Number.THREE, suit), Card(Number.FOUR, suit1)]
        hand2 = [Card(Number.KING, suit), Card(Number.KING, suit1), Card(Number.ACE, Suit.CLUBS), Card(Number.ACE, suit), Card(Number.JACK, suit1)]
        round_result = RoundResult([HandResult(hand1, player), HandResult(hand2, player2)])
        winning_hand = round_result.find_winning_hands()[0].cards
        self.assertTrue(set(hand1).issubset(winning_hand))

    def test_trips_comparison(self):
        player = Player("player", ManualActionCollector())
        player2 = Player("Player2", ManualActionCollector())
        suit = Suit.DIAMONDS
        suit1 = Suit.CLUBS
        hand1 = [Card(Number.ACE, suit), Card(Number.ACE, suit1), Card(Number.ACE, Suit.SPADES), Card(Number.THREE, suit), Card(Number.TWO, suit1)]
        hand2 = [Card(Number.KING, suit), Card(Number.KING, suit1), Card(Number.KING, Suit.SPADES), Card(Number.ACE, Suit.HEARTS), Card(Number.QUEEN, suit1)]
        round_result = RoundResult([HandResult(hand1, player), HandResult(hand2, player2)])
        winning_hand = round_result.find_winning_hands()[0].cards
        self.assertTrue(set(hand1).issubset(winning_hand))

    def test_trips_straight_comparison(self):
        player = Player("player", ManualActionCollector())
        player2 = Player("Player2", ManualActionCollector())
        suit = Suit.DIAMONDS
        suit1 = Suit.CLUBS
        hand1 = [Card(Number.ACE, Suit.SPADES), Card(Number.TWO, suit1), Card(Number.THREE, Suit.SPADES), Card(Number.FOUR, Suit.HEARTS), Card(Number.FIVE, suit1)]
        hand2 = [Card(Number.ACE, suit), Card(Number.ACE, suit1), Card(Number.ACE, Suit.SPADES), Card(Number.KING, suit), Card(Number.THREE, suit1)]
        round_result = RoundResult([HandResult(hand1, player), HandResult(hand2, player2)])
        winning_hand = round_result.find_winning_hands()[0].cards
        self.assertTrue(set(hand1).issubset(winning_hand))

    def test_straight_comparison(self):
        player = Player("player", ManualActionCollector())
        player2 = Player("Player2", ManualActionCollector())
        suit = Suit.DIAMONDS
        suit1 = Suit.CLUBS
        hand1 = [Card(Number.TWO, suit), Card(Number.THREE, suit1), Card(Number.FOUR, Suit.SPADES), Card(Number.FIVE, suit), Card(Number.SIX, suit1)]
        hand2 = [Card(Number.ACE, Suit.SPADES), Card(Number.TWO, suit1), Card(Number.THREE, Suit.SPADES), Card(Number.FOUR, Suit.HEARTS), Card(Number.FIVE, suit1)]
        round_result = RoundResult([HandResult(hand1, player), HandResult(hand2, player2)])
        winning_hand = round_result.find_winning_hands()[0].cards
        self.assertTrue(set(hand1).issubset(winning_hand))

    def test_straight_to_flush_comparison(self):
        player = Player("player", ManualActionCollector())
        player2 = Player("Player2", ManualActionCollector())
        suit = Suit.DIAMONDS
        suit1 = Suit.CLUBS
        hand1 = [Card(Number.TWO, suit), Card(Number.NINE, suit), Card(Number.FOUR, suit), Card(Number.FIVE, suit), Card(Number.SIX, suit)]
        hand2 = [Card(Number.ACE, Suit.SPADES), Card(Number.KING, suit1), Card(Number.QUEEN, Suit.SPADES), Card(Number.JACK, Suit.HEARTS), Card(Number.TEN, suit1)]
        round_result = RoundResult([HandResult(hand1, player), HandResult(hand2, player2)])
        winning_hand = round_result.find_winning_hands()[0].cards
        self.assertTrue(set(hand1).issubset(winning_hand))
        
    def test_flush_to_flush_comparison(self):
        player = Player("player", ManualActionCollector())
        player2 = Player("Player2", ManualActionCollector())
        suit = Suit.DIAMONDS
        suit1 = Suit.CLUBS
        hand1 = [Card(Number.ACE, suit), Card(Number.KING, suit), Card(Number.QUEEN, suit), Card(Number.JACK, suit), Card(Number.NINE, suit)]
        hand2 = [Card(Number.ACE, suit1), Card(Number.KING, suit1), Card(Number.QUEEN, suit1), Card(Number.JACK, suit1), Card(Number.EIGHT, suit1)]
        round_result = RoundResult([HandResult(hand1, player), HandResult(hand2, player2)])
        winning_hand = round_result.find_winning_hands()[0].cards
        self.assertTrue(set(hand1).issubset(winning_hand))
        
    def test_flush_to_full_house_comparison(self):
        player = Player("player", ManualActionCollector())
        player2 = Player("Player2", ManualActionCollector())
        suit = Suit.DIAMONDS
        suit1 = Suit.CLUBS
        hand1 = [Card(Number.TWO, suit1), Card(Number.TWO, Suit.HEARTS), Card(Number.TWO, suit), Card(Number.THREE, suit1), Card(Number.THREE, suit)]
        hand2 = [Card(Number.ACE, suit), Card(Number.KING, suit), Card(Number.QUEEN, suit), Card(Number.JACK, suit), Card(Number.NINE, suit)]
        round_result = RoundResult([HandResult(hand1, player), HandResult(hand2, player2)])
        winning_hand = round_result.find_winning_hands()[0].cards
        self.assertTrue(set(hand1).issubset(winning_hand))

    def test_full_house_to_full_house_comparison(self):
        player = Player("player", ManualActionCollector())
        player2 = Player("Player2", ManualActionCollector())
        suit = Suit.DIAMONDS
        suit1 = Suit.CLUBS
        hand1 = [Card(Number.ACE, suit1), Card(Number.ACE, Suit.HEARTS), Card(Number.ACE, suit), Card(Number.THREE, suit1), Card(Number.THREE, suit)]
        hand2 = [Card(Number.TWO, suit1), Card(Number.TWO, Suit.HEARTS), Card(Number.TWO, suit), Card(Number.KING, suit1), Card(Number.KING, suit)]
        round_result = RoundResult([HandResult(hand1, player), HandResult(hand2, player2)])
        winning_hand = round_result.find_winning_hands()[0].cards
        self.assertTrue(set(hand1).issubset(winning_hand))

    def test_full_house_to_quads_comparison(self):
        player = Player("player", ManualActionCollector())
        player2 = Player("Player2", ManualActionCollector())
        suit = Suit.DIAMONDS
        suit1 = Suit.CLUBS
        hand1 = [Card(Number.TWO, suit1), Card(Number.TWO, Suit.HEARTS), Card(Number.TWO, suit), Card(Number.TWO, Suit.SPADES), Card(Number.KING, suit)]
        hand2 = [Card(Number.ACE, suit1), Card(Number.ACE, Suit.HEARTS), Card(Number.ACE, suit), Card(Number.THREE, suit1), Card(Number.THREE, suit)]
        round_result = RoundResult([HandResult(hand1, player), HandResult(hand2, player2)])
        winning_hand = round_result.find_winning_hands()[0].cards
        self.assertTrue(set(hand1).issubset(winning_hand))

    def test_quads_to_quads_comparison(self):
        player = Player("player", ManualActionCollector())
        player2 = Player("Player2", ManualActionCollector())
        suit = Suit.DIAMONDS
        suit1 = Suit.CLUBS
        hand1 = [Card(Number.THREE, suit1), Card(Number.THREE, Suit.HEARTS), Card(Number.THREE, suit), Card(Number.THREE, Suit.SPADES), Card(Number.KING, suit1)]
        hand2 = [Card(Number.TWO, suit1), Card(Number.TWO, Suit.HEARTS), Card(Number.TWO, suit), Card(Number.TWO, Suit.SPADES), Card(Number.KING, suit)]
        round_result = RoundResult([HandResult(hand1, player), HandResult(hand2, player2)])
        winning_hand = round_result.find_winning_hands()[0].cards
        self.assertTrue(set(hand1).issubset(winning_hand))
        
    def test_quads_to_straight_flush_comparison(self):
        player = Player("player", ManualActionCollector())
        player2 = Player("Player2", ManualActionCollector())
        suit = Suit.DIAMONDS
        suit1 = Suit.CLUBS
        hand1 = [Card(Number.TWO, suit), Card(Number.THREE, suit), Card(Number.FOUR, suit), Card(Number.FIVE, suit), Card(Number.SIX, suit)]
        hand2 = [Card(Number.ACE, suit1), Card(Number.ACE, Suit.HEARTS), Card(Number.ACE, suit), Card(Number.ACE, Suit.SPADES), Card(Number.KING, suit1)]
        round_result = RoundResult([HandResult(hand1, player2), HandResult(hand2, player)])
        winning_hand_result = round_result.find_winning_hands()[0]
        winning_hand = winning_hand_result.cards
        self.assertTrue(set(hand1).issubset(winning_hand))
        self.assertEqual(player2, winning_hand_result.player, "Wrong Winning Player")

    def test_straight_flush_to_straight_flush_comparison(self):
        player = Player("player", ManualActionCollector())
        player2 = Player("Player2", ManualActionCollector())
        suit = Suit.DIAMONDS
        suit1 = Suit.CLUBS
        hand1 = [Card(Number.THREE, suit1), Card(Number.FOUR, suit1), Card(Number.FIVE, suit1), Card(Number.SIX, suit1), Card(Number.SEVEN, suit1)]
        hand2 = [Card(Number.TWO, suit), Card(Number.THREE, suit), Card(Number.FOUR, suit), Card(Number.FIVE, suit), Card(Number.SIX, suit)]
        round_result = RoundResult([HandResult(hand1, player), HandResult(hand2, player2)])
        winning_hand_result = round_result.find_winning_hands()[0]
        winning_hand = winning_hand_result.cards
        self.assertTrue(set(hand1).issubset(winning_hand))
        self.assertEqual(player, winning_hand_result.player, "Wrong Winning Player")

if __name__ == '__main__':
    unittest.main()
