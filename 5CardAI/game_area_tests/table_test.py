'''
Created on 3 Nov 2018

@author: mdunn
'''
import unittest
from game_area.table import Table;

class TableTest(unittest.TestCase):
    
    def testConstruction(self):
        table = Table(2);
        self.assertEqual(2, table.seats.__len__(), "Expected a table with 2 seats");
        
        
if __name__ == '__main__':
    unittest.main()