'''
Created on 3 Nov 2018

@author: mdunn
'''
from game_area.table import Table
from cards.deck import Deck
from beans.hand_result import HandResult
from beans.round_result import RoundResult


class Dealer:

    def __init__(self):
        self.table = Table(2)
        self.deck = Deck()

    def seat_player(self, player):
        self.table.seat_player(player)

    def go(self):
        print("Game is starting")
        self._deal()

    def deal(self):
        self.deck.reset()
        seats = self.table.seats
        for seat in seats:
            if not seat.is_free:
                seat.player.clear_hand()
                hand = []
                for i in range(5):
                    seat.player.give_card(self.deck.draw_card())

    def _printGameState(self):
        self.table.print_state()

    def process_actions(self):
        for seat in self.table.seats:
            if not seat.is_free:
                seat.player.print_state()
                action = seat.player.collect_action()
                seat.player.take_cards(action)
                for i in range(len(action)):
                    seat.player.give_card(self.deck.draw_card())
                seat.player.print_state()

    
    def declare_winner(self):
        hands = []
        for seat in self.table.seats:
            if not seat.is_free:
                hands.append(HandResult(seat.player.hand, seat.player))
        round_result = RoundResult(hands)
        winning_hands = round_result.find_winning_hands()
        
        for seat in self.table.seats:
            if not seat.is_free:
                seat.player.tell_result(round_result)
        
        print("Round Winner(s)!: ")
        for winning_hand in winning_hands:
            print(winning_hand.player.name + " " + str(winning_hand.hand_type))