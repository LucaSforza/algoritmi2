from draw import draw


def dfs(grafo,nodo,ids,low,stack,onStack,id):
    scc = 0
    stack.append(nodo)
    onStack[nodo]=True
    ids[nodo]=id
    low[nodo]=id
    id +=1
    for adi_nodo in grafo[nodo]:
        if ids[adi_nodo]==-1:
            scc+=dfs(grafo,adi_nodo,ids,low,stack,onStack,id)
        if onStack[adi_nodo]:
            low[nodo] = min(low[nodo],low[adi_nodo])
    if ids[nodo]==low[nodo]:
        for _ in range(len(grafo)):
            node = stack.pop()
            onStack[node] = False
            low[node]=ids[nodo]
            if node == nodo: break
        return scc+1
    return scc
    

def findScc(grafo,ids,low,stack,onStack,id):
    nSCC = 0
    for i in range(len(grafo)):
        if ids[i]==-1:
            nSCC+=dfs(grafo,i,ids,low,stack,onStack,id)
    
    return low

def es5(grafo):
    n = len(grafo)
    id = 0
    ids = [-1]*n
    low = [0]*n
    onStack = [False for _ in range(n)] 
    stack = []
    low = findScc(grafo,ids,low,stack,onStack,id)
    trad = dict()
    low_format = []
    ncomp = 0

    for comp in low:
        if comp in trad:
            low_format.append(trad[comp])
        else:
            trad[comp]=ncomp
            low_format.append(ncomp)
            ncomp+=1

    graf_conds = [[] for _ in range(ncomp)]
    for node,comp in enumerate(low_format):
        for edge in grafo[node]:
            if low_format[edge]!=comp:
                graf_conds[comp].append(low_format[edge])

    return graf_conds
            

    









esempio1 = [[16], #0
            [0,2],#1
            [8],#2
            [7],#3
            [3,5,6],#4
            [7],#5
            [5,11],#6
            [4,9,13],#7
            [0],#8
            [14],#9
            [],#10
            [12],#11
            [11],#12
            [10],#13
            [15,17],#14
            [9],#15
            [1,4],#16
            [9]#17
            ]

esempio2 = [[1],[2,3],[0],[4],[5],[3]]
esempio3 = [[1],[]]
esempio4 = [[1],[2],[1]]
esempio5 = [[1],[0],[0]]
esempio6 = [[1],[2],[3,4],[1],[1]]


draw(es5(esempio4),direct=True)
#draw(esempio1,direct = True)