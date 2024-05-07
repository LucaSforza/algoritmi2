from copy import deepcopy
#from draw import *

# usando liste di adiacenza 
def es2f(grafo:list[list[int]])->list[list[int]]: #O(n(n+m)) = O(nn+nm) = O(nm))
    contIteraz = 0
    gQuadro = [set() for _ in range(len(grafo))]  
    for i,nodo in enumerate(grafo):
        contIteraz+=1
        for adiNodo in nodo: # H(n+m)
            contIteraz+=1
            gQuadro[i].add(adiNodo)
            for nodo in grafo[adiNodo]: # O(n)
                contIteraz+=1
                gQuadro[i].add(nodo)
    return gQuadro,contIteraz

# usando matrici di adiacenza 
def es2fmat(grafo:list[list[int]])->list[list[int]]: # H(n^3)
    contIteraz = 0
    gQuadro = [set() for _ in range(len(grafo))]  
    for inl,line in enumerate(grafo): # H(n)
        contIteraz+=1
        for ie,edge in enumerate(line): # H(n)
            contIteraz+=1
            if edge:
                gQuadro[inl].add(ie)
                for ieq,edgeq in enumerate(grafo[ie]): # H(n)
                    contIteraz+=1
                    if edgeq:
                        gQuadro[inl].add(ieq)
    return gQuadro,contIteraz

matriceAdiacenza = [[0,1,0,0,0,0],
       [0,0,1,0,0,0],
       [0,0,0,1,0,0],
       [0,0,0,0,1,0],
       [0,0,0,0,0,1],
       [1,0,0,0,0,0]
       ]
matriceAdiacenzaCompl = [[1,1,1,1,1,1],
       [1,1,1,1,1,1],
       [1,1,1,1,1,1],
       [1,1,1,1,1,1],
       [1,1,1,1,1,1],
       [1,1,1,1,1,1],]

listaAdiacenza = [[1],[2],[3],[4],[5],[0]]
listaAdiacenzaCompl = [[1,2,3,4,5],[0,2,3,4,5],[0,1,3,4,5],[0,1,2,4,5],[0,1,2,3,5],[0,1,2,3,4]]

daMatrice,itmat = es2fmat(matriceAdiacenzaCompl)
daLista,itList = es2f(listaAdiacenzaCompl)
print(daMatrice)
print(daLista)
print("stesso output:"+str(daLista==daMatrice))
print('iterazioni matrice: '+str(itmat))
print('iterazioni liste: '+str(itList))