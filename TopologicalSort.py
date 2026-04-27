#Implementazione di un algoritmo di topological sort utilizzando DFS su liste adiacenti di un grafico diretto aciclico.

#Possiamo utilizzare questo algoritmo per definire gerarchie o dipendenze

#Restituiamo un array con gli indici dei nodi in un ordine topologico, per ogni direcetd edge u -> v, u viene prima di v nell'ordine

#Includiamo anche un metodo per trovare il shortest path nel DAG utilizzando l'ordinamento topologico



class topologicalSortAdjacencyList:

    #Inizializzazione della classe Edge

    class Edge:
        #Init della classe Edge

        def __init__(self, from_node : int,to : int,weight : int):

            self.from_node = from_node
            self.to = to
            #Peso dell'edge (il peso può rappresentare qualsiais cosa, ad esmepio la distanza)
            self.weight = weight


    #Funzione di main


    def main(self):

        #Impostiamo il numero di nodi a 7

        n : int = 7

        #Istanziamo un grafo

        graph : dict[int, list[Edge]] = {}

        #Aggiungiamo un array al grafo per ogni nodo

        for i in range(n):
            graph[i] = []

        
        #Impostiamo gli archi come: Edge(from,to,weight)


        graph[0].append(self.Edge(0,1,3))
        graph[0].append(self.Edge(0,2,2))
        graph[0].append(self.Edge(0,5,3))
        graph[1].append(self.Edge(1,3,1))
        graph[1].append(self.Edge(1,2,6))
        graph[2].append(self.Edge(2,3,1))
        graph[2].append(self.Edge(2,4,10))
        graph[3].append(self.Edge(3,4,5))
        graph[5].append(self.Edge(5,4,7))


        #Calcoliamo la topological sort


        ordering : list[int] = self.topologicalsort(graph, n)
        print(str(ordering))

        #Calcoliamo il percorso più breve
        dists : list[int] = self.dagShortestPath(graph,0,n)

        print(dists[4])
        print(dists[6])


    #Funzioni pubbliche


    def topologicalsort(self, graph : dict[int, list[Edge]], numNodes : int) -> list[int]:

        #Creiamo una lista di ordering, inizializziamo tutto con 0 

        ordering : list[int] = [0] * numNodes

        #Creiamo una lista per segnalare i visitati, inizializziamo a false 
        visited : list[bool] = [False] * numNodes
        #Settiamo l'indice per la lista di ordering

        i : int = numNodes - 1

        #Per ogni nodo non visitato eseguiamo la dfs e salviamo l'indice per il nodo successivo

        for at in range(numNodes):
            if not visited[at]:
                i = self.__dfs(i, at, visited, ordering, graph)

        #Restituiamo la lista

        return ordering


    #Metodo privato

    def __dfs(self,i : int, at : int, visited : list[bool], ordering : list[int], graph : dict[int, list[Edge]]) -> int:

        #Impostiamo il nodo corrrente come visitato

        visited[at] = True





        #Recuperiamo gli archi in uscita del node corrente

        edges: list[self.Edge] = graph[at]


        #Per ogni nodo adiacente non ancora visitato eseguiamo ricursivamente la dfs
        for e in edges:
                if not visited[e.to]:
                    i = self.__dfs(i, e.to, visited, ordering, graph)


        #Inseriamo il nodo corrente nell'array partendo dal fondo (post-order)


        ordering[i] = at

        #restituiamo l'indice decrementato per il prossimo nodo da inserire
        return i - 1
    

    #Funzione per trovare il shortestpath

    #Se volessimo trovare il percorso più lungo dovremmo moltiplicare tutti i valore dei vertici per -1
    #Una volta trovato il percorso più corto (siamo nel range negativo) lo rimpoltiplichiamo per -1 ottenendo il numero intero
    #Flippando il numero avremmo la strada più lunga
    def dagShortestPath(self, graph : dict[int, list[Edge]], start : int, numNodes : int) -> list[int]:

        #Calcoliamo l'ordinamento topologico del grafo.

        topsort : list[int] = self.topologicalsort(graph, numNodes)

        #Inizializziamo l'array delle distanze a infinito. Questo garantisce che ogni nuova distanza calcolata sarà inizialmente minore del valore di default.
        dist : list[int] = [float('inf')] * numNodes

        #Impostiamo a 0 la distanza del nodo di partenza (start), poiché la distanza da un nodo a sé stesso è nulla.

        dist[start] = 0

        for i in range(numNodes):
            #Otteniamo il nodo corrente seguendo rigorosamente l'ordine topologico.
            nodeIndex : int = topsort[i] 

            #Se il nodo corrente è irraggiungibile (distanza infinita), saltiamo l'iterazione poiché non può aggiornare i suoi vicini.

            if dist[nodeIndex] == float('inf'):
                continue

            #Per ogni arco in uscita dal nodo corrente, calcoliamo la potenziale nuova distanza verso la destinazione.

            for edge in graph.get(nodeIndex, []):
                newDist : int = dist[nodeIndex] + edge.weight

                #Processo di 'Relaxation': se abbiamo trovato un percorso più breve, aggiorniamo la distanza minima verso il nodo di destinazione.

                if newDist < dist[edge.to]:

                    dist[edge.to] = newDist

        #restituiamo le distanze minime

        return dist
    




p = topologicalSortAdjacencyList()

p.main()









    