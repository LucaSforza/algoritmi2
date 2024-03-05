grafo = [[1],[3],[1,4],[4],[2,3],[4]]
visitati = [0]*len(grafo)
def es82f(grafo:list[list[int]],nodo:int)->bool:
    if nodo in visitati:
        return False
    else:
        visitati[nodo]=1
        for arco in grafo[nodo]:
            if nodo in grafo[arco]:
                
            else:
                es82f(grafo,arco)




