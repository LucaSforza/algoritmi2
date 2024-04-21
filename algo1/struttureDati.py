# Lista a Puntatori
#   è composta da nodi, che a loro volta sono formati da una parte contenente 
#   l'informazione e un puntatore al record successivo

class Nodo:
    def __init__(self,key = None , next = None):
        self.key = key
        self.next = next
    
def stampa(p):
    while p!=None:
        print(p.key)
        p = p.next
        
def stampaString(p): #
    s = ''
    while p!=None:
        s +=str(p.key)+' -> '
        p = p.next
    s = s[:-4]
    print(s)
    return s

def crea(lista:list[int]):
    if lista == []: return None
    lOut = Nodo(lista[0])
    p = lOut
    for numero in range(1,len(lista)):
        p.next = Nodo(lista[numero])
        p = p.next
    return lOut

def aggiungiInTesta(punt,data):
    q = Nodo(data,punt)
    return q


def aggiungiDopo(punt,data,dopo):
    start = punt
    while punt!= None:
        if punt.key==dopo:
            riattaccare = punt.next
            punt.next = Nodo(data,riattaccare)
            break
        punt = punt.next
    return start

if __name__ == '__main__':
    # p = Nodo(5)
    # print(p.key)
    # print(p.next)
    # q = Nodo(6)
    # p.next = q
    # print(p.next)

    # p = Nodo(7)
    # p.next = Nodo(2)
    # p.next.next = Nodo(12)

    prov1 = [1,2,3,4,5,6,7,8,9]
    listaPuntata = crea(prov1)
    stampaString(listaPuntata)
    #stampaString(aggiungiInTesta(listaPuntata,10))
    stampaString(aggiungiDopo(listaPuntata,10,6))
    #aggiungiDopo(listaPuntata,10,6)



'''
fatto da copilot 
class Nodo:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class ListaCollegata:
    def __init__(self):
        self.head = None

    def inserisci_in_testa(self, data):
        nuovo_nodo = Nodo(data)
        nuovo_nodo.next = self.head
        self.head = nuovo_nodo

    def stampa_lista(self):
        nodo_corrente = self.head
        while nodo_corrente:
            print(nodo_corrente.data)
            nodo_corrente = nodo_corrente.next

    def rimuovi_nodo(self, key):
        nodo_corrente = self.head
        if nodo_corrente and nodo_corrente.data == key:
            self.head = nodo_corrente.next
            nodo_corrente = None
            return
        prev = None
        while nodo_corrente and nodo_corrente.data != key:
            prev = nodo_corrente
            nodo_corrente = nodo_corrente.next
        if nodo_corrente:
            prev.next = nodo_corrente.next
            nodo_corrente = None
'''

'''
es data una lista a puntatori ordinare la lista a puntatori
'''