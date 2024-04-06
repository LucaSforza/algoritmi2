from draw import draw

def dfs(grafo:list[list[int]],currNodo:int,padre:int,visitati:list[int],grafOut:list[list[int]]):
    visitati[currNodo]=1
    for adiNodo in grafo[currNodo]:
        if visitati[adiNodo]==0:
            dfs(grafo,adiNodo,currNodo,visitati,grafOut)
        elif visitati[adiNodo]==1:
            grafOut[currNodo].append(adiNodo)
    return 


def es4f(grafo:list[list[int]]):
    visitati = [0]*len(grafo)
    grafOut = [[] for _ in range(len(grafo))]
    dfs(grafo,0,0,visitati,grafOut)




esempio=[[3,4],[2,3,4,5],[1,4,5],[0,1],[0,1,2],[1,2]]

draw(esempio)