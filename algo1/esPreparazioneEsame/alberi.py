class NodoABR2:
    def __init__(self, key = None, parent = None, num = 0, left = None, right = None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.num = num


def es3(nodo:NodoABR2,x):
    found = False
    if nodo.key<x:
        if nodo.right != None:
            if nodo.key==x:
                found = True
            else:
                if not es3(nodo.right,x):
                    nodo.num+=1
        else:
            nodo.right = NodoABR2(x,nodo)

    elif nodo.key>x:
        if nodo.left != None:
            if nodo.key==x:
                found = True
            else:
                if not es3(nodo.left,x):
                    nodo.num+=1
        else:
            nodo.left = NodoABR2(x,nodo)
    
    return found


if "__main__" == __name__:
    P = NodoABR2(5, None, 6, NodoABR2(2, 5, 3, NodoABR2(1, 2),NodoABR2(4, 2, 1, NodoABR2(3, 4))),NodoABR2(7, 5, 3, NodoABR2(6, 7),NodoABR2(9, 7, 1, NodoABR2(8, 9))))
    es3(P, 10)
    print(P)