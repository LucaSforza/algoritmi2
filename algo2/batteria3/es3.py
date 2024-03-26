from draw import *

Grafo = [
    [1], # 1 -> 2
    [2], # ...
    [3],
    [4],
    [5], # ...
    [0], # 6 -> 1
]

def grafo_quadrato(G: list[list[int]]) -> list[list[int]]:
    L = [[] for _ in range(len(G))]
    V = [0]*len(G)
    gqR(G, 0, len(G)-1, L, V)
    return L

def gqR(
    G: list[list[int]],
    u: int,
    p: int,
    L: list[list[int]],
    V: list[int],
):
    V[u] = 1
    for v in G[u]:
        L[p].append(v)
        L[u].append(v)
        if V[v] == 0:
            gqR(G,v,u,L,V)


if __name__ == '__main__':
    print(grafo_quadrato(Grafo))
    draw()