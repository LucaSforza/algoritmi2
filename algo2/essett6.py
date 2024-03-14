def find_ancestor(padri: list[int], anc: int, nodo:int) -> bool:
    if padri[nodo] == anc:
        return True
    if padri[nodo] == nodo:
        return False
    found = False
    return found or find_ancestor(padri,anc,padri[nodo])


def cnt_edges_types(
        grafo:list[list[int]],
        nodo:int,
        padre:int,
        padri:list[int],
        visitati:list[int],
        cnt_i: int, # contantore archi in avanti
        cnt_a: int, # contantore archi in avanti
        cnt_t: int, # contatore archi di traverso
    ) -> tuple[int,int,int] :
    padri[nodo]= padre
    visitati[nodo]=1
    for nex_node in grafo[nodo]:
        if padri[nex_node]==-1:
            f_cnt_i, f_cnt_a, f_cnt_t = cnt_edges_types(grafo,nex_node,nodo,padri,visitati,0,0,0)
            cnt_i += f_cnt_i
            cnt_a += f_cnt_a
            cnt_t += f_cnt_t
        elif visitati[nex_node] == 1:
            cnt_i += 1
        else:
            if find_ancestor(padri, nodo, nex_node):
                cnt_a += 1
            else:
                cnt_t += 1
    visitati[nodo] = 2
    return cnt_i, cnt_a, cnt_t


def conta_archi(grafo:list[list[int]],nodo:int):
    padri = [-1]*len(grafo)
    visitati = [0]*len(grafo)
    print(cnt_edges_types(grafo,nodo,nodo,padri,visitati,0,0,0))

if __name__=="__main__":
    graf = [[1,2],[3],[3],[4,5],[5],[6],[1]]

    conta_archi(graf,0)