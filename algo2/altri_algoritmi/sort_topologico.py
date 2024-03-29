from typing import Optional

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

# esercizio slide 5
def orienta_alcuni(G: list[tuple[list[int],list[int]]]) -> list[list[int]]:
    pass

if __name__ == '__main__':
    print(sorgenti(G))
    print(sort_dfs(G))