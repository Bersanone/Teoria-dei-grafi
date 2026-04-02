'''
Implementazione del BreadthFirstSearch con liste adiacenti.
Esplora un grafo partendo da un nodo da cui punta ai nodi vicini fino ad esplorarli tutti, utilizzando una coda FIFO per l'ordine.
Serve per trovare la strada più breve in un unweighted graph

Time: O(V+E)
Space: O(V)
'''


#Importiamo la Doubly Linked List
from collections import deque


class BreadthFirstSearchAdjacencyList:

    #Creiamo una classe che rappresenta gli edge(i collegamenti tra nodi)

    class Edge:
        #inizializziamo il from e il to
        from_node = 0
        to = 0

        #Inizializziamo il costruttore della classe Edge

        def __init__(self,from_node : int, to : int):
            self.from_node = from_node
            self.to = to


    #Inizializziamo il costruttore della classe BreadthFirstSearchAdjacencyList
    #Passiamo un solo parametro ovvero il grafo che deve essere una lista adiacente oppure None di default


    def __init__(self,graph : list[list[Edge]] | None = None):
        #Se il grafo non è presente ne creiamo uno nuovo
        if graph is None:
            graph = self.createEmptyGraph(8)

        #Impostiamo i nodi al numero di elementi presenti nel grafo

        self.n = len(graph)

        #Impostiamo il graph con self


        self.graph = graph

        #Creiamo una lista per rappresentare i precedenti
        self.prev = []

    
    def main(self) -> None:

        #Impostiamo il numero di nodi ad 8
        n : int = 8

        #Creiamo un nuovo grafo per il numero di nodi impostato all'inizio

        graph : list[list[self.Edge]] = self.createEmptyGraph(n)

        #Creiamo dei collegamenti Undirected

        self.addUndirectedEdge(graph,0,1)
        self.addUndirectedEdge(graph,1,2)
        self.addUndirectedEdge(graph,0,3)
        self.addUndirectedEdge(graph,1,4)
        self.addUndirectedEdge(graph,2,5)
        self.addUndirectedEdge(graph,3,6)
        self.addUndirectedEdge(graph,4,6)
        self.addUndirectedEdge(graph,4,7)
        self.addUndirectedEdge(graph,5,7)
        self.addUndirectedEdge(graph,6,7)

        #Istanziamo la classe BreadthFirstSearchAdjacencyList e passiamo il grafo creato in precedenza


        solver : BreadthFirstSearchAdjacencyList = BreadthFirstSearchAdjacencyList(graph=graph)

        #Stampiamo i path

        print(f"{solver.reconstructPath(0,7)}")
        print(f"{solver.reconstructPath(3,5)}")
    
    #Funzione per ricostruire il path da uno start ad uno end

    def reconstructPath(self,start : int,end : int) -> list[int]:
        #Istanziamo la __bfs con il parametro di start
        self.__bfs(start)
        #Istanziamo la linked list
        path : deque[int] = deque()
        #Creiamo la variabile at = end 
        at = end

        while at is not None:

            #aggiungiamo il nodo inizale nella linked list

            path.appendleft(at)

            at = self.prev[at]

        #Se il path è null o l'inzio è diverso da start restituiamo una lista vuota

        if not path or path[0] != start:
            return []
        
        return path






    #Metodi privati



    def __bfs(self,start : int) -> None:
        #Creiamo un array per tracciare i parent node 
        self.prev = [None] * self.n
        #Settiamo False per tutti i nodi
        visited : list[bool] = [False] * self.n
        #Inizializzazione della linked list
        queue = deque()



        #Aggiungiamo il primo nodo all'inzio della lista
        queue.append(start)
        #Settiamo il nodo come visited
        visited[start] = True

        #Finchè la queue cointiene elementi

        while queue:

            #Eliminiamo il nodo scelto dalla queue

            node : int = queue.popleft()
            #Per ogni edge preseete nel nodo
            for edge in self.graph[node]:
                #Verifichiamo che non sia gia stato visitato
                if not visited[edge.to]:
                    #Impostiamo visited a True
                    visited[edge.to] = True
                    #Impostiamo come parenti il nodo corrente
                    self.prev[edge.to] = node
                    #AGgiungiamo il nodo collegato alla lista
                    queue.append(edge.to)







    #Graph utils



    #Funzione per creare un nuovo grafo, passiamo come parametro il numero di nodi da passare

    def createEmptyGraph(self,n:int) -> list[list[Edge]]:

        #Creiamo le liste adiacenti vuote per tutti i nodi

        graph : list[list[self.Edge]] = [[] for _ in range(n)]

        #Restituiamo il grafo

        return graph
    

    #Creiamo un collegamento directed

    #Accetta 3 parametri, un grafo, il nodo di inziio e quello di fine


    def addDirectedEdge(self, graph : list[list[Edge]], u : int, v : int) -> None:
        #Prendiamo il nodo di partenza dal grafo e facciamo un append del collegamento diretto
        graph[u].append(self.Edge(u,v))



    def addUndirectedEdge(self,graph : list[list[Edge]], u : int, v : int) -> None:
        #Creiamo un collegamento doppio utilizzando la funzione di prima
        self.addDirectedEdge(graph, u, v)
        self.addDirectedEdge(graph, v, u)



p = BreadthFirstSearchAdjacencyList()

p.main()




