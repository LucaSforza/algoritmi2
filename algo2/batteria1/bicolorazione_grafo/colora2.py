

def colora2(nodo:int,G:list[list[int]],colorati:list[list[int]],c:int)->bool:
    colorati[nodo]=c
    for nextNodo in G[nodo]:
        if colorati[nextNodo] == -1:
            if not colora2(nextNodo,G,colorati,1-c): return False
        elif colorati[nextNodo] == c:
            return False
    return True



if __name__ == '__main__':
    grafo1 = [[1],[0,2,3],[1,4],[1,4],[2,3,5],[4]]
    colorati = [-1]*len(grafo1)
    if colora2(0,grafo1,colorati,0) : print(colorati)    
    else : print([])