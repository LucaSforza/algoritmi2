G = [
    [1,2], # 1 -> 2,3
    [0,2], # 2 -> 1,3
    [0,1], # 3 -> 1,2
    [4,10,6], # 4 -> 5,11,7
    [3], # 5 -> 4
    [],  # 6 -> None
    [3], # 7 -> 4
    [8], # 8 -> 9
    [7], # 9 -> 8
    [10],# 10 -> 11
    [9,3], # 11 -> 10,3
    [12,13], # 12 -> 13,14
    [11,14,15], # 13 -> 12,15,16
    [11,14], # 14 -> 12,15
    [12,13], # 15 -> 13,14
    [12], # 16 -> 13
]

V = [0 for _ in range(len(G))]

def es7v(L: list[list[int]], V)-> int:
    count = 0
    for i in range(len(L)):
        if V[i] == 0 and is_tree(i,None,L,V):
            count+=1
    return count

def is_tree(nodo:int,lastVisited:int,grafo:list[list[int]],visitati:list[int])-> bool:
    visitati[nodo] = 1
    for nextNodo in grafo[nodo]:
        if visitati[nextNodo] == 0:
            return is_tree(nextNodo,nodo,grafo,visitati)
        elif nextNodo != lastVisited:
            return False
    return True
    
        
if __name__ == '__main__':

    graf = [[1,2],[3],[3],[]]
    V = [0 for _ in range(len(graf))]

    print(es7v(graf,V))