from draw import draw

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
    DFS1(0,AL,V,res,time,timestamp) # O(n + m)
    return res[0],res[1],res[2]

def DFS1(u: int, L: list[list[int]], V: list[int], res: list[int], time: int, timestamp: list[int]) -> int:
    V[u] = 1
    timestamp[u] = time
    for v in L[u]:
        if V[v] == 0:
            time = DFS1(v,L,V,res, time + 1, timestamp)
        elif V[v] == 1:
            res[1] += 1
        else:
            if timestamp[u] > timestamp[v]:
                res[2] += 1
            else:
                res[0] += 1
    V[u] = 2
    return time

if __name__ == '__main__':
    print(count_edges(G))
    #draw(G,direct=True)