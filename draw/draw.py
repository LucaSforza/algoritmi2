import networkx as nx
import pickle
import os
import matplotlib.pyplot as plt
import matplotlib.patches as matpat

def draw(G: list[list[int]], direct=False):
    drawNetGraf(adjacent_list_to_graft(G,direct))
    
def adjacent_list_to_graft(G: list[list[int]], direct: bool) -> nx.Graph:
    if direct:
        graph = nx.DiGraph()
    else:
        graph = nx.Graph()

    for i in range(len(G)):
        graph.add_node(i)
    
    for i,edges in enumerate(G):
        for v in edges:
            graph.add_edge(i,v)
    
    return graph
        
    
# mi sa che esiste gia una funzione che fa la stessa cosa della libreria 
def edgeListToNetGraf(edgeList:list[tuple[int,int]],grafo=nx.Graph()):
    """
    Converte una lista di archi in un grafo networkx.

    Parametri:
    - edgeList: Una lista di tuple rappresentanti gli archi del grafo.
    - grafo: (Opzionale) Il grafo networkx in cui aggiungere gli archi. Se non specificato, viene creato un nuovo grafo vuoto.

    Returns:
    - grafo: Il grafo networkx con gli archi aggiunti.
    """
    for tupla in edgeList:
        if tupla[0] not in list(grafo.nodes):
            grafo.add_node(tupla[0])
        if tupla[1] not in list(grafo.nodes):
            grafo.add_node(tupla[1])
        grafo.add_edge(tupla[0],tupla[1])
    return grafo

def drawNetGraf(grafo:nx.Graph):
    '''
    Disegna un grafo utilizzando l'oggetto grafo della libreria networkx.

    Parametri:
    grafo (networkx.Graph): L'oggetto grafo da disegnare.

    Ritorna:
    None
    TODO grafi diretti
    '''
    nx.draw(grafo,
        with_labels=True,
        node_size=400,
        font_size=10,
        linewidths = 0.5,
        font_color='black',
        node_color='green',
        edge_color='black',
        width=4,
        pos=nx.spring_layout(grafo)
        )
    plt.margins(0.2)
    plt.show()
    return

def inputGrafoEdgeList():
    '''
    Permette all'utente di inserire da terminale una lista di archi nel formato 'nodo nodo' separato da uno spazio.
    Per eliminare un arco inserito, scrivere 'del nodo nodo'.
    Per terminare l'inserimento, scrivere 'fine'.
    
    Ritorna un oggetto networkx.Graph().
    
    TODO: Comando che stampa tutti gli archi inseriti fino ad ora.
    TODO: Comando che permette di eliminare un nodo solo se non è più collegato a nessun arco.
    '''
    grafo_diretto = True
    print("Inserisci gli archi, prima il nodo di partenza seguito dal nodo di arrivo -> nodo nodo")
    print("per inserire solo un nodo inserici un stringa senza spazi")
    print("Quando hai finito, scrivi 'fine'")
    print('scrivi: g, dg')
    scelta = input()
    if scelta.lower() == 'dg':
        print('modaloita scelta: grafo diretto')
        grafo = nx.DiGraph()
    elif scelta.lower() == 'g':
        grafo_diretto = False
        grafo = nx.Graph()
        print('modalita scelta: grafo non diretto')
    else:
        lastInputFailed = True
        print('input non valido \n scrivi: g, dg')
    
    arcs = None
    inserito = True
    lastInputFailed = False
    lastInputElimined = False
    while inserito:        
        
        if lastInputElimined:
            print("Ultimo arco rimosso: " + str(arcs))
            lastInputElimined = False
        else:
            print("Ultimo arco aggiunto: " + str(arcs))
        if lastInputFailed:
            print("Nodi inseriti: " + str(len(grafo.nodes)))
            print("Archi inseriti: " + str(len(grafo.edges)))
            print("Inserisci un arco che è costituito da due stringhe separate da uno spazio")
            print("Per rimuovere un arco, scrivi 'del nodo nodo'")
            lastInputFailed = False
        arco = input()
        if arco == "fine":
            inserito = False
        elif arco[0:3] == "del":
            arc = arco[4:]
            arcs = arc.split(" ")
            grafo.remove_edge(arcs[0], arcs[1])
            lastInputElimined = True
        else:
            arcs = arco.split(" ")
            if len(arcs) == 2:
                if arcs[0] not in grafo.nodes:
                    grafo.add_node(arcs[0])
                if arcs[1] not in grafo.nodes:
                    grafo.add_node(arcs[1])
                if grafo_diretto:
                    grafo.add_edge(arcs[0], arcs[1])
                else:
                    grafo.add_edge(arcs[0], arcs[1])
                    grafo.add_edge(arcs[1], arcs[0])
            elif len(arcs) == 1:
                grafo.add_node(arcs[0])
            else:
                lastInputFailed = True
    return grafo

def netGrafToListAdiacenzaList(grafo:nx.Graph)->list[list[int]]:
    dizTradIndexToNodo = dict()    
    dizTradNodotoIndex = dict()    
    nodi = list(grafo.nodes())
    listGrafOut = []
    for index,nodo in enumerate(nodi):
        dizTradIndexToNodo[index] = nodo
        dizTradNodotoIndex[nodo] = index
        listGrafOut.append(list())
    archi = list(grafo.edges())
    for arco in archi:
        listGrafOut[dizTradNodotoIndex[arco[0]]].append(dizTradNodotoIndex[arco[1]])
        listGrafOut[dizTradNodotoIndex[arco[1]]].append(dizTradNodotoIndex[arco[0]])
    return listGrafOut

def netGrafToListAdiacenzaSet(grafo:nx.Graph)->list[set[int]]:
    dizTradIndexToNodo = dict()    
    dizTradNodotoIndex = dict()    
    nodi = list(grafo.nodes())
    listGrafOut = []
    for index,nodo in enumerate(nodi):
        dizTradIndexToNodo[index] = nodo
        dizTradNodotoIndex[nodo] = index
        listGrafOut.append(set())
    archi = list(grafo.edges())
    for arco in archi:
        listGrafOut[dizTradNodotoIndex[arco[0]]].add(dizTradNodotoIndex[arco[1]])
        listGrafOut[dizTradNodotoIndex[arco[1]]].add(dizTradNodotoIndex[arco[0]])
    return listGrafOut

def saveGraphToFile(grafo, filename):
    """
    Salva un grafo in un file pickle nella cartella 'saved'.

    Parametri:
    - grafo: Il grafo da salvare.
    - filename: Il nome del file pickle.

    Ritorna:
    None
    """
    if type(grafo) == nx.Graph or type(grafo) == nx.DiGraph:
        filename = filename +'_'+ 'networkx'
    else:
        filename = filename +'_'+ str(type(grafo))
    filepath = f"draw/saved/{filename}.pickle"
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "wb") as file:
        pickle.dump(grafo, file)
    print(f"Graph saved to {filepath}")

def loadGraphFile(filename):
    """
    Cerca un file nella cartella 'draw/saved' e lo ritorna.

    Parametri:
    - filename: Il nome del file da cercare.

    Ritorna:
    - grafo: Il grafo caricato dal file pickle.
    """
    filepath = f"draw/saved/{filename}.pickle"
    if os.path.exists(filepath):
        with open(filepath, "rb") as file:
            grafo = pickle.load(file)
        return grafo
    else:
        print(f"File {filename} not found.")
        return None

if __name__ ==  "__main__":
    G = inputGrafoEdgeList()
    # saveGraphToFile(G,'provagrafodiretto')
    #G = loadGraphFile('provagrafodiretto_networkx')
    drawNetGraf(G)
    pass