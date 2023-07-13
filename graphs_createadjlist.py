https://www.codingninjas.com/studio/problems/create-a-graph-and-print-it_1214551
from os import *
from sys import *
from collections import *
from math import *

def printAdjacency(n, m, edges):
    adj={}
    for i in range(m):
        u=edges[i][0]
        v=edges[i][1]
        
        if u not in adj:
            adj[u]=[]
            adj[u].append(u)
            adj[u].append(v)
            a=adj[u][0]
            adj[u]=adj[u][1:]
            adj[u].sort()
            adj[u].insert(0,a) 
 


        else:
            adj[u].append(v)
            a=adj[u][0]
            adj[u]=adj[u][1:]
            adj[u].sort()
            adj[u].insert(0,a)
  
            
        if v not in adj:
            adj[v]=[]
            adj[v].append(v)
            adj[v].append(u)
            a=adj[v][0]
            adj[v]=adj[v][1:]
            adj[v].sort()
            adj[v].insert(0,a)  
        
        else:
            adj[v].append(u)
            a=adj[v][0]
            adj[v]=adj[v][1:]
            adj[v].sort()
            adj[v].insert(0,a)
        
    while (len(adj)!=n):
        for i in range(n):
            if i not in adj:
                adj[i]=[]
                adj[i].append(i)


    return adj