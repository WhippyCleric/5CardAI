'''
Created on 5 Nov 2018

@author: mdunn
'''
from people.dealer import Dealer
from people.player import Player

def collectActions(dealer):
    for seat in dealer.table.seats:
        if not seat.isFree:
            seat.player.printState()
            action = input("Which cards would you like to change?");
            print(action);

dealer = Dealer();
player1 = Player("Player1");
player2 = Player("Player2");
dealer.seatPlayer(player1);
dealer.seatPlayer(player2);
dealer.deal();
collectActions(dealer);