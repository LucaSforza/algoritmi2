
def percorso(n,scacchiera,sol,mosse_cavallo,x=0,y=0):
    if len(sol)==(n*n)-1:
        return True
    scacchiera[y][x]=1
    sol.append((x,y))
    for mossa in mosse_cavallo:
        tx = x+mossa[0]
        ty = y+mossa[1]
        if n>tx>=0 and  n>ty>=0 and scacchiera[ty][tx]==0:
            if percorso(n,scacchiera,sol,mosse_cavallo,tx,ty):
                return True
    sol.pop()
    scacchiera[y][x]=0
    return False

def cercaP(n):
    mosse_cavallo = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)] # (x,y)
    sol = []
    scacchiera = [[0]*n for _ in range(n)]
    ris = percorso(n,scacchiera,sol,mosse_cavallo)
    print(sol)
    return ris

################################################################################################

def ricerca(n,grafo,visitati,count,sol,x=0,y=0):
    idx = cordToIdx(n,x,y)
    visitati[idx]=1
    count-=1
    if count == 0 :
        sol.append((x,y))
        return True
    for adi in grafo[idx]:
        if visitati[adi]==0:
            ax,ay = idxToCord(n,adi)
            if ricerca(n,grafo,visitati,count,sol,ax,ay):
                sol.append((x,y))
                return True
    visitati[idx]=0
    return False


def cercaPercorsoGrafo(n):
    scacchiera = [[0 for _ in range(n)] for _ in range(n)]
    grafo = creaGrafo(n)
    visitati = [0]*(n*n)
    sol = []
    if ricerca(n,grafo,visitati,n*n,sol):
        print(list(reversed(sol)))
    else:
        print('non trovato')
    return 

def percMat(grafo,n):
    nNodi = len(grafo)
    mat = [[[0]*nNodi] for _ in range(nNodi)]
    for npassi in range(nNodi):
        for nodo in range(nNodi):
            gn = grafo[nodo]
            for adi in gn:
                xt = idxToCord(n,adi)
                if npassi==0:
                    mat[npassi][nodo][xt]=1
                else:
                    for adi2 in gn:
                        yt2 = idxToCord(n,adi2)
                        if mat[npassi-1][yt2][xt]:
                            mat[npassi][nodo][xt]=1
    print(mat[-1])
    return

###############################################################################################


def ricerca3(grafo,visitati,contatore,count=0,pos=0):
    
    if count == (n*n)-1:
        return True
    visitati[pos]=1
    rev = []
    for adi in grafo[pos]:
        contatore[adi]-=1
        rev.append(adi)
        if contatore[adi]==0 and visitati[adi]==0:
            print(contatore[adi])
            print(visitati[adi])
            print()
            for d in rev:
                contatore[d]+=1
            rev = []
            visitati[pos]=0
            return False
    for adi in grafo[pos]:
        if visitati[adi]==0:
            if ricerca3(grafo,visitati,contatore,count+1,adi):
                return True
    visitati[pos]=0
    return False

def haPercorso(n):
    scacchiera = [[0]*n for _ in range(n)]
    grafo = creaGrafo(n)
    visitati = [0]*((n*n))
    contatore = [0]*((n*n))
    for nodo in grafo:
        for adi in nodo:
            contatore[adi]+=1
    print(contatore)

    print(ricerca3(grafo,visitati,contatore))
    return

################################################################
def cordToIdx(n,x,y):
    return x+(y*n)

def idxToCord(n,i):
    x = i%n
    y = i//n
    return x,y

def creaGrafo(n):
    mosse_cavallo = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)] # (x,y)
    grafo = [[] for _ in range(n*n)]
    for x in range(n): # creo grafo
        for y in range(n):
            for mossa in mosse_cavallo:
                tx = x+mossa[0]
                ty = y+mossa[1]
                if n>tx>=0 and  n>ty>=0:
                    grafo[cordToIdx(n,x,y)].append(cordToIdx(n,tx,ty))
    return grafo

def hamiltonian_path(graph, pos, path,nelPath,counter):
    path += [pos]

    if len(path) == len(graph):
        return path
    nelPath[pos]=1
    x,y = idxToCord(n,pos)
    if mosse_legali(x,y,counter):
        mosse_legali(x,y,counter,False)
        return None
    for neighbor in graph[pos]:
        if nelPath[neighbor]==0:
            extended_path = hamiltonian_path(graph, neighbor, path,nelPath,counter)
            if extended_path: 
                return extended_path
            elif neighbor==graph[-1]:
                path.pop()
                nelPath[pos]=0
    return None

def mosse_legali(x,y,counter,decremento = True):
    rev = False
    mosse_cavallo = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)] # (x,y)
    for mossa in mosse_cavallo:
                tx = x+mossa[0]
                ty = y+mossa[1]
                if n>tx>=0 and  n>ty>=0:
                    if decremento:
                        counter[cordToIdx(n,tx,ty)]-=1
                        if counter[cordToIdx(n,tx,ty)]==0:
                            rev = True
                    else:
                        counter[cordToIdx(n,tx,ty)]+=1
    return rev

def prova1(n):
    graf = creaGrafo(n)
    sol = []
    nelPath = [0]*(n*n)
    counter = [0]*(n*n)
    for y in range(n):
        for x in range(n):
            mosse_legali(x,y,counter,False)
    return hamiltonian_path(graf,0,sol,nelPath,counter)

if __name__ == '__main__':
   n = 5
   print(prova1(n))
   #percMat(graf,n)
#    print(prova1(n))
#    print(len(set(prova1(n))))