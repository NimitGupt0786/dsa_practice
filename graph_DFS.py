https://www.codingninjas.com/studio/problems/dfs-traversal_630462
from collections import deque
def bfs(adj, src, visited, ans):
    q = deque()
    q.append(src)
    visited.add(src)

    while (len(q) > 0):
        curr = q.pop()   #if pop(means stack) is used dfs and if popleft(means queue) is used bfs
        ans.append(curr)
        for i in adj[curr]:
            if i not in visited:
                q.append(i)
                visited.add(i)

    while (len(visited) != len(adj)):
        for i in adj:
            if i not in visited:
                bfs(adj, i, visited, ans)

    return ans


def BFS(vertex, edges):
    adj = {}
    for i in range(len(edges)):
        u = edges[i][0]
        v = edges[i][1]

        if u not in adj:
            adj[u] = []
            adj[u].append(v)


        else:
            adj[u].append(v)


        if v not in adj:
            adj[v] = []
            adj[v].append(u)


        else:
            adj[v].append(u)


    while (len(adj) != vertex):
        for j in range(vertex):
            if j not in adj:
                adj[j] = []

    # for i in range(len(adj)):
    #     adj[i].sort()
    print(adj)

    ans = []
    visited = set()
    return bfs(adj, 0, visited, ans)

vertex=5
edges=[
[2, 0],
[1 ,0],
[3, 1],
]
print(BFS(vertex,edges))