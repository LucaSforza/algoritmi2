from math import inf


def dijkstra(s, G): # O(n^2)
    '''restituisce il vettore delle distanze D e l'albero dei cammini minimi rappresentato tramite vettore dei padri p'''
    Inserito=[False] * len(G)
    Lista = [(inf, -1)] * len(G)
    Lista[s], Inserito[s] = (0, s), True
    for y, costo in G[s]:
        Lista[y] = (costo, s)
    while True:
        minimo = inf
        for i in range(len(Lista)):
            if not Inserito[i] and Lista[i][0] < minimo:
                minimo, x = Lista[i][0], i
        if minimo == inf: break
        Inserito[x] = True
        for y, costo in G[x]:
            if not Inserito[y] and minimo + costo < Lista[y][0]:
                Lista[y] = (minimo + costo, x)
    D = [costo for costo, _ in Lista]
    P = [padre for _, padre in Lista]
    return P, D


G = [
    [(1,17), (5, 4)],
    [(0,17), (4, 5), (5,6)],
    [(3, 12), (4,10)],
    [(2, 12), (4,4) , (5,1)],
    [ (1,5), (2,10), (3,4)],
    [(0,4), (1,6), (3,1)],
]

print(dijkstra(0,G))