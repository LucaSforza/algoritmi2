from draw import draw

# tuple del tipo: (nodo,peso)
G = [
[(1, 17), (5, 4)],
[(0, 17), (4, 5), (5, 6)],
[(3, 12), (4, 10)],
[(2, 12), (4, 4), (5, 1)],
[(1, 5), (2, 10), (3, 4)],
[(0, 4), (1, 6), (3, 1)]
]

from math import inf

# O(n^2)
def dijastra(G: list[list[tuple[int,int]]],s: int) -> tuple[list[int],list[int]]:
    Inserito = [False]*len(G) # O(n)
    Lista = [(inf,-1)]*len(G) # in Lista[i] ci sta il costo Lista[i][0] per andare in i dal padre List[i][1]
    Lista[s], Inserito[s] = (0,s),True
    for y,costo in G[s]:
        Lista[y] = (costo,s)
    while True:
        minimo = inf
        for i in range(len(Lista)): # eseguiro esattamente n volte
            if not Inserito[i] and Lista[i][0] < minimo:
                minimo, x = Lista[i][0], i
        if minimo == inf:
            break
        Inserito[x] = True
        for y, costo in G[x]:
            if not Inserito[y] and minimo + costo < Lista[y][0]:
                Lista[y] = (minimo + costo, x)
    D = [costo for costo,_ in Lista]
    P = [padre for _,padre in Lista]
    return P,D

# esercizi slide 9 
def es1(s: int,G: list[list[int]],P: list[bool]) -> list[int]:
    '''funzione che ritorna tutti i nodi irraggiongibili da s senza passare per nodi pericolosi'''
    def DFSr(u: int, G: list[list[int]], V: list[int]):
        V[u] = 1
        for v in G[u]:
            if V[v] == 0:
                DFSr(v,G,V)

    V = [0]*len(G) # contiene -1 se è pericoloso
    for p in P: # eseguito O(n) volte
        V[p] = -1
    DFSr(s,G,V) # O(n+m)
    return [u for u in range(len(G)) if V[u] == 0] # h(n)

# P è una lista di 0 o di 1, P[i] è 1 se e solo se il nodo 1 è pericoloso
def es2_v1(s: int, G: list[list[int]], P: list[int]) -> tuple[list[int],list[int]]:
    # in questa versione è l'agoritmo di dijastra leggermente modificato, quindi costa O(n^2)
    Inserito = [False]*len(G) # O(n)
    Lista = [(inf,-1)]*len(G) # in Lista[i] ci sta il costo Lista[i][0] per andare in i dal padre List[i][1]
    Lista[s], Inserito[s] = (0,s),True
    for y in G[s]:
        Lista[y] = (P[y],s)
    while True:
        minimo = inf
        for i in range(len(Lista)): # eseguiro esattamente n volte
            if not Inserito[i] and Lista[i][0] < minimo:
                minimo, x = Lista[i][0], i
        if minimo == inf:
            break
        Inserito[x] = True
        for y in G[x]:
            if not Inserito[y] and minimo + P[y] < Lista[y][0]:
                Lista[y] = (minimo + P[y], x)
    D = [costo for costo,_ in Lista]
    P = [padre for _,padre in Lista]
    return P,D

# questa implementazione è O(n+m)
def es2_v2(s: int, G: list[list[int]], P: list[int]) -> tuple[list[int],list[int]]:
    from collections import deque
    C = [-1]*len(G)
    Pa = [-1]*len(G)
    Pa[s], C[s] = s,0
    coda_per = deque()
    coda_nom = deque([s])
    while True:
        if coda_nom:
            to_pop = coda_nom
        elif coda_per:
            to_pop = coda_per
        else: break
        u = to_pop.popleft()
        for y in G[u]:
            if C[y] == -1:
                C[y] = C[u] + P[y]
                Pa[y] = u
                if P[y] == 0:
                    coda_nom.append(y)
                else:
                    coda_per.append(y)
    return Pa,C
        
G1 = [
    [1, 5],
    [0, 4, 5],
    [3, 4],
    [2,4,5],
    [1,2,3,6],
    [0, 1,3],
    [4]
]

if __name__ == '__main__':
    print(dijastra(G,0))
    print(es1(1,G1,[3,4]))
    print(es2_v1(1,G1,[0,0,0,0,1,0,0]))
    print(es2_v2(1,G1,[0,0,0,0,1,0,0]))
    draw(G1)
    
