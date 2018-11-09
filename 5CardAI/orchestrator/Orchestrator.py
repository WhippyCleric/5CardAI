'''
Created on 5 Nov 2018

@author: mdunn
'''
from people.dealer import Dealer
from people.player import Player


def collect_actions(dealer):
    actions = {}
    for seat in dealer.table.seats:
        if not seat.is_free:
            seat.player.print_state()
            action = input("Which cards would you like to change? (Space seperated)")
            actions[seat.player] = parse_action(action)
    return actions

def parse_action(action):
    return list(map(lambda index: int(index), action.split(",")))

dealer = Dealer()
player1 = Player("Player1")
#player2 = Player("Player2")
dealer.seat_player(player1)
#dealer.seat_player(player2)
dealer.deal()
actions = collect_actions(dealer)
dealer.process_actions(actions)