https://www.codingninjas.com/studio/problems/sort-a-stack_985275
from os import *
from sys import *
from collections import *
from math import *

def sortStack(stack):
    if (len(stack)==0):
        return stack
    stack=stack.sort()
    return stack    