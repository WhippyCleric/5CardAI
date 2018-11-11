'''
Created on 5 Nov 2018

@author: mdunn
'''
from people.dealer import Dealer
from people.player import Player
from action.manual_action_collector import ManualActionCollector
from action.random_action_collector import RandomActionCollector

dealer = Dealer()
player1 = Player("Player1", RandomActionCollector())
player2 = Player("Player2", RandomActionCollector())
dealer.seat_player(player1)
dealer.seat_player(player2)
for i in range(1000):
    dealer.deal()
    dealer.process_actions()
    dealer.declare_winner()