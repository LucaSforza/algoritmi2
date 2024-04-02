from collections import deque
from math import inf
from draw import draw

G = [
    [1,3,4],
    [0,2],
    [1,3,4],
    [0,2,4],
    [0,2,3],
]

def bfs(G: list[list[int]],s: int) -> list[int]:
    D = [inf]*len(G)
    
    d = deque()
    d.append(s)
    D[s] = 0
    while d:
        u = d.popleft()
        for v in G[u]:
            if D[v] == inf:
                d.append(v)
                D[v] = D[u] + 1
    return D

if __name__ == '__main__':
    print(bfs(G,1))
    draw(G)