'''
Created on 3 Nov 2018

@author: mdunn
'''


class NoFreeSeatError(Exception):

    def __init__(self):
        message = "There are no free seats at the table, unable to seat player"
        super().__init__(message)
