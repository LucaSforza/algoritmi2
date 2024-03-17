def sortT(G:list[list[int]]):
    visitati = [0]*len(G)
    lista = []
    for nodo in range(len(G)):
        if visitati[nodo] == 0:
            DFSr(nodo,G,visitati,lista)
    lista.reverse()
    return lista


def DFSr(nodo:int,G:list[list[int]],visitati:list[int],lista:list):
    visitati[nodo] = 1
    for nextNodo in G[nodo]:
        if visitati[nextNodo] == 0:
            DFSr(nextNodo,G,visitati,lista)
    lista.append(nodo)
    
if __name__ == '__main__':
    grafo1 = [[1,4,5],[2],[3],[4],[],[2],[2]]
    print(sortT(grafo1))
    