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
    nx.draw(grafo)
    plt.show()
    return

def inputGrafoEdgeList():
    grafo = nx.Graph()
    print("inserisci gli archi prima il nodo di partenza spazio nodo di arrivo quando hai finito scrivi 'fine'")
    print('per rimuovere un nodi scrivere (del num num) ')
    inseritoTutto = False
    while inseritoTutto:
        print("nodi inseriti:"+str(grafo.number_of_nodes))
        print("archi inseriti:"+str(grafo.number_of_edges))
        print('ultimo arco aggiunto: '+str(arc))
        arco = input()
        if arco == 'fine':
            return grafo
        else:
            arc = arco.split(' ')
            if arc[0] not in list(grafo.nodes):
                grafo.add_node(arc[0])
            if arc[1] not in list(grafo.nodes):
                grafo.add_node(arc[1])
            grafo.add_edge(arc[0],arc[1])

drawNetGraf(edgeListToNetGraf(edgeList))
# G = nx.Graph()
# G.add_node(0)
# G.add_node(1)
# G.add_node(2)
# G.add_node(3)
# G.add_edge(0,1)
# G.add_edge(2,1)
# G.add_edge(3,1)
# nx.draw(G)
# plt.show()


#drawGrafo(edgeList)
# drawGrafo(G)



# G = nx.Graph()
# #DG = nx.DiGraph()
# #G.add_edges_from([("A","B"),("A","C"),("C","B")])
# G.add_edge((0,1))
# G.add_edge((2,1))
# G.add_edge((3,1))
# #DG.add_edges_from([(0,1),(1,2),(2,3),(3,0),(0,3)])
# H = nx.path_graph(10)
# G.add_nodes_from(H)
# pos = nx.spring_layout(G)
# nx.draw_networkx_nodes(G,pos,node_size=500)
# nx.draw_networkx_edges(G,pos,edgelist=G.edges(),edge_color='black')
# nx.draw_networkx_labels(G,pos)
# plt.show()