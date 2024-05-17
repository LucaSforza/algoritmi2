import sys
from time import time 
sys.setrecursionlimit(1_100_000)

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

def hamiltonian_path(n,graph, pos, path, nelPath, move_cnt,start,timeOut):
    if time()-start>timeOut:
        return n
    path.append(pos)
    nelPath[pos]=1

    deltalen=len(graph)-len(path)
    if not deltalen:
        return path
    
    x,y = idxToCord(n,pos)

    if not update_cnt(n,x,y,move_cnt,nelPath,dec=True) or deltalen == 1:
        neighbor_list = [n for n in graph[pos] if nelPath[n]==0]
        neighbor_list.sort(key = lambda n: move_cnt[n])
        for neighbor in neighbor_list:
            extended_path = hamiltonian_path(n,graph, neighbor, path,nelPath,move_cnt,start,timeOut)
            if extended_path: 
                return extended_path
        
    path.pop()
    nelPath[pos]=0
    update_cnt(n,x,y,move_cnt,nelPath,dec=False)
    return None

def percorsoCavalloricerca(n,start,timeOut):
    graf = creaGrafo(n)
    used = [0]*(n*n)
    move_cnt = make_cnt(n)
    sol = hamiltonian_path(n,graf,0,[],used,move_cnt,start,timeOut)

    return sol

def cercaNumeriCritici(limite,timeOut):
    numeri = []
    for n in range(5,limite):
        print(n)
        start = time()
        ret = percorsoCavalloricerca(n,start,timeOut)
        if type(ret)==int:
            numeri.append(ret)
    return numeri


if __name__ == '__main__':
    # start = time()
    # print(percorsoCavalloricerca(35,start,1.0))

    
    num = 300

    print(cercaNumeriCritici(num,2.0))
    sec1 = [35, 36, 52, 63, 87, 93, 98, 99, 101, 106, 108, 109, 121, 125, 127, 141, 144, 145, 147, 152, 154, 157, 158, 161, 165, 166, 169, 173, 183, 184, 185, 189, 191, 193, 197, 199, 201, 205, 206, 209, 213, 215, 217, 219, 222, 223, 225, 227, 229, 230, 231, 234, 236, 237, 238, 239, 240, 241, 243, 247, 251, 252, 253, 254, 255, 256, 257, 259, 260, 261, 263, 264, 265, 267, 268, 269, 270, 271, 272, 273, 274, 275, 277, 279, 280, 281, 283, 284, 285, 287, 289, 291, 292, 294, 299]
    sec2 = [35, 36, 52, 63, 87, 93, 98, 99, 101, 106, 108, 109, 121, 125, 127, 141, 144, 145, 147, 152, 154, 157, 158, 161, 165, 166, 169, 173, 183, 185, 189, 191, 193, 197, 199, 201, 205, 206, 209, 213, 215, 217, 219, 222, 223, 225, 227, 229, 230, 231, 234, 236, 237, 238, 239, 240, 241, 243, 247, 251, 252, 253, 254, 255, 256, 257, 259, 260, 261, 263, 264, 265, 267, 268, 269, 270, 271, 272, 273, 274, 275, 277, 279, 280, 281, 283, 284, 285, 287, 289, 291, 292, 294, 299]