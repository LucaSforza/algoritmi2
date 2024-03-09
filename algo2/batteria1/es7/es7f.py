from draw import netGrafToListAdiacenzaList,edgeListToNetGraf,drawNetGraf



def es7f(grafo:list[list[int]])->int:
    nAlberi = 0
    incontrati = [0]*len(grafo)
    counterComponenti = 1

    return

netGr = edgeListToNetGraf([("A","B"),("A","C"),("A","D"),("C","D")])
drawNetGraf(netGr)
adiList = netGrafToListAdiacenzaList(netGr)

es7f(adiList)