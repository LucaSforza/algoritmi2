import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
DG = nx.DiGraph()
#G.add_edges_from([("A","B"),("A","C"),("C","B")])
#G.add_edges_from([(0,1)])
#DG.add_edges_from([(0,1),(1,2),(2,3),(3,0),(0,3)])
H = nx.path_graph(10)
G.add_nodes_from(H)
pos = nx.circular_layout(G)
nx.draw_networkx_nodes(G,pos,node_size=500)
nx.draw_networkx_edges(G,pos,edgelist=G.edges(),edge_color='black')
nx.draw_networkx_labels(G,pos)
plt.show()