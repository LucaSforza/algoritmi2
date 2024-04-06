


def cercaNodo(grafo:list[list[int]],orientamento:list[list[int]]):
    dritti = [0 for _ in grafo]
    rovescio = [0 for _ in grafo]
    visita(grafo,orientamento,5,5,rovescio,dritti)
    min = 0
    for i,nr in enumerate(rovescio):
        if rovescio[min]>nr:
            min = i
    print(rovescio)
    return min

def visita(grafo:list[list[int]],orientamento:list[list[int]],nodoPartenza:int,padre:int,rovescio:list[int],dritti:list[int]):
    nr,nd = 0,0
    for nexnodo in grafo[nodoPartenza]:
        if nexnodo!=padre:
            if orientamento[nodoPartenza][nexnodo]:
                nd = nd+1
            else:
                nr = nr+1
            nr1,nd1 = visita(grafo,orientamento,nexnodo,nodoPartenza,rovescio,dritti)
            nr,nd = nr+nr1,nd+nd1
    rovescio[nodoPartenza]= nr
    dritti[nodoPartenza]= nd

    return rovescio[nodoPartenza],dritti[nodoPartenza]

def cercaNodo2(orientamento:list[list[int]]):
    dritti = [0 for _ in orientamento]
    rovescio = [0 for _ in orientamento]
    visitati = [0 for _ in orientamento]
    visita2(orientamento,0,0,rovescio,dritti,visitati)
    min = 0
    for i,nr in enumerate(rovescio):
        if rovescio[min]>nr:
            min = i
    print(rovescio)
    return min

def visita2(orientamento:list[list[int]],nodoPartenza:int,padre:int,rovescio:list[int],dritti:list[int],visitati:list[int]):
    nr,nd = 0,0
    visitati[nodoPartenza] = 1
    for i,nexnodo in enumerate(orientamento[nodoPartenza]):
        ci_sta_arco = False
        if visitati[i]!=1:
            if orientamento[nodoPartenza][i]:
                nd += 1
                ci_sta_arco = True
            if orientamento[i][nodoPartenza]:
                nr += 1
                ci_sta_arco=True
            if ci_sta_arco:
                nr1,nd1 = visita2(orientamento,nexnodo,nodoPartenza,rovescio,dritti,visitati)
                nr,nd = nr+nr1,nd+nd1
    rovescio[nodoPartenza]= nr
    dritti[nodoPartenza]= nd
    return rovescio[nodoPartenza],dritti[nodoPartenza]

graf = [[],[0],[0],[0],[0],[4]]
orient = [
    [0,0,0,0,0,0],
    [1,0,0,0,0,0],
    [1,0,0,0,0,0],
    [1,0,0,0,0,0],
    [1,0,0,0,0,0],
    [0,0,0,0,1,0]
]

print(cercaNodo(graf,orient))
print(cercaNodo2(orient))