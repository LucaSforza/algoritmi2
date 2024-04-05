from copy import deepcopy
from draw import *

def es2f(grafo:list[list[int]])->bool:
    gQuadro = [[] for _ in range(len(grafo))]  
    for i,nodo in enumerate(grafo):
        for adiNodo in nodo:

            gQuadro[i].append(adiNodo)
            for nodo in grafo[adiNodo]:
                gQuadro[i].append(nodo)
    return gQuadro


prova = [('a','b'),('b','c'),('c','a')]
esempio = [[1],[2],[3],[4],[5],[0]]
# print(es2f(esempio))
# draw(es2f(esempio),direct = True)

drawNetGraf(edgeListToNetGraf(prova))