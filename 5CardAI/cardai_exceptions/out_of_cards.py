'''
Created on 7 Oct 2018

@author: mdunn
'''


class OutOfCardsException(Exception):

    def __init__(self):
        super().__init__("Attempted to draw a card from an empty deck!")
