grafo1 = [[1],[3],[1,4],[4],[2,3],[4]]
grafo2 = [[1],[2],[3],[0]]
visitati = [0]*len(grafo2)
def es82f(grafo:list[list[int]],nodo:int):
    if visitati[nodo]==1:
        return 
    else:
        visitati[nodo]=1
        for arco in grafo[nodo]:
            if nodo in grafo[arco] and arco in grafo[nodo]:
                if arco in visitati:
                    grafo[arco].remove(nodo)
                else:
                    grafo[arco].remove(nodo)
            else:
                es82f(grafo,arco)

es82f(grafo2,0) 
print(grafo2)




