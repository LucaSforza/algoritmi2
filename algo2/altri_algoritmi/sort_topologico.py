from typing import Optional
from draw import draw

G = [
    [1,5,6],
    [2,6],
    [],
    [2,4,6],
    [5,6],
    [],
    [2,5]
]

def sorgenti(G: list[list[int]]) -> Optional[list[int]]:
    # prima mi calcolo sorgenti
    C = [0]*len(G)
    for u in range(len(G)): # O(n+m)
        for v in G[u]:
            C[v] += 1
    S = [u for u in range(len(C)) if C[u] == 0] # O(n)
    ST = []
    # per ogni sorgente la tolgo dalla lista S e l'aggiungo al sort topologico e mi calcolo altre eventuali sorgenti
    while S: # eseguito O(n) volte
        s = S.pop()
        ST.append(s)
        for v in G[s]: # O(m_s) dove m_s è il numero di archi uscenti da s
            C[v] -= 1
            if C[v] == 0:
                S.append(v)
    # in totale questo algoritmo è O(n+m)
    if len(ST) == len(G):
        return ST
    return None

def sort_dfs(G: list[list[int]]) -> Optional[list[int]]:
    def DFSr(u: int, G: list[list[int]],V: list[int], list_out: list[int]):
        V[u] = 1
        for v in G[u]:
            if V[v] == 0:
                DFSr(v,G,V,list_out)
        list_out.append(u)
    list_out = []
    V = [0] * len(G)
    for u in range(len(G)):
        if V[u] == 0:
            DFSr(u,G,V,list_out)
    list_out.reverse()
    return list_out

G1 = [
    ([],[2,3]),
    ([0,3],[2]),
    ([],[0,1,4]),
    ([2],[0]),
    ([],[2])
]

grafo_parz_orientato = list[tuple[list[int],list[int]]]

# esercizio slide 5
def orienta_alcuni(G: grafo_parz_orientato) -> list[list[int]]:
    def sort_top(G: grafo_parz_orientato) -> list[int]:
        from collections import deque
        V = [0]*len(G)
        for u in range(len(G)):
            for y,_ in zip(*G[u]):
                V[y] += 1
        S = [u for u in range(len(G)) if V[u] == 0]
        S = deque(S)
        ST = []
        while S:
            u = S.popleft()
            ST.append(u)
            for y,_ in zip(*G[u]):
                V[y] -= 1
                if V[y] == 0:
                    S.append(y)
        return ST
    def DFSr(u: int, V: list[int], G: grafo_parz_orientato,out: list[list[int]], sort: list[int]):
        V[u] = 1
        A,B = G[u]
        for y in A:
            out[u].append(y)
            if V[y] == 0:
                DFSr(y,V,G,out,sort)
        for y in B:
            if sort[u] < sort[y]:
                out[u].append(y)
            else:
                out[y].append(u)
            if V[y] == 0:
                DFSr(y,V,G,out,sort)

    sort = sort_top(G) # O(n+m)
    sort_value = [-1]*len(G)
    for i,u in enumerate(sort):
        sort_value[u] = i
    out = [[] for _ in range(len(G))]
    V = [0]*len(G)
    for u in range(len(G)):
        if V[u] == 0:
            DFSr(u,V,G,out,sort_value)
    return out

if __name__ == '__main__':
    print(sorgenti(G))
    print(sort_dfs(G))
    draw(orienta_alcuni(G1),direct=True)