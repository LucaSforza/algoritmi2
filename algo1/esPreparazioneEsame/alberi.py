class NodoABR1:
    def __init__(self, key = None, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

class NodoABR2:
    def __init__(self, key = None, parent = None, num = 0, left = None, right = None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.num = num


def es3(nodo:NodoABR1,x):
    found = False
    if nodo.key<x:
        if nodo.right != None:
            if nodo.key==x:
                found = True
            else:
                if not es3(nodo.right,x):
                    nodo.num+=1
        else:
            nodo.right = NodoABR1(x,nodo)

    elif nodo.key>x:
        if nodo.left != None:
            if nodo.key==x:
                found = True
            else:
                if not es3(nodo.left,x):
                    nodo.num+=1
        else:
            nodo.left = NodoABR1(x,nodo)
    
    return found


def kappesimo_elemento_albero(nodoAlbero,k,cnt=0):
    
    if nodoAlbero.left!=None:
        out,cnt = kappesimo_elemento_albero(nodoAlbero.left,k,cnt)
        if cnt==k:
            return out,cnt   
             
    cnt+=1
    if cnt == k : return nodoAlbero.key,cnt

    if nodoAlbero.right!=None:
        out,cnt = kappesimo_elemento_albero(nodoAlbero.right,k,cnt)
        if cnt == k:
            return out,cnt
        
    return nodoAlbero.key,cnt

if "__main__" == __name__:
    # P = NodoABR2(5, None, 6, NodoABR2(2, 5, 3, NodoABR2(1, 2),NodoABR2(4, 2, 1, NodoABR2(3, 4))),NodoABR2(7, 5, 3, NodoABR2(6, 7),NodoABR2(9, 7, 1, NodoABR2(8, 9))))
    # es3(P, 10)
    # print(P)
    P = NodoABR1(5,
                 NodoABR1(2,
                          NodoABR1(1),
                          NodoABR1(4,
                                   NodoABR1(3))),
                 NodoABR1(7,
                          NodoABR1(6),
                          NodoABR1(9,
                                   NodoABR1(8))))
    #p = NodoABR1(2,NodoABR1(1),NodoABR1(3))
    out,cnt = kappesimo_elemento_albero(P,8)
    print(out)
