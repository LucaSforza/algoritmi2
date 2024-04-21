from collections import deque
from draw import draw

def find_sorg(grafo)->list[int]: # H(n+m)
    entr = [0]*len(grafo)
    for nodo in grafo:
        for adi_nodo in nodo:
            entr[adi_nodo]+=1
    return entr

def sort_top(grafo,sorg,trad,ordine,sorg_trov = 0): # H(n+m)
    for i,grad in enumerate(sorg):
        if grad==0:
            trad[i] = sorg_trov
            sorg_trov+=1
            ordine.append(i)
            sorg[i]-=1
            for edge in grafo[i]:
                sorg[edge]-=1
            sort_top(grafo,sorg,trad,ordine,sorg_trov)
    return ordine,trad

def cercaAdiacenti(grafo,componenti): # H(n+m)
    for currnodo,adiacenti in enumerate(grafo):
        for adiNodo in adiacenti: 
            if adiNodo > currnodo:
                componenti[adiNodo] = componenti[currnodo]
            elif adiNodo < currnodo:
                if componenti[adiNodo]==adiNodo:
                    if componenti[currnodo]==currnodo:
                        componenti[currnodo]=componenti[adiNodo]
                    else:
                        componenti[adiNodo]=componenti[currnodo]
    return

def es7f2(grafo)->int:
    sorg = find_sorg(grafo) # H(n+m)
    trad = [[] for _ in range(len(grafo))]
    sort_node,trad = sort_top(grafo,sorg,trad,[]) # H(n+m)
    sort_graf = [[] for _ in range(len(grafo))]
    for i,nodo in enumerate(sort_node): # H(n+m)
        for adi_node in grafo[nodo]:
            sort_graf[i].append(trad[adi_node])
    comp = []
    for nodo in range(len(sort_graf)): # H(n)
        comp.append(nodo)
    cercaAdiacenti(sort_graf,comp) # H(n+m)
    compTrovata = [0]*len(grafo)
    ncomp = 0
    for com in comp: # H(n)
        if compTrovata[com]==0:
            compTrovata[com]+=1
            ncomp+=1
    return ncomp

esempio1 = [[1],[3,4],[6],[4],[],[],[5]] # expected = 2
esempio2 = [[2],[0,3,4],[],[2],[]] # expected = 1
esempio3 = [[1],[2],[],[3]] # expected = 2
esempio4 = [[2],[2],[3],[]] # expected = 2
esempio5 = [[],[],[],[]] # expected = 4
esempio6 = [[1,2,3],[0,2,3],[0,1,3],[0,1,2]] # expected = 4
esempio7 = [[],[0],[1]] # expected = 1

print(es7f2(esempio1)==2)
print(es7f2(esempio2)==1)
print(es7f2(esempio3)==2)
print(es7f2(esempio4)==2)
print(es7f2(esempio5)==4)
print(es7f2(esempio6)==4)
print(es7f2(esempio7)==1)

