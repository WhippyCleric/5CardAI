'''
Created on 5 Nov 2018

@author: mdunn
'''
from people.dealer import Dealer
from people.player import Player
from game_area.game import Game

dealer = Dealer();
player1 = Player("Player1");
player2 = Player("Player2");
game = Game(dealer);
game.seatPlayer(player1);
game.seatPlayer(player2);
game.startGame();