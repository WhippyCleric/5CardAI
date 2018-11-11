'''
Created on 9 Nov 2018

@author: mdunn
'''


class ManualActionCollector():

    def collect_action(self, player):
        action =  input("Which cards would you like to change? (csv)")
        if action is not None and action is not "":
            return list(map(lambda index: int(index), action.split(",")))
        else:
            return []

    def tell_result(self, round_result):
        pass