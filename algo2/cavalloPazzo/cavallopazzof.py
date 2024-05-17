import sys
from math import sqrt,ceil
from img import make_img_from_board

sys.setrecursionlimit(1_100_000)

def print_board(vett,n):
    sOut = ''
    cnt = 0
    for cas in vett:
        sOut+=str(cas)
        cnt+=1
        if cnt == n:
            sOut+='\n'
            cnt = 0
    print(sOut)
    return 

def save_board(vett,n,nomeFile):
    sOut = ''
    cnt = 0
    for cas in vett:
        sOut+=str(cas)
        cnt+=1
        if cnt == n:
            sOut+='\n'
            cnt = 0
    with open(nomeFile, 'a') as f:
        f.write(sOut+'\n\n')
    return 

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

def make_cnt(n):
    cnt = [0]*(n*n)
    for y in range(n):
        for x in range(n):
            update_cnt(n,x,y,cnt,None,False)
    return cnt

def update_cnt(n,x,y,cnt,nelPath,dec):
    rev = False
    mosse_cavallo = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)] # (x,y)
    for mossa in mosse_cavallo:
                tx = x+mossa[0]
                ty = y+mossa[1]
                if n>tx>=0 and  n>ty>=0:
                    t_idx = cordToIdx(n,tx,ty)
                    if dec:
                        cnt[t_idx]-=1
                        if cnt[t_idx]==0 and nelPath[t_idx]==0:
                            rev = True
                    else:
                        cnt[t_idx]+=1
    return rev

def dist_centro(n,pos):
    x,y = idxToCord(n,pos)
    centro = n/2
    return sqrt((x-centro)**2+(y-centro)**2)

def hamiltonian_path(n,graph, pos, path, nelPath, move_cnt,nomeFile,id=0):
    path.append(pos)
    nelPath[pos]=1
    save_board(nelPath,n,nomeFile)
    #make_img_from_board(nelPath,n,1000,nomeFile+str(id))
    id+=1
    deltalen=len(graph)-len(path)
    if not deltalen:
        return path
    
    x,y = idxToCord(n,pos)

    if not update_cnt(n,x,y,move_cnt,nelPath,dec=True) or deltalen == 1:
        neighbor_list = [n for n in graph[pos] if nelPath[n]==0]
        neighbor_list.sort(key = lambda neig: (move_cnt[neig]*n)+dist_centro(n,neig))
        for neighbor in neighbor_list:
            extended_path = hamiltonian_path(n,graph, neighbor, path,nelPath,move_cnt,nomeFile,id)
            if extended_path: 
                return extended_path
        
    path.pop()
    nelPath[pos]=0
    update_cnt(n,x,y,move_cnt,nelPath,dec=False)
    return None

def percorsoCavallo(n):
    graf = creaGrafo(n)
    used = [0]*(n*n)
    move_cnt = make_cnt(n)
    nomeRicerca = './algo2/cavalloPazzo/txt/('+str(n)+'*'+str(n)+')ricerca.txt'
    with open(nomeRicerca, 'w') as f:
        f.write('\n')
    sol = hamiltonian_path(n,graf,0,[],used,move_cnt,nomeRicerca)
    return sol

#TODO quando metto una casella a 1 nel vettore caratteristico nelPath mi devo assicurare che tutti gli zero che puntano all'uno appena messo abbiamo almeno un altro zero su cui andare 
if __name__ == '__main__':
    percorsoCavallo(34)

    # num = 5
    # vett = [0]*(num*num)
    # print_board(vett,num)

