from collections import defaultdict, deque

from random import *
import time

"Creo il grafo"
class Graph(object):
    def __init__(self):
        "Lista che contiene i nodi"
        self.nodi = set()
        "Dizionario che conterrà gli archi"
        self.archi = defaultdict(list)
        "Dizionario che conterrà i costi "
        self.distanze = {}

    "Aggiungo i nodi"
    def AggiungiNodo(self, valore):
        self.nodi.add(valore)

    def AggiungiArchi(self, NodoA, NodoB, distanza):
        "Creo il collegamento tra due nodi [A:B] arco da A a B"
        self.archi[NodoA].append(NodoB)
        "Questo è un dizionario quindi associo alla coppia <A,B> il costo"
        "Ovvero associo il costo all'arco A,B"
        self.distanze[(NodoA, NodoB)] = distanza
        return self.distanze

"Algoritmo di Dijkstra"
def dijkstra(graph, initial):
    start_time = time.time()

    nodi_visitati = {initial: 0}
    predecessori = {}

    nodi = set(graph.nodi)

    while nodi:
        min_node = None
        for node in nodi:
            if node in nodi_visitati:
                if nodi_visitati[node] < 0:
                    print("Trovato costo arco negativo")
                    print("Tempo di esecuzione --- %.3f secondi ---" % (time.time() - start_time))
                    return ([],[])
                if min_node is None:
                    min_node = node
                elif nodi_visitati[node] < nodi_visitati[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodi.remove(min_node)
        Peso_corrente = nodi_visitati[min_node]

        for edge in graph.archi[min_node]:
            try:
                Peso = Peso_corrente + graph.distanze[(min_node, edge)]
            except:
                continue
            if edge not in nodi_visitati or Peso < nodi_visitati[edge]:
                nodi_visitati[edge] = Peso
                predecessori[edge] = min_node
    print("Tempo di esecuzione --- %.3f secondi ---" % (time.time() - start_time))
    return nodi_visitati, predecessori


"Con questa funzione calcolo la distanza minima tra due nodi"
def Cammino_minimo(graph, sorgente, destinazione):
     
        "Qua richiamo la funzione di Dijkstra che mi restituisce i visitati e il path con i collegamenti"
        nodi_visitati, pred = dijkstra(graph, sorgente)
        tutti_i_predecessori = deque()
        result = 0
        if nodi_visitati==[]:
            return ([],[])
        "Se il nodo di start è uguale al nodo di destinazione il camminimo minimo è zero"
        if(sorgente == destinazione):
            result = 0
        else:
            "Qua metto in destinazione il valore di path alla posizione destinazione"
            "ovvero, path contiene tutit i predecessori,quindi prendo il successore di destionazione"
            try:
                nodo_destinazione = pred[destinazione]
            except:
                print("Cammino non presente")
                return ([],[])
            "Finchè destinazione è diversa dalla sorgente"
            while nodo_destinazione != sorgente:
                "Inserisco in testa tutti i predecessori fino ad arrivare alla a quello prima della sorgente "
                tutti_i_predecessori.appendleft(nodo_destinazione)
                "Qua mi racalcoldo destinazione" 
                nodo_destinazione = pred[nodo_destinazione]


            "E infine metto la sorgente in cima"
            tutti_i_predecessori.appendleft(sorgente)
            "La destinazione in fondo"
            tutti_i_predecessori.append(destinazione)
            "E restituisco il valore del dizionario avente chiave= destinazione che non sarà altro che il valore"
            "totale del percorso piu breve per arrivare dalla sorgente ad esso"
            result = nodi_visitati[destinazione]
        return result,list(tutti_i_predecessori)


if __name__ == '__main__':
    graph = Graph()

    for nodo in ['A', 'B', 'C', 'D', 'E','D','E','F','G']:
        graph.AggiungiNodo(nodo)
        
    graph.AggiungiArchi('A', 'G', 17)
    graph.AggiungiArchi('B', 'A', 25)
    graph.AggiungiArchi('C', 'B', 10)
    graph.AggiungiArchi('D', 'C', 10)
    graph.AggiungiArchi('D', 'E', 20)
    graph.AggiungiArchi('D', 'G', 5)
    graph.AggiungiArchi('E', 'A', 20)
    graph.AggiungiArchi('F', 'D', 5)
    graph.AggiungiArchi('F', 'G', 18)
    graph.AggiungiArchi('G', 'B', 12)
    graph.AggiungiArchi('G', 'E', 3)



print(Cammino_minimo(graph, 'D', 'A'))