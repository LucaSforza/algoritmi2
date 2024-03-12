def componenti(G:list[list[int]]):
    
        def DFSr(nodo:int,G:list[list[int]],componenti:list[int],id_componente:int):
            componenti[nodo] = id_componente
            for nextNodo in G[nodo]:
                if componenti[nextNodo] == 0:
                    DFSr(nextNodo,G,componenti,id_componente)
                    
        ###           
        componenti = [0]*len(G)
        id_componente = 0
        for nodo in range(len(G)):
            if componenti[nodo] == 0:
                id_componente += 1
                DFSr(nodo,G,componenti,id_componente)
        return componenti
    
if __name__ == '__main__':
    grafo1 = [[1,5],[0,5],[4],[],[2],[0,1]]
    print(componenti(grafo1))
    