from draw import draw

# gli archi sono tuple (v,c) in v è il nodo in uscita, c è il costo per attraversarlo
grafo_pesato = list[list[tuple[int,int]]]
unionfind = list[tuple[int]]

def kruskal(G: grafo_pesato) -> grafo_pesato:
    m = [(c,u,v) for u in range(len(G)) for v,c in G[u] if u < v]
    m.sort(reverse=True)
    T = [[] for _ in range(len(G))]
    C = crea(T)
    while m:
        # da x va a y
        c,x,y = m.pop()
        cx = find(x,C)
        cy = find(y,C)
        if cx != cy:
            T[x].append(y)
            T[y].append(x)
            union(cx,cy,C)
    return T

def crea(T: grafo_pesato) -> unionfind:
    return [(x,1) for x in range(len(T))]

def find(u: int, C: unionfind) -> int:
    while u != C[u][0]:
        u = C[u][0]
    return u

def union(a: int,b: int,C: unionfind) -> None:
    tota,totb = C[a][1], C[b][1]
    if tota >= totb:
        C[a] = (a, tota+totb)
        C[b] = (a, totb)
    else:
        C[b] = (b, tota+totb)
        C[a] = (b, tota)

G=[
    [(1,25), (2,10), (3,35)],
    [(0,25), (2,20), (3,42)],
    [(0,10), (1,20), (3,40)],
    [(0,35), (1,42), (2,40)]
]

if __name__ == '__main__':
    draw(kruskal(G))