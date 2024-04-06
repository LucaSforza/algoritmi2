from draw import draw


def dfs(grafo:list[list[int]],nodoCorrente:int,padre:int,percorso:list[int],visitati:list[int]):
    visitati[nodoCorrente] = 1
    percorso.append(nodoCorrente)
    for adiNodo in grafo[nodoCorrente]:
        if visitati[adiNodo]==2:            
            #percorso.append(adiNodo)
            pass
        elif visitati[adiNodo]==1 and adiNodo!=padre:
            percorso.append(adiNodo)
            percorso.append(nodoCorrente)
            pass
        elif visitati[adiNodo]==0:
            dfs(grafo,adiNodo,nodoCorrente,percorso,visitati)
            visitati[adiNodo]=2
            percorso.append(nodoCorrente)

    return percorso

def es3f(grafo:list[list[int]],nodoPartenza:int)->list[int]:
    percorso = []
    visitati = [0]*len(grafo)
    percorsout = dfs(grafo,nodoPartenza,nodoPartenza,percorso,visitati)
    return percorsout


esempio = [[1,3],[0,2],[1,3,4],[0,2,4],[0,2,3]]
print(es3f(esempio,0))
draw(esempio)