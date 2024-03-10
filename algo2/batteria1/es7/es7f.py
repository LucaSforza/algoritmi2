def ricerca(grafo:list[list[int]], nodoCorrente,lastNodeVisited, visitati:list[int], counterComponenti:int,isAlbero:bool=True):
    visitati[nodoCorrente] = counterComponenti
    isAlberor = True
    for nodo in grafo[nodoCorrente]:
        if visitati[nodo]!=0 and (lastNodeVisited==None or nodo!=lastNodeVisited):
            isAlbero = False
        if visitati[nodo]==0:
            isAlberor,visitati = ricerca(grafo,nodo,nodoCorrente,visitati,counterComponenti)
        isAlbero = isAlbero and isAlberor
            
    return isAlbero,visitati

def es7f(grafo:list[list[int]],nodoPartenza=0)->int:
    nAlberi = 0
    visitati = [0]*len(grafo)
    counterComponenti = 0        
    for i in range(len(visitati)):
        if visitati[i] == 0:
            counterComponenti+=1
            isAlbero,visitati = ricerca(grafo,i,None, visitati,counterComponenti)
            if isAlbero:
                nAlberi+=1
    return nAlberi

print(es7f([[13],[2,3],[1,3],[1,2],[5,11,7],[4],[],[4],[9],[8],[11],[10,4],[13,14],[12,15,0],[12,15],[14,13]]))