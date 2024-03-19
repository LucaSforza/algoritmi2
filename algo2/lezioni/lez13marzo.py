
from collections import deque
esempio1 = [[5,8,3,4],[2,7],[1,6],[0,4,7,8],[0,3],[0,8],[2],[3,1,2],[0,3,5]]

def BFSlista(nodo,grafo): #O(N^2)
    V = [0]*len(grafo)
    V[nodo]=1
    coda = [nodo]
    while coda != []:
        x = coda.pop(0)
        for newNodo in grafo[x]:
            if V[newNodo]==0:
                V[newNodo]=1
                coda.append(newNodo)
    return V

def BFScoda(nodo,grafo): #O(n+m)
    V = [0]*len(grafo)
    V[nodo]=1
    coda = deque([nodo])
    i = 0
    while len(coda)>i:
        x = coda.popleft()
        i+=1
        for newNodo in grafo[x]:
            if V[newNodo]==0:
                V[newNodo]=1
                coda.append(newNodo)
    return V

def BFSpadri(nodo,grafo): #O(n+m)
    P = [0]*len(grafo)
    P[nodo]=1
    coda = [nodo]
    while len(coda)>i:
        x = coda[i]
        for newNodo in grafo[x]:
            if P[newNodo]==-1:
                P[newNodo]=1
                coda.append(newNodo)
    return P






