


class BellmanFordEdgeList:

    #Inizializzazione della classe Edge

    class Edge:

        def __init__(self, from_node : int, to : int, weight : int):

            self.from_node = from_node
            self.to = to
            self.weight = weight


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


    

    def bellmanFord(self,edges : Edge, v : int, start : int) -> list:
    
     dist = [float('inf')] * v

     dist[start] = 0

     relaxedEdege = True



     for _ in range(v -1):
            if not relaxedEdege:
                 break
            relaxedEdege = False
            for edge in edges:
                    if dist[edge.from_node] + edge.weight < dist[edge.to]:
                        dist[edge.to] = dist[edge.from_node] + edge.weight
                        relaxedEdege = True

     for _ in range(v-1):
            if not relaxedEdege:
                    break
            relaxedEdege = False
            for edge in edges:
                    if dist[edge.from_node] + edge.weight < dist[edge.to]:
                        dist[edge.to] = float("-inf")
                        relaxedEdege = True

     return dist
    


    def main(self):
        e = 10
        v = 9
        start = 0

        edges = [None] * e

        edges[0] = self.Edge( 0, 1, 1)
        edges[1] = self.Edge( 1, 2, 1)
        edges[2] = self.Edge( 2, 4, 1)
        edges[3] = self.Edge( 4, 3, -3)
        edges[4] = self.Edge( 3, 2, 1)
        edges[5] = self.Edge( 1, 5, 4)
        edges[6] = self.Edge( 1, 6, 4)
        edges[7] = self.Edge( 5, 6, 5)
        edges[8] = self.Edge( 7, 6, 4)
        edges[9] = self.Edge( 5, 7, 3)

        res = self.bellmanFord(edges,v,start)

        for i in range(v):
            print(f"Distance from node {start} to node {i} is: {res[i]}")




p = BellmanFordEdgeList()

p.main()