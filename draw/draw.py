import networkx as nx
import matplotlib.pyplot as plt

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

def drawNetGraf(grafo):
    '''
    Disegna un grafo utilizzando l'oggetto grafo della libreria networkx.

    Parametri:
    grafo (networkx.Graph): L'oggetto grafo da disegnare.

    Ritorna:
    None
    '''
    nx.draw(grafo, with_labels=True,
        node_size=2500,
        font_size=25
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
    grafo = nx.Graph()
    print("Inserisci gli archi, prima il nodo di partenza seguito dal nodo di arrivo -> nodo nodo")
    print("Quando hai finito, scrivi 'fine'")
    print("Per rimuovere un arco, scrivi 'del nodo nodo'")
    arcs = None
    inserito = True
    lastInputFailed = False
    lastInputElimined = False
    while inserito:
        print("Nodi inseriti: " + str(len(grafo.nodes)))
        print("Archi inseriti: " + str(len(grafo.edges)))
        if lastInputElimined:
            print("Ultimo arco rimosso: " + str(arcs))
            lastInputElimined = False
        else:
            print("Ultimo arco aggiunto: " + str(arcs))
        if lastInputFailed:
            print("Inserisci un arco che è costituito da due stringhe separate da uno spazio")
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
            if len(arcs) != 2:
                lastInputFailed = True
            else:
                if arcs[0] not in grafo.nodes:
                    grafo.add_node(arcs[0])
                if arcs[1] not in grafo.nodes:
                    grafo.add_node(arcs[1])
                grafo.add_edge(arcs[0], arcs[1])
    return grafo


#drawNetGraf(inputGrafoEdgeList())