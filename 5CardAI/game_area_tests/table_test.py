'''
Created on 3 Nov 2018

@author: mdunn
'''
import unittest
from game_area.table import Table
from people.player import Player
from cardai_exceptions.no_free_seat import NoFreeSeatException


class TableTest(unittest.TestCase):

    def testConstruction(self):
        table = Table(2)
        numberOfSeats = table.seats.__len__()
        self.assertEqual(2, numberOfSeats, "Expected a table with 2 seats")

    def testSeatPlayer(self):
        table = Table(2)
        table.seatPlayer(Player("Player1"))
        self.assertFalse(table.seats[0].isFree)

    def testSeatToManyPlayers(self):
        table = Table(2)
        table.seatPlayer(Player("Player1"))
        table.seatPlayer(Player("Player2"))
        self.assertRaises(NoFreeSeatException, table.seatPlayer, Player("Player3"))


if __name__ == '__main__':
    unittest.main()
