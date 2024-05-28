

class Nodo:
    def __init__(self,key = None , left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def esMonti(radice):
    if radice.left == radice.right == None: return True
    if (radice.left and esMonti(radice.left) and radice.key<radice.left.key):
        return True
    if (radice.right and esMonti(radice.right) and radice.key<radice.right.key):
        return True

    return False

def es3(radice):
    caml = False
    camr = False
    if radice.left==None and radice.right == None:
        return True
    if radice.left !=None and radice.left.key == radice.key:
        caml = es3(radice.left)
    if radice.right !=None and radice.right.key == radice.key:
        camr = es3(radice.right)
    return caml or camr

class NodoP:
    def __init__(self,key = None , next = None):
        self.key = key
        self.next = next


def CercaMinElementi(listp,k,somma):
    if somma<k:
        return CercaMinElementi(listp.next,k,somma+listp.key)+1
    return 0

def ordinaNegativiPositivi(nodoPuntato,lastNode = None,testa = None):
    if nodoPuntato.next == None:
        return testa
    prossimo = nodoPuntato.next
    if testa == None:
        testa = nodoPuntato
  
    if nodoPuntato.key<0:
            oldTesta = testa
            riattacco = nodoPuntato.next
            testa = nodoPuntato
            nodoPuntato.next = oldTesta
            lastNode.next = riattacco
            prossimo = riattacco
            prima = riattacco
    else:
        prossimo = nodoPuntato.next
        prima = nodoPuntato
            
    ordinaNegativiPositivi(prossimo,prima,testa)

    return testa


def stampaListP(listp):
    while listp:
        print(listp.key)
        listp = listp.next 

from math import inf

def cercaMinMaxListaP(nodeP,massimo = 0,minimo = inf):
    if nodeP != None:
        if nodeP.key>massimo : massimo = nodeP.key
        if nodeP.key<minimo : minimo = nodeP.key
        return cercaMinMaxListaP(nodeP.next,massimo,minimo)
    else:
        return minimo,massimo


def camminoMassimoAlbero(nodoAlbero):
    if nodoAlbero == None:
        return 0
    else:
        cammsx = camminoMassimoAlbero(nodoAlbero.left)
        cammdx = camminoMassimoAlbero(nodoAlbero.right)
        return nodoAlbero.key + max(cammdx,cammsx)




if __name__=='__main__':
    albero1 = Nodo(-1,Nodo(0,None,None),Nodo(None))    
    albero2 = Nodo(3,Nodo(3,Nodo(1),None),Nodo(1))
    albero3 = Nodo(3,Nodo(4,Nodo(5),Nodo(3)),Nodo(7))
    albero4 = Nodo(0,Nodo(2,Nodo(1),Nodo(7,Nodo(9))),Nodo(5,Nodo(6),Nodo(-40,Nodo(-35))))  
  


    listp1 = NodoP(1,NodoP(2,NodoP(3,NodoP(4,NodoP(5)))))
    listp2 = NodoP(3,NodoP(-5,NodoP(-7,NodoP(1,NodoP(-8)))))
    listp3 = NodoP(3)
    
    print(camminoMassimoAlbero(albero4))
