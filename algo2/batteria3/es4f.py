from draw import draw

def dfs(grafo:list[list[int]],currNodo:int,padre:int,visitati:list[int],grafOut:list[set[int]],finita):
    visitati[currNodo]=1
    for adiNodo in grafo[currNodo]:
        if visitati[adiNodo]==0:
            grafOut[currNodo].add(adiNodo)
            dfs(grafo,adiNodo,currNodo,visitati,grafOut,finita)
            finita[adiNodo]=True
        elif visitati[adiNodo]==1:
            if not finita[adiNodo]:
                grafOut[adiNodo].add(currNodo)
            
    return 


def es4f(grafo:list[list[int]]):
    visitati = [0]*len(grafo)
    grafOut = [set() for _ in range(len(grafo))]
    finita = [False for _ in range(len(grafo))]
    dfs(grafo,0,0,visitati,grafOut,finita)
    return [list(l) for l in grafOut]




esempio = [[2,3],[4,5],[0,3,4,5],[0,2,5],[1,2],[1,2,3]]
print(es4f(esempio))
draw(es4f(esempio),direct = True)
#draw(esempio)