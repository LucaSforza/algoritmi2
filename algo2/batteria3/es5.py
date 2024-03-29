from draw import draw

# calcola il grafo complenetare di un grafo DIRETTO con complessità O(n+m)
def grafo_complementare(G: list[list[int]]) -> list[list[int]]:
    list_out = [[] for _ in range(len(G))]

    for u in range(len(G)):
        for v in G[u]:
            list_out[v].append(u)

    return list_out
            

def tarjan(AL: list[list[int]]) -> list[int]:

    def calculate_sink_SCC(u: int, V: list[int],L: list[list[int]], list_out: list[int]) -> None:
        V[u] = 1
        for v in L[u]:
            if V[v] == 0:
                calculate_sink_SCC(v,V,L,list_out)
        list_out.append(u)

    def DFSr(u: int,V:list[int],c: int,L: list[list[int]]):
        V[u] = c
        for v in L[u]:
            if V[v] == -1:
                DFSr(v,V,c,L)

    compl = grafo_complementare(AL) # O(n+m)

    V = [0]*len(AL) # O(n)
    nodes = []
    for u in range(len(AL)):
        if V[u] == 0:
            calculate_sink_SCC(u,V,compl,nodes) # O(n+m)
    nodes.reverse() # O(n)

    V = [-1]*len(AL) # O(n)
    count = 0

    for u in nodes: # O(n+m)
        if V[u] == -1:
            DFSr(u,V,count,AL)
            count += 1
    return V

G = [
    [16],
    [0,2],
    [8],
    [7],
    [3,5,6],
    [7],
    [5,11],
    [4,9,13],
    [0],
    [14],
    [],
    [12],
    [11],
    [10],
    [15,17],
    [9],
    [1,4],
    [9]
]

def es5(G: list[list[int]]) -> list[list[int]]:
    
    def DFSr(u: int, G: list[list[int]], V: list[int], CFS: list[int], list_out: list[list[int]]):
        V[u] = 1
        for v in G[u]:
            if V[v] == 0:
                if CFS[u] != CFS[v]:
                    list_out[CFS[u]].append(CFS[v])
                DFSr(v,G,V,CFS,list_out)

    CFS = tarjan(G) # O(n+m)
    print(CFS)
    nCFS = max(CFS) + 1 # O(n)
    list_out = [[] for _ in range(nCFS)] # O(n)
    V = [0 for _ in range(len(G))] # O(n)
    for u in range(len(G)):
        if V[u] == 0:
            DFSr(u,G,V,CFS,list_out)
    return list_out

if __name__ == '__main__':
    draw(es5(G),direct=True)