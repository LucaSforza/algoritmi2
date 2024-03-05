def init_completo(n: int) -> list[list[int]]:
    res: list[list[int]] = [[] for _ in range(n)]
    for i in range(n):
        for y in range(n):
            if y != i:
                res[y].append(i)
    return res

def DFS(u: int, L: list[list[int]], V: list[int]):
    V[u] = 1
    for x in reversed(L[u]):
        if V[x] == 0:
            L[x].pop()
    if u != 0:
        DFS(u-1,L,V)
            
    
if __name__ == '__main__':
    n = 3
    V = [0 for _ in range(n)]
    L = init_completo(n)
    DFS(n - 1,L,V)
    print(L)