'''
Created on 9 Nov 2018

@author: mdunn
'''
from enum import Enum
from cards.card import Number
import copy


class HandType(Enum):
    HIGH_CARD = 0
    PAIR = 1000000
    TWO_PAIR = 2000000
    TRIPS = 3000000
    STRAIGHT = 4000000
    FLUSH = 5000000
    FULL_HOUSE = 6000000
    QUADS = 7000000
    STRAIGHT_FLUSH = 8000000


class HandResult():


    def __init__(self, cards):
        self.cards = cards
        self._order_cards()
        self.hand_type = self._deduce_hand_type(cards)
        self.hand_value = self._deduce_hand_value(cards, self.hand_type)

    def _deduce_hand_value(self, cards, hand_type):
        value = hand_type.value
        if hand_type == HandType.HIGH_CARD:
            value = value + self._high_card_value(cards)
        if hand_type == HandType.PAIR:
            value = value + self._pair_value(cards)
        if hand_type == HandType.TWO_PAIR:
            value = value + self._two_pair_value(cards)
        if hand_type == HandType.TRIPS:
            value = value + self._trips_value(cards)
        if hand_type == HandType.STRAIGHT:
            value = value + self._straight_value(cards)
        if hand_type == HandType.FLUSH:
            value = value + self._high_card_value(cards)
        if hand_type == HandType.FULL_HOUSE:
            value = value + self._trips_value(cards)
        if hand_type == HandType.QUADS:
            value = value + self._trips_value(cards)
        if hand_type == HandType.STRAIGHT_FLUSH:
            value = value + self._straight_value(cards)
        return value
    
    def _straight_value(self, cards):
        value = 0
        power = 4
        if cards[4].number == Number.ACE and cards[0].number == Number.TWO:
            #Unique case for Ace through 5 straight
            card_to_iterate = cards[:-1]
            for card in reversed(card_to_iterate):
                value = value + pow(14,power)*card.number.value
                power = power - 1
            value = value + 1
        else:
            for card in reversed(cards):
                value = value + pow(14,power)*card.number.value
                power = power - 1
        
        return value

    def _trips_value(self, cards):
        trips = self._find_trips(cards)
        return trips[0].number.value

    def _two_pair_value(self, cards):
        value = 0
        cards_clone = copy.deepcopy(cards)
        pair1 = self._find_pair(cards_clone)
        pair1_value = pair1[0].number.value
        for card in pair1:
            cards_clone.remove(card)
        pair2 = self._find_pair(cards_clone)
        pair2_value = pair2[0].number.value
        for card in pair2:
            cards_clone.remove(card)
        if pair1_value > pair2_value:
            value = 14*14*pair1_value
            value = value + 14*pair2_value
        else:
            value = 14*14*pair2_value
            value = value + 14*pair1_value
            
        value = value + cards_clone[0].number.value
        return value
    
    def _pair_value(self, cards):
        cards_clone = copy.deepcopy(cards)
        pair = self._find_pair(cards_clone)
        pair_value = pair[0].number.value
        for card in pair:
            cards_clone.remove(card)
        value = pow(14,3)*pair_value
        power = 2
        for card in reversed(cards_clone):
            value = value + pow(14,power)*card.number.value
            power = power - 1
        return value
        
    def _find_pair(self, cards):
        previous_card = cards[0]
        for card in cards[1:]:
            if previous_card.number == card.number:
                return [previous_card, card]
            previous_card = card
        return None

    
    def _find_trips(self, cards):
        previous_card = cards[0]
        trips = []
        for card in cards[1:]:
            if previous_card.number == card.number:
                if len(trips) == 0:
                    trips = [previous_card, card]
                else:
                    trips.append(card)
                    return trips
            previous_card = card
        return None
    
    def _high_card_value(self, cards):
        value = 0
        power = 4
        for card in reversed(cards):
            value = value + pow(14,power)*card.number.value
            power = power - 1
        return value

    def _deduce_hand_type(self, cards):
        hand_type = self._check_for_sets(cards)
        
        if hand_type == HandType.HIGH_CARD: 
            if self._check_if_flush(cards):
                if self._check_if_straight(cards):
                    return HandType.STRAIGHT_FLUSH
                return HandType.FLUSH
            
            if self._check_if_straight(cards):
                return HandType.STRAIGHT
        
        return hand_type
    
    def _check_if_flush(self, cards):
        first_suit = cards[0].suit;
        for card in cards:
            if first_suit is not card.suit:
                return False
        return True
    
    def _check_if_straight(self, cards):
        first_card = cards[0]
        for card in cards[1:]:
            if card.number.value != first_card.number.value + 1:
                if card.number != Number.ACE:
                    return False
                else:
                    return cards[0].number == Number.TWO
            first_card = card
        return True
    
    def _check_for_sets(self, cards):
        previous_card = cards [0]
        current_count = 1
        hand_type = HandType.HIGH_CARD
        for card in cards[1:]:
            if card.number == previous_card.number:
                current_count = current_count +1
            else:
                hand_type = self._check_count(current_count, hand_type)
                current_count = 1
            previous_card = card
        return self._check_count(current_count, hand_type)

    def _check_count(self, count, hand_type):
        if count == 4:
            hand_type = HandType.QUADS
        if count == 3:
            if hand_type == HandType.PAIR:
                hand_type = HandType.FULL_HOUSE
            else:
                hand_type = HandType.TRIPS
        if count == 2:
            if hand_type == HandType.PAIR:
                hand_type = HandType.TWO_PAIR
            elif hand_type == HandType.TRIPS:
                hand_type = HandType.FULL_HOUSE
            else:
                hand_type = HandType.PAIR
        return hand_type

    def _order_cards(self):
        quickSort(self.cards)
            
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first<last:
        splitpoint = partition(alist,first,last)

        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
           done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    
    return rightmark