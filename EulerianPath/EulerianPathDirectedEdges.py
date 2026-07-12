'''
Implemenmtazione dell'algoritmo di ricerca per un Eulerian path in un grafo diretto.
Questa implementazione verifica che il grafo di input sia densamente connesso (tutti gli edges sono raggiungibili) e supporti self loops e repeated edges tra nodi.


Un Eulerian Path è un path in un grafo che visita ogni edge esattamente una volta.
Un Eulerian circuits è un Eulerian path che inizia e finisce nello stesso nodo.

Time complexity: O(V+E)
'''
import collections

class EulerianPathDIrectedEdges:

    def __init__(self, graph : list[list[int]]):
        
        if graph is None:
            raise ValueError("Graph cannot be None")
        

        self.edgeCount = 0
        self.inDeg = list[int]
        self.outDeg = list[int]
        self.path = collections.deque()
        self.graph = list[list[int]]




        self.n = len(graph)
        self.graph = graph

        #Istanzioamento di una deque
        self.path = collections.deque()


    '''
    Trova un Eulerian path nel grafo se esiste

    L'algoritmo prima verifica le condizioni necessarie per un eulerian path basato sui gradi(quanti edge entrano, e quanti escono) dei vertici per poi utilizzare l'algoritmo di Hierholzer per costruire il path via DFS.


    Restituisece un array di ID dei nodi rapressentando l'eulerian path oppure None se non esiste nessun path oppure il grafo è disconnesso

    Tempo: O(V+E)
    Space: O(V+E)
    
    
    '''




    def getEulerianPath(self) -> None:

        self.setup()

        if not self.graphHasEulerianPath():
            return None
        
        #Eseguiamo la dfs da unp starting node valido
        
        self.__dfs(self.findStartNode())

        #Controlliamo se tutti i nodi sono stati traversati. se il grafo è disconnesso (Esclusi i nodi isolati senza edge), la path.size() sarà minore di edgecount + 1


        self.edgeCount = self.edgeCount + 1

        if len(self.path) != self.edgeCount:
            return None
        
        #Convertiamo il path da una linkedList ad un array primitivo per convenzienza del caller

        soln : list[int] =  [self.edgeCount + 1]

        for i in self.path:
            soln[i] = self.path.popleft()











    #Pre computa gli in degrees,out-degrees e il count totale degli Edge

    def setup(self) -> None:

        self.inDeg = [[] for _ in range(self.n)]
        self.outDeg = [[] for _ in range(self.n)]
        self.edgeCount = 0

        for fromN in self.n:
            for to in self.graph[fromN]:
                self.inDeg[to] += 1
                self.outDeg[fromN]+=1
                self.edgeCount += 1
 












    #Un grafo diretto ha un Eulerian path solo se:
    #1. Almeno un vertice ha outDegree - inDegree = 1 (start node)
    #2. Almeno un vertice ha inDegree - outDegree = 1 (end node)
    #3. Tutti i vertici hanno inDegree == outDegree


    def graphHasEulerianPath(self) -> bool:
        if self.edgeCount == 0:
            return False
        

        startNodes : int = 0
        endNodes : int = 0

        for i in self.n:
            diff : int = self.outDeg[i] - self.inDeg[i]

            if abs(diff) > 1:
                return False
            elif diff == 1:
                startNodes+=1
            elif diff == -1:
                endNodes += 1

        return endNodes == 0 & startNodes == 0 or endNodes == 1 & startNodes == 1
    



    #Identifichiamo un nodo per iniziare l'eurelian path traversal

    def findStartNode(self) -> int:

        start : int = 0
        for i in range(self.n):
            #Se un nodo ha uno o più outgoing edges rispetto a quelli incoming, DEVE ESSERE LO START
            if self.outDeg[i] - self.inDeg[i] == 1:
                return i
            
            #Altrimenti iniziamo al primo nodo incontarto con almeno un outgoing edge
            
            if self.outDeg[i] > 0:
                start = i


            return start







    #Implementrazione ricursiva dell'algoritmo di Hierholzer

    #Traversiamo gli edge fino a che raggiungiamo un nodo senza edge outgoing rimasti, a quel punto eseguiamo il backtracking

    #Durante il backtracking aggiungiamo il nodo corrente di fronte al path.

    #Questo merge naturalmente tutti i sub-cicli all'interno del path principale


    def __dfs(self, at : int) -> None:
        while self.outDeg(at) != 0:
            #Prendiamo il prossimo nodo disponibile e decrementiamo out[at] per rimuovere gli edge 
            #Lo utilizziamo come index per selezionare il prossimo vicino, questo è O(1) per edge

            self.outDeg[at] = self.outDeg[at] - 1

            next : int = self.graph[at][self.outDeg[at]]

            self.__dfs(next)
        #Quando backtrackiamo dalla recursione, aggiungiamo i nodi all'inizio del path

        self.path.appendleft(at)













    #Helpers


    #Aggiunge un directed edge da un nodo ad un altro

    #Parametro g: Adjency list per aggiungere l'edge to
    #Parametro ffromN: L'indice del nodo sorgente
    #Parametro toN: L'indice del nodo di destinazione dell'edge

    def addDirectedEdge(self, g : list[list[int]], fromN : int, toN : int) -> None:
        g[fromN].append(toN)


    #Inizializza una adjency list vuota con n nodi

    #Parametro n: Il numero di nodi nel grafo
    #Return: Un adjency list vuota


    def initializeEmptyGraph(self, n : int) -> list[list[int]]:
        graph : list[list[int]] = [[] for _ in range(n)]
        return graph





