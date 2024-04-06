from copy import deepcopy
from draw import *

# usando liste di adiacenza 
def es2f(grafo:list[list[int]])->list[list[int]]: #H((n+m)^2)
    gQuadro = [[] for _ in range(len(grafo))]  
    for i,nodo in enumerate(grafo):
        for adiNodo in nodo: # H(n+m)
            gQuadro[i].append(adiNodo)
            for nodo in grafo[adiNodo]: # H(n+m)
                gQuadro[i].append(nodo)
    return gQuadro

# usando matrici di adiacenza 
def es2fmat(grafo:list[list[int]])->list[list[int]]: # H(n^3)
    gQuadro = [[] for _ in range(len(grafo))]  
    for inl,line in enumerate(grafo): # H(n)
        for ie,edge in enumerate(line): # H(n)
            if edge:
                gQuadro[inl].append(ie)
                for ieq,edgeq in enumerate(grafo[ie]): # H(n)
                    if edgeq:
                        gQuadro[inl].append(ieq)
    return gQuadro

matriceAdiacenza = [[0,1,0,0,0,0],
       [0,0,1,0,0,0],
       [0,0,0,1,0,0],
       [0,0,0,0,1,0],
       [0,0,0,0,0,1],
       [1,0,0,0,0,0]
       ]

listaAdiacenza = [[1],[2],[3],[4],[5],[0]]
daMatrice = es2fmat(matriceAdiacenza)
daLista = es2f(listaAdiacenza)
print(daMatrice)
print(daLista)
print(daLista==daMatrice)
