'''
Created on 3 Nov 2018

@author: mdunn
'''
class NoFreeSeatException(Exception):
    def __init__(self):
        super().__init__("There are no free seats at the table, unable to seat player")
