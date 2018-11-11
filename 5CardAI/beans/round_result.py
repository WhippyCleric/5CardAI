'''
Created on 9 Nov 2018

@author: mdunn
'''


class RoundResult:
    
    def __init__(self, hand_results):
        self.hand_results = hand_results
        
    def find_winning_hands(self):
        winning_hands = [self.hand_results[0]]
        for hand in self.hand_results[1:]:
            if hand.hand_value > winning_hands[0].hand_value:
                winning_hands = [hand]
            elif hand.hand_value == winning_hands[0].hand_value:
                winning_hands.append(hand)
        return winning_hands