from unionfind import *

def spanning_tree(G):
    T = [[] for _ in range(len(G)) ] #H(n)
    E = [(c,x,y) for x in range(len(G)) for y,c in G[x] if x<y] # H(m)
    E.sort(reverse = True)
    C = crea(len(G))
    #while E!=[]:
    while E:
        c,x,y = E.pop() # O(1)
        cx = find(x,C) # O(log(n))
        cy = find(y,C) # O(log(n))
        if cx != cy:
            T[x].append(y)
            T[y].append(x)
            union(cx,cy,C)
    return

def crea(n):
    C = [x for x in range(n)]
    return C

def find(x,C):
    return C[x]

def union(x,y,C):
    if C[x]!=C[y]:
        ma = max(C[x],C[y])
    if ma == C[x]:
        mi = c[y]
    else:
        mi = c[y]
    for n in C:
        if c == mi:
            C[c]=ma



if __name__=="__main__":
    c = 2
    graf = [[]]
    spanning_tree(graf,0)