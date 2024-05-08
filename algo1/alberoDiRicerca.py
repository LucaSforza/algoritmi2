'''
un albero si dice bilanciato se la sua altezza é logaritmica

alberi RB red and black ha operazione di ribilanciamento

h = log n h é il numero di livelli dell'albero

l'albero deve permettere : ricerca cancellazione inserimento e riesce a farle tutto in tempo log n  
    con i vettori che siano ordinati o non le complessita sono queste:
        - ricerca         O(log n)    O(n)
        - inserimento     O(n)        O(1)
        - cancellazione   O(n)        O(n)
'''

def ricerca(p,x): # O(h)
    if p == None: return False
    if p.key == x: return True
    if x<p.key: return ricerca(p.left,x)
    else : return ricerca(p.right,x)

'''
ci sono tre modi di stampare inorder postorder preorder
    in-order se l'albero e di ricerca stampa gli elementi in ordine 
    pre-order strampa per primo la radice poi tutto il sottoalbro sinistro e dopo il destro
    post-order visita prima il sottoalbero sinistro, poi il sottoalbero destro e infine il nodo radice
'''

def nodoABR(x):
    return

def inserimento(p,x):
    z = nodoABR(x)
    if p == None : return z
    q = p 
    while p!=None and p.key!=x:
        if x<p.key and p.left!=None: p = p.left
        elif p.key<x and p.right!=None: p = p.right
        else: break
    if p.key==x: return q
    if x<p.key: p.left = z
    else : p.right = z

def dimensione(p):
    return 

def inserisci(p,A,x=0):
    if p == None: return 
    A[x] = p.key
    if p.left != None:
        inserisci(p.left,A,2*x+1)
    if p.right != None:
        inserisci(p.right,A,2*x+2)
    return 


def creaOrd(p):
    if p == None : return []
    n = dimensione(p)
    A = [None]*(n+1)
    inserisci(p,A)
    return A