def DFSf(grafo:list[list[int]],nodo:int,visitati,sortOut:list[int]):
    visitati[nodo] = 1
    for nodoArrivo in grafo[nodo]:
        if visitati[nodoArrivo]==0:

            visitati,sortOut = DFSf(grafo,nodoArrivo,visitati,sortOut)
            sortOut.append(nodo)
    return visitati,sortOut

def sortTopologico(grafo:list[list[int]])->list[int]:
    sortOut = list()
    visitati = [0]*len(grafo)
    for nodo in range(len(grafo)):
        if visitati[nodo]==0:
            visitati,sortOut = DFSf(grafo,nodo,visitati,sortOut)
    return sortOut

# versione prof
def DFSp(u,G,V,lista=[]):
    V[u]=1
    for y in G[u]:
        if V[y]==0:
            DFSp(y,G,V,lista)
            lista.append(u)
    return lista

def sortT(G:list[list[int]]):
    V = [0]*len(G)
    for i in range(len(G)):
        if V[i]==0:
            lista = DFSp(i,G,V)
    return lista

graf = [[1,5,6],[2,6],[],[6,2,4],[5,6],[],[2,5]]
print(sortT(graf))
print(sortTopologico(graf))


def DFSc(u,G,V):
    V[u]=1
    for y in G[u]:
        if V[u]==1 :return True
        if V[y]==0:
            if DFSc(y,G,V): return False
    V[u]=2 #per falo 
    return False

def haCicli(u,G):
    V = [0]*len(G)
    if DFSc(u,G,V):return True
    return False