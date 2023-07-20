https://www.codingninjas.com/studio/problems/build-min-heap_1171167?leftPanelTab=0
from os import *
from sys import *
from collections import *
from math import *

def minheap(heap,i,n):

    L = 2*i+1
    R = 2*i+2

    if L < n and heap[i] > heap[L]:
        smallest = L
    else:
        smallest = i

    if R < n and heap[smallest] > heap[R]:
        smallest = R

    if smallest != i:
        heap[smallest],heap[i] = heap[i],heap[smallest]
        minheap(heap,smallest,n)

    return    




def buildMinHeap(arr):
    n=len(arr)
    if(n==0 or n==1):
        return arr

    for i in range(n//2-1,-1,-1):
        minheap(arr,i,n)
    return arr    