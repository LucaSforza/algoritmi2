from typing import Tuple

def ricerca(grafo:list[list[int]], nodoCorrente,lastNodeVisited, visitati:list[int],isAlbero:bool=True)-> Tuple[bool ,list[int]]:
    visitati[nodoCorrente] = 1
    isAlberor = True
    for nodo in grafo[nodoCorrente]:
        
        if visitati[nodo]==0:
            isAlberor = ricerca(grafo,nodo,nodoCorrente,visitati)
        elif  nodo!=lastNodeVisited:
            isAlbero = False
        isAlbero = isAlbero and isAlberor
            
    return isAlbero,visitati

def es7f(grafo:list[list[int]])->int:
    nAlberi = 0
    visitati = [0]*len(grafo)
    for i in range(len(grafo)):
        if visitati[i] == 0:
            isAlbero = ricerca(grafo,i,None, visitati)
            if isAlbero:
                nAlberi+=1
    return nAlberi

graf = [[1,2],[3],[3],[]]
print(es7f(graf))