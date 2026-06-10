'''
Implementazione degli algoritmi per trovare i ponti e i punti di articolazione in un grafo non orientato.


I bridge è un arco che, se rimosso, aumenta il numero di componenti connesse del grafo. Un punto di articolazione è un nodo che, se rimosso, aumenta il numero di componenti connesse del grafo.


esempio:

1---2---3
    |   |
    5---4

Un punto di articolazione  è un nodo che, se rimosso insieme a tutti i suoi archi, aumenta il numero di componenti connesse del grafo.

Un bridge è un arco che, se rimosso, aumenta il numero di componenti connesse del grafo.


questo grafo ha un ponte tra 1 e 2, e un punto di articolazione in 2, perché se rimuoviamo 2 il grafo si divide in due componenti connesse: {2} e {3,4}.

L'approccio nativo con DFS ha tempo algoritmico per trovare i ponti e i punti di articolazione è O(V(V + E)), dove V è il numero di nodi e E è il numero di archi del grafo.

L'algoritmo di Tarjan utilizza i low-link values per risolvere il problema
in una singola DFS, riducendo la complessità a O(V + E).

'''


class BridgesAdjacencyList:

    #Inizializzazione del costruttore

    def __init__(self,graph : list[list[int]], n : int):

        #Check della dimesione del grafo

        if graph is None or n <= 0 or len(graph) != n:
            raise ValueError("Il grafo non deve essere nullo o vuoto")
        
        self.graph = graph
        self.n = n
        self.solved = False
        #Id incrementale da assegnare a ogni nodo visitato durante la DFS
        self.id = 0


            #Array che risponde alla domanda: "qual è il nodo più 'antico' che posso raggiungere senza usare l'arco con cui sono arrivato qui?"
            #low[v] parte uguale a ids[v], poi si aggiorna durante il backtracking della DFS guardando due cose:

            #Back-edge (v → w) dove w è già visitato → low[v] = min(low[v], ids[w])
            #Figlio c nel DFS tree → low[v] = min(low[v], low[c])



        self.low = [0] * n

        #Serve per memorizzare l'id di ogni nodo, che rappresenta l'ordine in cui è stato visitato durante la DFS

        #esempio: DFS parte da 0:
        #visita 1 → ids[1] = 1
        #visita 2 → ids[2] = 2
        #visita 0 → ids[0] = 0
        #visita 3 → ids[3] = 3
        #backtrack a 1, visita 4 → ids[4] = 4

        self.ids = [0] * n
        self.visited = [False] * n

        #Lista dei risultati dei ponti trovati

        self.bridges = []


    #Funzione per trovare i ponti del grafo

    def findBridges(self) -> list[list[int]]:

        #Se è già stata risolta restituiamo false

        if self.solved:
            return False
        
        #DFS per trovare i ponti, partendo da ogni nodo non visitato
        
        
        for i in range(self.n):
            if not self.visited[i]:
                self.dfs(i, -1)

        #Segna come risolto e restituisce i ponti trovati

        self.solved = True
        return self.bridges

    

    #Creazione del algoritmo dfs
        
    

    def dfs(self, at : int, parent: int) -> None:

        #Impostiamo il nodo attuale come visitato, assegniamo un id incrementale e inizializziamo low e ids per il nodo attuale

        self.visited[at] = True
        self.id += 1
        self.low[at] = self.ids[at] = self.id

        #per ogni nodo adiacente al nodo attuale, se non è il nodo genitore, procediamo con la DFS

        for to in self.graph[at]:
            if to == parent:
                continue

            #   Se il nodo adiacente non è stato visitato, facciamo la DFS su di esso e aggiorniamo low[at] con il minimo tra low[at] e low[to]
            if not self.visited[to]:
                self.dfs(to, at)
                self.low[at] = min(self.low[at], self.low[to])

                #Se nessun vertice raggiungibile da to è un antenato di at, allora at-to è un ponte
                if self.ids[at] < self.low[to]:
                    self.bridges.append([at,to])

            else:
                    
                    #Se il nodo adiacente è già stato visitato, aggiorniamo low[at] con il minimo tra low[at] e ids[to]

                    self.low[at] = min(self.low[at], self.ids[to])



    #Funzione per la craezione del grafo

    def creategraph(self, n : int) -> list[list[int]]:

        graph = [[] for _ in range(n)]

        return graph
    

    #Funzione per aggiungere un arco al grafo

    def addEdge(self, graph : list[list[int]], from_ : int, to : int) -> None:
        graph[from_].append(to)
        graph[to].append(from_)




    #Funzione di main per testare il grafo

    def main(self,string : list[str]) -> None:

        n = 9
        self.graph = self.creategraph(n)

        self.addEdge(self.graph, 0, 1)
        self.addEdge(self.graph, 0, 2)
        self.addEdge(self.graph, 1, 2)
        self.addEdge(self.graph, 2, 3)
        self.addEdge(self.graph, 3, 4)
        self.addEdge(self.graph, 2, 5)
        self.addEdge(self.graph, 5, 6)
        self.addEdge(self.graph, 6, 7)
        self.addEdge(self.graph, 7, 8)
        self.addEdge(self.graph, 8, 5)


        solver = BridgesAdjacencyList(self.graph, n)

        bridges = solver.findBridges()

        for bridge in bridges:
            print(f"Bridge beetween nodes {bridge[0]} and {bridge[1]}")






p = BridgesAdjacencyList([[] for _ in range(9)],9)

p.main([])


    


