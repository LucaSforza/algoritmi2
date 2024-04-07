
def cercaAdiacenti(grafo,componenti):
    for currnodo,adiacenti in enumerate(grafo):
        for adiNodo in adiacenti: # H(n+m)
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
    componenti = []
    numNodi = len(grafo)
    for nodo in range(numNodi): # H(n)
        componenti.append(nodo)
    cercaAdiacenti(grafo,componenti) # H(n+m)
    nComp = len(set(componenti))
    return nComp

esempio1 = [[1],[3,4],[6],[4],[],[],[5]] # expected = 2
esempio2 = [[2],[0,3,4],[],[2],[]] # expected = 1
esempio3 = [[1],[2],[],[3]] # expected = 2
esempio4 = [[2],[2],[3],[]] # expected = 2
esempio5 = [[],[],[],[]] # expected = 4
esempio6 = [[1,2,3],[0,2,3],[0,1,3],[0,1,2]] # expected = 4

print(es7f2(esempio1)==2)
print(es7f2(esempio2)==1)
print(es7f2(esempio3)==2)
print(es7f2(esempio4)==2)
print(es7f2(esempio5)==4)
print(es7f2(esempio6)==1)



