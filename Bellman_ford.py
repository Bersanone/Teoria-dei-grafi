'''
L'algoritmo di Bellman-Ford è un algoritmo per trovare i percorsi più brevi da un nodo start ad un node end.
A differenza di Dijkstra questo algoritmo funziona anche con archi negativi.

Tempi: O(V*E) dove V è il numero di nodi e E è il numero di archi
Spazio: O(V) per memorizzare le distanze
'''


class BellmanFord:

    #Inizializzazione della classe Edge

    class Edge:

        def __init__(self, from_node : int, to : int, weight : int):

            self.from_node = from_node
            self.to = to
            self.weight = weight


    #Funzione di supporto per creare un grafo rappresentato come lista di adiacenza
    def createGraph(self, v : int) -> list:
        graph = []
        for i in range(v):
            graph.append([])

        return graph
    

    def addEdge(self, graph : list, from_node : int, to : int, cost : float) -> None:
        graph[from_node].append(self.Edge(from_node,to,cost))


        '''
        * Algoritmo di Bellman-Ford (SSSP su grafi con pesi generici)
        *
        * Paradigma: Programmazione Dinamica (Bottom-Up).
        * Complessità: Tempo O(|V||E|) | Spazio O(|V|).
        *
        * Dinamica: L'algoritmo non compie scelte greedy irrevocabili (es. Dijkstra).
        * Rilassa l'intero set di archi iterativamente per |V|-1 volte, basandosi sul 
        * principio che un cammino minimo semplice contiene al massimo |V|-1 archi.
        * Equazione di ricorrenza: D[i][v] = min(D[i-1][v], min_{(u,v)}(D[i-1][u] + w(u,v)))
        *
        * Rilevamento Divergenze: Esegue una |V|-esima iterazione di validazione. 
        * Se la condizione D[u] + w(u,v) < D[v] risulta ancora soddisfatta, segnala
        * se trova la presenza di un ciclo negativo raggiungibile dalla sorgente imposta -inf (divergenza a -inf).
        '''


    

    def bellmanFord(self,graph : list, v : int, start : int) -> list:
     
     #Impostiamo le distanze a infinito tranne quella del nodo di partenza che è 0
    
     dist = [float('inf')] * v

     dist[start] = 0

     #Cicliamo per |V|-1 volte rilassando tutti gli archi


     for _ in range(v -1):
            #Iteriamo su ogni vertice del grafo
            for e in graph:
                #per ogni arco presente nel vertice corrente
                for edge in e:
                    #Se la distanza fino al nodo sorgente dell'arco  + il peso dell'arco è minore della distanza al nodo di arrivo, aggiorniamo la distanza al nodo di arrivo
                    if dist[edge.from_node] + edge.weight < dist[edge.to]:
                        dist[edge.to] = dist[edge.from_node] + edge.weight
     #eseguiamo un secondo set di iterazioni per rilevare tutti i nodi che possiedono un ciclo bnegativo raggiungibile dalla sorgente dell'arco 
     for _ in range(v-1):
            for e in graph:
                for edge in e:
                    #Se troviamo un arco minore della distanza al nodo di arrivo, significa che è presente un ciclo negativo raggiungibile dalla sorgente, quindi impostiamo la distanza al nodo di arrivo a -inf
                    if dist[edge.from_node] + edge.weight < dist[edge.to]:
                        dist[edge.to] = float("-inf")

     #Restituiamo la lista delle distanze
     return dist
    


    def main(self):
        e = 10
        v = 9
        start = 0

        graph = self.createGraph(v)

        self.addEdge(graph, 0, 1, 1)
        self.addEdge(graph, 1, 2, 1)
        self.addEdge(graph, 2, 4, 1)
        self.addEdge(graph, 4, 3, -3)
        self.addEdge(graph, 3, 2, 1)
        self.addEdge(graph, 1, 5, 4)
        self.addEdge(graph, 1, 6, 4)
        self.addEdge(graph, 5, 6, 5)
        self.addEdge(graph, 7, 6, 4)
        self.addEdge(graph, 5, 7, 3)

        res = self.bellmanFord(graph,v,start)

        for i in range(v):
            print(f"Distance from node {start} to node {i} is: {res[i]}")




p = BellmanFord()

p.main()