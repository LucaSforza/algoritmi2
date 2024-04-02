from typing import Optional

# Esercizio 1 lucici, questo algoritmo è 𝛩(n)
def cassonetti(case: list[int], k: int) -> list[int]:
    pos_k = None
    result = []
    for c in case: # eseguito esattamente n volte
        if not rientra(c,pos_k,k): # il corpo del for è costante 𝛩(1)
            pos_k = c + k
            result.append(pos_k)
    return result

def rientra(c: int,pos_k: Optional[int],k :int) -> bool:
    if pos_k is None:
        return False
    return c >= pos_k - k and c <= pos_k + k

albero = list[list[int]]

# Esercizio 2 lucidi, costo O(n)
def indipendente_max(T: albero) -> list[int]:
    from collections import deque
    D = [-1]*len(T) # vettore delle distanze
    coda = deque()
    for u in range(len(T)): # eseguito 𝛩(n) volte
        if len(T[u]) == 1:
            D[u] = 0
            coda.append(u)
    result = [0]*len(T) # lista con tutti i nodi che fanno parte dell'insieme indipendente massimo 
    # 1 se appartengono 0 altrimenti
    while coda:
        control = True
        u = coda.popleft()
        for y in T[u]:
            if D[y] == -1:
                D[y] = D[u] + 1
                coda.append(y)
            elif D[y] == D[u]:
                # questo caso accade solo per alberi con una quantità di nodi non foglie pari
                if result[y]:
                    control = False
        if D[u] % 2 == 0 and control:
            result[u] = 1
    return [u for u in range(len(T)) if result[u]]

if __name__ == '__main__':
    C = [2, 5, 7, 11, 14, 16, 18]
    k = 3
    print("esercizio 1 cassonetti: ",cassonetti(C,k))
    G = [
        [4],
        [2],
        [1,4,8],
        [5],
        [0,2,9],
        [3,6,7,8],
        [5],
        [5],
        [2,5],
        [4],
    ]
    ind = indipendente_max(G)
    print("esercizio 2 albero con insieme indipendente: ",ind," lunghezza: ",len(ind))