https://www.codingninjas.com/studio/problems/quick-sort_983625
from os import *
from sys import *
from collections import *
from math import *

def partion(arr):
    pivot=arr[0]
    count=0
    for k in range(1,len(arr)):
        if pivot >= arr[k]:
            count += 1

    arr[count],arr[0]=arr[0],arr[count]

    i=0
    j=len(arr)-1
    while(i<count and j>count):
        if arr[i]>=pivot and arr[j]<=pivot:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1

        elif arr[i]<=pivot:
            i+=1

        elif arr[j]>=pivot:
            j-=1

    return count,arr

def quickSort(arr):
    if len(arr)<=1:
        return arr

    p,arr=partion(arr)
    return quickSort(arr[:p]) + [arr[p]] + quickSort(arr[p+1:])