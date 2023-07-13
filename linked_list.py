https://www.codingninjas.com/studio/problems/merge-two-sorted-linked-lists_800332
from math import *
from collections import *
from sys import *
from os import *

import sys
from sys import stdin


class Node
    def __init__(self, data):
        self.data = data
        self.next = None
      
def sortTwoLists(first, second):

    if first == None and second == None:
        return None

    if first == None :
        return second

    if second == None :
        return first
    
    myhead=None

    if first.data <= second.data:
        myhead=first
        first=first.next

    else:
        myhead= second
        second=second.next

    curr=myhead

    while(first != None and second != None):

        if first.data >= second.data:   
            curr.next= second
            second=second.next
            curr=curr.next

        else:
            curr.next = first
            first=first.next
            curr=curr.next 
                      
    if second == None:
        curr.next=first

    if first == None:
        curr.next = second

    return myhead 