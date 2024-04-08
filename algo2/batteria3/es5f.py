

def tarjan(grafo,nodo,visitati,stack,minDist)->int:
    visitati[nodo]=1
    minDist[nodo]=nodo
    stack.append(nodo)
    for adiNodo in grafo[nodo]:
        if visitati[adiNodo]==0:
            tarjan(grafo,adiNodo,visitati,stack,minDist)
            minDist[adiNodo]=min(minDist[nodo],minDist[adiNodo])
        elif adiNodo in stack:
            minDist[adiNodo]=min(minDist[nodo],minDist[adiNodo])
        
    return 

def es5f(grafo)->list[list[int]]:
    indice = 0 
    stack = []
    nNodi = len(grafo)
    minDist = [nNodi+1]*nNodi
    visitati = [0]*nNodi
    for nodo in range(len(grafo)):
        if visitati[nodo]==0:
            tarjan(grafo,nodo,visitati,stack,minDist)
