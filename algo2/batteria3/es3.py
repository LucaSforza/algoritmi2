from draw import draw

G = [
    [1,3,4],
    [0,2],
    [1,3,4],
    [0,2,4],
    [0,2,3],
]

# restituisce un cammino dove si passa per ogni arco una ed una sola volta
def cammino(G: list[list[int]]) -> list[int]:
    def DFSr(u: int,p: int,G: list[list[int]],V: list[int],cam: list[int]) -> None:
        V[u] = 1
        cam.append(u)
        for v in G[u]:
            if V[v] == 0:
                DFSr(v,u,G,V,cam)
                cam.append(u)
            if V[v] == 1 and not v == p:
                cam.extend([v,u])
        V[u] = 2
    cam = []
    V = [0]*len(G)
    # dato che è connesso posso partire da un qualsiasi nodo per visitarlo tutto
    DFSr(0,None,G,V,cam)
    return cam

if __name__ == '__main__':
    print(cammino(G))
    draw(G)