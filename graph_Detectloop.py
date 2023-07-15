https://www.codingninjas.com/studio/problems/cycle-detection-in-undirected-graph_1062670?leftPanelTab=1
from collections import deque
def bfs(adj, src, visited, parent,n):
    if n==1:
        return 'No'
        
    parent[src] = -1
    q = deque()
    q.append(src)
    visited.add(src)


    while (len(q) > 0):
        curr = q.popleft()   #if pop(means stack) is used dfs and if popleft(means queue) is used bfs
        for i in adj[curr]:
            if i in visited and parent[curr]!=i:
                return 'Yes'
            elif i not in visited:
                q.append(i)
                visited.add(i)
                parent[i]=curr

    for i in adj:
        if i not in visited:
            return bfs(adj, i, visited, parent,n)

    return 'No'

def BFS(n, edges,src):
    adj = {}
    for u, v in edges:
        adj.setdefault(u, []).append(v)
        adj.setdefault(v, []).append(u)


    for j in range(n):
        if j not in adj:
            adj[j] = []


    parent = [-1] * (n + 1)
    visited = set()
    return bfs(adj, src, visited,parent,n)

def cycleDetection(edges, n, m):
    return (BFS(n,edges,1))
