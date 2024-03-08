class Nodo:
    def __init__(self,numero:int):
        self.numero:int

    def my_method(self):
        print(self.numero)
        
class Grafo:
    def __init__(self,nodi:set[int]=None,archi: set[tuple[int, int]]=None):
        self.nodi: set[int]
        self.archi: set[tuple[int, int]]
        if nodi is None:
            self.nodi = set()
        else:
            self.nodi = nodi
        if archi is None:
            self.archi = set()
        else:
            self.archi = archi


    def addNodo(self,num:int):
        self.nodi.add(num)

    def addArco(self,arco:tuple[int, int]):
        self.archi.add(arco)

    def my_method(self):
        print(self.nodi)
        print(self.archi)



def getGrafDaListArchi(archi:list[tuple[int,int]],grafo:Grafo=Grafo())->Grafo:
    for arco in archi:
        if arco[0] not in grafo.nodi:
            grafo.addNodo(Nodo(arco[0]))
        if arco[1] not in grafo.nodi:
            grafo.addArco(Nodo(arco[1]))
        grafo.addArco(arco)
    return grafo


