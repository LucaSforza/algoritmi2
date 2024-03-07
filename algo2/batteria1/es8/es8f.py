import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()
G.add_edges_from([("A","B")],("A","C"),("C","B"))
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G,pos,node_size=500)
nx.draw_networkx_edges(G,pos,edgelist=G.edges(),edge_color='black')
nx.draw_networkx_labels(G,pos)
plt.show()









grafo1 = [[1],[3],[1,4],[4],[2,3],[4]]
grafo2 = [[1,3],[2],[3],[0]]  # expected [[1, 3], [2], [3], []]
visitati = [0]*len(grafo2)
def es82f(grafo:list[list[int]],nodo:int):
    if visitati[nodo]==1:
        return 
    else:
        visitati[nodo]=1
        for arco in grafo[nodo]:
            if nodo in grafo[arco] and arco in grafo[nodo]:
                if visitati[arco]==1:
                    grafo[nodo].remove(arco)
                else:
                    grafo[arco].remove(nodo)
            else:
                es82f(grafo,arco)







