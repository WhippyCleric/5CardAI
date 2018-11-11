'''
Created on 9 Nov 2018

@author: mdunn
'''


class ManualActionCollector():

    def collect_action(self):
        action =  input("Which cards would you like to change? (csv)")
        return list(map(lambda index: int(index), action.split(",")))
