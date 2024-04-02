from draw import draw

G = [
    [3,4,5,8],
    [7,2],
    [1,6,7],
    [0,4,7],
    [0,3],
    [0,8],
    [2],
    [1,2,3],
    [0,5],
]

# algoritmo che trova i ponti di un grafo in O(n+m)
def ponti(G: list[list[int]]) -> list[tuple[int,int]]:
    from math import inf
    def DFSr(
        u: int,
        p: int,
        level: int,
        G: list[list[int]],
        V: list[int],
        list_out: list[tuple[int,int]]
    ) -> int:
        V[u] = level
        min_h = inf
        for v in G[u]:
            if V[v] == -1:
                min_v = DFSr(v,u,level + 1, G, V, list_out)
                min_h = min(min_v,min_h)
                if level < min_v:
                    list_out.append((u,v))
            elif V[v] != -1 and v != p:
                min_h = min(min_h,V[v])
        return min_h

    V = [-1]*len(G)
    list_out = []
    # inizio da 0 poichè il grafo per ipotesi è connesso
    DFSr(0,None,0,G,V,list_out)
    return list_out

if __name__ == '__main__':
    print(ponti(G))
    draw(G)