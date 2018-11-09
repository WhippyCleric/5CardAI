'''
Created on 5 Nov 2018

@author: mdunn
'''
from people.dealer import Dealer
from people.player import Player
from action.manual_action_collector import ManualActionCollector

dealer = Dealer()
player1 = Player("Player1", ManualActionCollector())
dealer.seat_player(player1)
dealer.deal()
dealer.process_actions()
