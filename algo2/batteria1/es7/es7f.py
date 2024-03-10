def ricerca(grafo:list[list[int]], nodoCorrente,lastNodeVisited, visitati:list[int], counterComponenti:int,isAlbero:bool=True)->bool,list[int]:
    visitati[nodoCorrente] = counterComponenti
    isAlberor = True
    for nodo in grafo[nodoCorrente]:
        if visitati[nodo]!=0 and nodo!=lastNodeVisited:
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

