from draw.draw import *
from algo2.batteria1.es7.es7f import *



#print(es7f(netGrafToListAdiacenzaList(loadGraphFile("grafo_esempio_es7_networkx")),))
'''
per inserire un grafo nella cartella dei gafi salvati onserendolo in input da terminale
'''
# grafo = inputGrafoEdgeList()
# saveGraphToFile(grafo,"grafo_prova_es7_3")

'''
disegnare un grafo da uno salvato su un file
'''
# netgraf = loadGraphFile("grafo_prova_es7_3_networkx")
# drawNetGraf(netgraf)

'''
provare un esercizio usando lista di adiacenza
'''
netgraf = loadGraphFile("grafo_prova_es7_3_networkx")
listaAdiacenza = netGrafToListAdiacenzaList(netgraf)
print(es7f(listaAdiacenza))


# netGr = edgeListToNetGraf([("A","B"),("A","C"),("A","D"),("C","D")])
# drawNetGraf(netGr)
# adiList = netGrafToListAdiacenzaList(netGr)

#es7f(adiList)