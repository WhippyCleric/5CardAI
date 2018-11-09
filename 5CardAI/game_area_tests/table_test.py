'''
Created on 3 Nov 2018

@author: mdunn
'''
import unittest
from game_area.table import Table
from people.player import Player
from cardai_exceptions.no_free_seat import NoFreeSeatException


class TableTest(unittest.TestCase):

    def test_construction(self):
        table = Table(2)
        number_of_seats = table.seats.__len__()
        self.assertEqual(2, number_of_seats, "Expected a table with 2 seats")

    def test_seat_player(self):
        table = Table(2)
        table.seat_player(Player("Player1"))
        self.assertFalse(table.seats[0].is_free)

    def test_seat_too_many_players(self):
        table = Table(2)
        table.seat_player(Player("Player1"))
        table.seat_player(Player("Player2"))
        self.assertRaises(NoFreeSeatException, table.seat_player, Player("Player3"))


if __name__ == '__main__':
    unittest.main()
