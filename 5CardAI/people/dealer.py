'''
Created on 3 Nov 2018

@author: mdunn
'''
from game_area.table import Table
from cards.deck import Deck


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
                hand = []
                for i in range(5):
                    seat.player.give_card(self.deck.draw_card())

    def _printGameState(self):
        self.table.print_state()

    def process_actions(self, actions):
        for player in actions:
            player.take_cards(actions[player])
            for i in range(len(actions[player])):
                player.give_card(self.deck.draw_card())
        self._printGameState()
