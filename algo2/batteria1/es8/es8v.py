grafo1 = [[1],[0,2,3],[1,4],[1,4],[2,3,5],[4]]
visitati = [0] * len(grafo1)

def es8_2v(grafo: list[list[int]],nodoCorrente:int):
    if visitati[nodoCorrente] == 1:
        return
    else:
        visitati[nodoCorrente] = 1
        for nextNodo in grafo[nodoCorrente]:
            if nodoCorrente in grafo[nextNodo]:
                if visitati[nextNodo] == 1:
                    grafo[nodoCorrente].remove(nextNodo)
                else:
                    grafo[nextNodo].remove(nodoCorrente)
            if visitati[nextNodo] == 0:
                return es8_2v(grafo,nextNodo)
        return    
    