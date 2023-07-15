https://www.codingninjas.com/studio/problems/topological-sort_982938
from collections import deque
def topologicalsort(adj, src, visited,stack):

        visited.add(src)
        print(src)


        for k in adj[src]:
            if k not in visited:
                topologicalsort(adj, k, visited,stack)
        stack.append(src)
        return


def BFS(vertex, edges):
    adj = {}
    for u,v in edges:
        adj.setdefault(u, []).append(v)

    for j in range(1,vertex+1):
        if j not in adj:
            adj[j] = []

    print(adj)

    stack = deque()
    visited = set()

    for i in range(1,vertex+1):
        if i not in visited:
            topologicalsort(adj, i, visited,stack)

    ans=[]

    while(len(stack)!=0):
        curr=stack.pop()
        ans.append(curr)
    return ans


vertex=6

edges=[
[1, 2],
[1 ,3],
[2, 4],
    [3,4],
    [4,5],
    [4,6],
    [5,6]
]
print(BFS(vertex,edges))