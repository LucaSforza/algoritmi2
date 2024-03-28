G = [
    [1,2,5],
    [4],
    [3],
    [0,7],
    [5,6,7],
    [1,6],
    [],
    [6],
]

# ritorna in pos 0 archi in avanti, pos 1 archi all'indietro e pos 2 archi di attraversamento
def count_edges(AL: list[list[int]]) -> tuple[int,int,int]:
    res = [0,0,0]
    V = [0 for _ in range(len(AL))] # O(n)
    time = 0
    timestamp = [-1 for _ in range(len(AL))] # O(n)
    DFS_count(0,AL,V,res,time,timestamp) # O(n + m)
    return res[0],res[1],res[2]

def DFS_count(u: int, L: list[list[int]], V: list[int], res: list[int], time: int, timestamp: list[int]) -> int:
    V[u] = 1
    timestamp[u] = time
    for v in L[u]:
        if V[v] == 0:
            time = DFS_count(v,L,V,res, time + 1, timestamp)
        elif V[v] == 1:
            res[1] += 1
        else:
            if timestamp[u] > timestamp[v]:
                res[2] += 1
            else:
                res[0] += 1
    V[u] = 2
    return time

G1 = [
    [1],
    [2,3,4],
    [5],
    [],
    [1,5,6],
    [2,7],
    [7,9],
    [10],
    [6],
    [8],
    [11],
    [9],
]

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

if __name__ == '__main__':
    print("risultato algoritmo che conta i tipi di archi: ", count_edges(G))
    print("CFS di G1: ", tarjan(G1))