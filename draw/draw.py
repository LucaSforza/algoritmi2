import networkx as nx
import matplotlib.pyplot as plt
from strut import *

edgeList =[(0,1),(1,2),(2,3),(3,0),(0,3)]

def edgeListToNetGraf(edgeList:list[tuple[int,int]],grafo=nx.Graph()):
    for tupla in edgeList:
        if tupla[0] not in list(grafo.nodes):
            grafo.add_node(tupla[0])
        if tupla[1] not in list(grafo.nodes):
            grafo.add_node(tupla[1])
        grafo.add_edge(tupla[0],tupla[1])
    return grafo

def drawNetGraf(grafo):
    nx.draw(grafo,with_labels=True,
            node_size = 2500,
            font_size = 25
            )
    plt.margins(0.2)
    plt.show()
    return

def inputGrafoEdgeList():
    grafo = nx.Graph()
    print("inserisci gli archi prima il nodo di partenza spazio nodo di arrivo ->nodo nodo")
    print("quando hai finito scrivi -> fine")
    print('per rimuovere un nodi scrivere (del num num) ')
    arc = None
    inserito = True
    lastInputFailed = False
    lastInputElimined = False
    while inserito:
        print("nodi inseriti:"+str(len(grafo.nodes)))
        print("archi inseriti:"+str(len(grafo.edges)))
        if lastInputElimined:
            print('ultimo arco rimosso: '+str(arc))
            lastInputElimined = False
        else:
            print('ultimo arco aggiunto: '+str(arc))
        if lastInputFailed:
            print('inserici un arco che è costituito due stringhe separate da uno spazio')
            lastInputFailed = False
        arco = input()
        if arco == 'fine':
            inserito = False
        elif arco[0:3]=="del":
            arc = arco[4:]
            arc.split(' ')
            grafo.remove_edge(arc[0],arc[1])
            lastInputElimined = True
        else:
            arc = arco.split(' ')
            if len(arc)!=2:
                lastInputFailed = True
            else:
                if arc[0] not in grafo.nodes:
                    grafo.add_node(arc[0])
                if arc[1] not in grafo.nodes:
                    grafo.add_node(arc[1])
                grafo.add_edge(arc[0],arc[1])
    return grafo

#drawNetGraf(edgeListToNetGraf(edgeList))

#a = inputGrafoEdgeList()

b = edgeListToNetGraf([(1,2),(2,3)])
print(b.has_edge(1,2))
drawNetGraf(b)