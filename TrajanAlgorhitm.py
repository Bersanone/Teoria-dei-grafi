from collections import deque, defaultdict


# =============================================================================
# TARJAN'S ALGORITHM — STRONGLY CONNECTED COMPONENTS (SCC)
# =============================================================================
#
# DESCRIZIONE:
#   L'algoritmo di Tarjan (1972) individua tutte le Strongly Connected
#   Components (SCC) di un grafo orientato in un'unica passata DFS.
#   Un SCC è un sottoinsieme massimale di nodi dove ogni nodo è raggiungibile
#   da qualsiasi altro nodo del sottoinsieme.
#
# FUNZIONAMENTO:
#   1. Esegue una DFS assegnando a ogni nodo un ID (timestamp di visita)
#      e un valore low-link (nodo più antico raggiungibile nel DFS tree).
#   2. Mantiene uno stack dei nodi visitati ma non ancora assegnati a un SCC.
#   3. Quando low[v] == ids[v], il nodo v è la "radice" di un SCC:
#      tutti i nodi nello stack fino a v formano quel componente.
#
# COMPLESSITÀ:
#   - Tempo  : O(V + E)  — ogni nodo e arco visitato esattamente una volta
#   - Spazio : O(V)      — stack, arrays ids/low/onStack/sccs
#
# RAPPRESENTAZIONE VISIVA:
#
#   Grafo orientato:          DFS tree + back-edges:
#
#   6 ──► 0 ◄── 2            ids:  [1, 2, 3, 4, 5, 6, 7, 8]
#   │     │     ▲            low:  [1, 1, 1, 4, 4, 4, 4, 7]
#   ▼     ▼     │
#   2 ──► 1 ───►             SCC trovati (low[v] == ids[v]):
#   │                          SCC-0: {0, 1, 2}   ← ciclo 0→1→2→0
#   ▼                          SCC-1: {3, 7}       ← ciclo 3↔7
#   4 ◄── 5 ◄── 7              SCC-2: {4, 5, 6}   ← ciclo 4→5→6→4
#   │     ▲     │
#   └──►  6 ◄──┘
#
# RIFERIMENTO: Tarjan, R. E. (1972). "Depth-first search and linear graph
#              algorithms". SIAM Journal on Computing, 1(2), 146–160.
# =============================================================================


class TarjanSolverScc:


    #Istanziamento del costruttore della classe

    def __init__(self, graph : list[list[int]]):
        if graph is None:
            raise ValueError("Graph cannot be None")
        
        self.n = len(graph)
        self.graph = graph
        self.solved = False

        # Contatore globale DFS: assegna un ID incrementale a ogni nodo
        # nell'ordine in cui viene scoperto dalla visita
        self.id = 0

        #Counter che segna il numero di Strongly connected components

        self.sccount = 0

        # Traccia quali nodi sono attualmente presenti nello stack DFS.
        # Un nodo rimane "onStack" finché il suo SCC non viene finalizzato

        self.onStack = [False] * self.n
        
        # ids[v] = timestamp di scoperta del nodo v durante la DFS (statico).
        # Inizializzato a -1 (= unvisited) per distinguere i nodi non ancora visitati        
        self.ids = [-1] * self.n

        # low[v] = minimo ids raggiungibile da v tramite il DFS subtree
        # e al più un back-edge verso un antenato.
        # Determina se v è la radice di un SCC: low[v] == ids[v]

        self.low = [0] * self.n

        # sccs[v] = indice del SCC a cui appartiene il nodo v.
        # Nodi con lo stesso valore appartengono allo stesso componente

        self.sccs = [0] * self.n

         # Stack esplicito dei nodi visitati in attesa di essere assegnati a un SCC

        self.stack = deque()
        self.unvisited = -1


   #Funzioni main

    #Restituiamo l'ID SCC perogni nodo, se due nodi hanno lo stesso ID appartengono allo stesso SCC


    def getSccs(self) -> list[int]:
        if not self.solved:
            self.solve()
        
        return self.sccs
    

    
    #Restituiamo il numero di strongly connected components presenti
    
    def sccCount(self) -> int:
        if not self.solved:
            self.solve()

        return self.sccount
    

    #Funzione di main per provare l'algoritmo
    

    def main(self, args : list[str]) -> None:

        n = 8

        graph = self.createGraph(n)


        self.addEdge(graph, 6, 0);
        self.addEdge(graph, 6, 2);
        self.addEdge(graph, 3, 4);
        self.addEdge(graph, 6, 4);
        self.addEdge(graph, 2, 0);
        self.addEdge(graph, 0, 1);
        self.addEdge(graph, 4, 5);
        self.addEdge(graph, 5, 6);
        self.addEdge(graph, 3, 7);
        self.addEdge(graph, 7, 5);
        self.addEdge(graph, 1, 2);
        self.addEdge(graph, 7, 3);
        self.addEdge(graph, 5, 0);
    

        solver = TarjanSolverScc(graph)

        sccs = solver.getSccs()

        multimap = defaultdict(list)

        for i in range(n):

            multimap[sccs[i]].append(i)

        print(f"Numero di strongly connected components: {solver.sccCount()}")


        for sc in multimap.values():

            print(f"Node {sc} forma un strongly connected components")









    #funzioni per la creazione del grafo
    


    #Funzione di solve per l'algoritmo di Tarjan 

    def solve(self) -> None:

        #Se risolto restituiamo

        if self.solved:
            return 
        
        #per ogni nodo non visitato eseguiamo la dfs
        
        for i in range(self.n):
            if self.ids[i] == self.unvisited:
                self.dfs(i)

        #Impostaimo come solved una volta completato dfs
        
        self.solved = True






    #Definizione della DFS per Tarjan

    def dfs(self, at : int) -> None:

        """DFS ricorsiva

        Per ogni nodo 'at':
          1. Assegna ids e low con il contatore corrente, poi lo aggiunge allo stack.
          2. Esplora i vicini: se non visitati, ricorre; se già nello stack,
             aggiorna low[at] = min(low[at], low[to]) per propagare
             il collegamento all'antenato più remoto.
          3. Al ritorno dalla ricorsione (backtracking), se ids[at] == low[at],
             'at' è la radice di un SCC: estrae dallo stack tutti i nodi
             del componente e li etichetta con l'ID corrente.
        """

        #Incrementiamo l'ID

        self.id += 1

        #Impostiamo l'ID incrementale 

        self.ids[at] = self.low[at] = self.id

        #Aggiungiamo il nodo corrente allo stack

        self.stack.append(at)

        #Impostiamo a True essendo che è nello stack

        self.onStack[at] = True


        #Iteriamo sui nodi raggiungibili dal nodo corrente


        for to in self.graph[at]:

            #Se non è stato visitato applichiamo la dfs

            if self.ids[to] == self.unvisited:
                self.dfs(to)
            #Se presente all'interno dello stack impostiamo come low il min tra il low[at] e low[to] (low-link)
            if self.onStack[to]:
                self.low[at] = min(self.low[at], self.low[to])

        #se l'id di at corrisponde anche il proprio low allora è la radice del proprio scc

        if self.ids[at] == self.low[at]:

             while True:
                    #Rimuoviamo i componenti dallo stack
                    node = self.stack.pop()
                    self.onStack[node] = False
                    #assegniamo l'id ai nodi che costruiscono un SCC per tracciarli
                    self.sccs[node] = self.sccount

                    #Se arriviamo al componente attuale interrompiamo il ciclo

                    if node == at:
                        break
                    
             #Incrementiamo

             self.sccount +=1


    #Funzione per creare il una lista di adiacenza con n nodi

    def createGraph(self, n : int) -> list[list[int]]:

        graph = [[] for _ in range(n)]

        return graph
    

    #Funzione per aggiungere edge diretti from - to
    

    def addEdge(self,graph : list[list[int]], from_node : int, to_node : int) -> None:
        graph[from_node].append(to_node)




p = TarjanSolverScc([[] for _ in range(8)])

p.main([])
