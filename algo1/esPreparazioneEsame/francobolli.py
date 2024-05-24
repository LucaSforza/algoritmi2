

def intervalloFrancobolliDaButtare(n,m):
    A = [i for i in range(1,m+1)]
    T = [[[None for _ in range(m)]for _ in range(m)]for _ in range(n+1)]
    print(T)
    for s in range(n+1):
        for y in range(m):
            for x in range(m):
                if s == 0:
                    T[s][y][x]=0
                elif s == 1:
                    if x == y:
                        T[s][y][x]=A[x]
                else:
                    T[s][y][x]=T[s-1][y][x]+A[y]
    return 

def ricerca(n,somma,scelte,risultati):
    if n==0 or len(scelte)==0:
        risultati[somma-1]=somma
        return 
    if len(scelte)>n:
        ricerca(n,somma,scelte[1:],risultati)
    ricerca(n-1,somma+scelte[0],scelte[1:],risultati)
    return

def intervalloFrancobolli(n,m):
    scelte = [v  for v in range(1,m+1) for _ in range(n)]
    risultati = [None for _ in range(m*n)]
    ricerca(n,0,scelte,risultati)
    print(risultati)
    return
if __name__=="__main__":
    intervalloFrancobolli(4,4)