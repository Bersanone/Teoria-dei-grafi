#Implementazione del algoritmo di Prim utilizzando un IPQ (indexed priority queue)

#Viene chiamato Eager perchè quando un edge migliore viene trovato , la entry del IPQ viene aggiornata così gli edge non si accumolano mai
#A differenza della variante lazy che le lascia nellla queue


#L'Eager Prims trova l'MST (minimum spanning tree) di un grafo connesso e pesato.
#Perciò trova il percorso di costo minimo che connette tutti i vertici del grafo senza cicli.
# 
#  
# Tempo algoritmico: O(E log V) dove E è il numero di edges e V il numero di vertici
# Spazio algoritmico: O(V+E) 


from dataclasses import dataclass,field
import math

class EagerPrimsAdjancencyList:

    #Usiamo dataclass per definire una struttura dati per rappresentare un edge con i suoi attributi. 
    #L'ordine=True permette di confrontare gli oggetti basandosi sui campi definiti, utile per le operazioni di priorità.

    @dataclass(order=True)

    class Edge:

        weight : int
        from_ : int = field(compare=False)
        to : int = field(compare=False)

    #Inizzializzazione di una IPQ minimale per Eager



    class MinIndexedDHeap:

        def __init__(self, degree : int, maxSize : int):
            #Numero corrente di elementi nella heap
            self.sz = 0
            #Degree di ogni nodo nel heap
            self.D = max(2, degree)
            #Numero massimo di elementi nella heap
            self.N = max(self.D + 1, maxSize)
            #Array di lookup per tracciare gli indici child/parent di ogni nodo
            self.child = [0] * self.N
            self.parent = [0] * self.N
            #La position map (pm) tiene mappa gli indici chiavi (ki) dove la posizione di quelle chiavi è rappresentata nella priprity queue nel dominio (0,sz)
            self.pm = [0] * self.N
            #La inverse map (im) tiene mappa gli indici delle chiavi nel range (0,sz) il quale crea la priority queue.
            #Nota che 'im' e 'pm' sono gli inversi l'uno dell'altro, quindi pm[im[i]] = im[pm[i]] = i
            self.im = [0] * self.N
            #I valori associati con le chiavi, nota che questo array è indicizzato dalle key indexes (dette anche ki)
            self.values = [None] * self.N

            for i in range(self.N):
                self.parent[i] = (i-1) // self.D
                self.child[i] = i * self.D + 1
                self.pm[i] = self.im[i] = -1


        def isEmpty(self) -> bool:
            return self.sz == 0

        def contains(self, ki : int) -> bool:
            return self.pm[ki] != -1


        def peekMinKeyIndex(self) -> int:
            return self.im[0]

        def poolMinValue(self) -> int:

            minValue = self.values[self.im[0]]
            self.delete(self.im[0])
            return minValue



        def insert(self, ki : int, value : list[int]) -> None:
            self.pm[ki] = self.sz
            self.im[self.sz] = ki
            self.values[ki] = value
            self.sz += 1
            self.swim(self.sz)

        def decrease(self, ki : int, value : list[int]) -> None:
            if value < self.values[ki]:
                self.values[ki] = value
                self.swim(self.pm[ki])


        def delete(self,ki : int) -> int:
            i = self.pm[ki]
            self.swap(i, self.sz-1)
            self.sink(i)
            self.swim(i)
            value = self.values[ki]
            self.values[ki] = None
            self.pm[ki] = -1
            self.im[self.sz] = -1
            self.sz = -1
            return value



        def swap(self, i : int, j : int) -> None:
            self.pm[self.im[j]] = i
            self.pm[self.im[i]] = j
            tmp = self.im[i]
            self.im[i] = self.im[j]
            self.im[j] = tmp


        def sink(self, i : int) -> None:
            for j in range(self.minChild(i),-1,-1):
                self.swap(i,j)
                i = j
                j = self.minChild(i)




        def swim(self, i : int) -> None:
            while self.less(i, self.parent[i]):
                self.swap(i, self.parent[i])
                i = self.parent[i]



        def minChild(self, i : int) -> int:
            index = -1
            from_ = self.child[i]
            to = min(self.sz, from_ + self.D)
            for j in range(from_,to):
                if self.less(j,i):
                    index = j
                    i = j

            return index


        def less(self, i : int, j : int) -> bool:
            return self.values[self.im[i]] < self.values[self.im[j]]


 


    def __init__(self, graph : list[list[Edge]]):

        if not graph:
            raise ValueError("Graph cannot be null")

        self.n = len(graph)
        self.graph = graph
        self.solved = False
        self.mstExsists = False
        self.visited = [False] * self.n


    def getMST(self) -> list[Edge]:
        self.solve()
        return self.mstExsists if self.mstEdges else None


    def getMstCost(self) -> int:
        self.solve()
        return self.mstExsists if self.minCostSum else None


    def solve(self) -> None:
        if self.solved == True:
            return
        self.solved = True
        m : int = self.n - 1
        edgeCount = 0
        visited = [False] * self.n
        mstEdges = [self.Edge(0,0,0)] * m

        #Il grado del d-ary heap può impatatre le performance specialmente su grafi densi
        #la base-2 logaritmica di N è una buona euristica


        #Utilizziamo il grado massimo tra 2 e il logaritmo in base 2 del numero di nodi per bilanciare la profondità dell'albero e il numero di figli per nodo.
        #In questo modo N cresce gradualmente con l'aumento dei nodi, tenendo le operazioni di inserimento e rimozione efficienti.

        degree = max(2, math.floor(math.log2(self.n)))

        ipq = self.MinIndexedDHeap(degree, self.n)

        self.relaxEdgesAtNode(0)

        while not ipq.isEmpty() and edgeCount != m:
            destNode = ipq.peekMinKeyIndex()
            edge = ipq.poolMinValue()

            mstEdges[edgeCount+1] = self.Edge(0,0,0)
            minCostSum += edge.cost
            self.relaxEdgesAtNode(destNode)

        self.mstExsists = edgeCount == m

    def relaxEdgesAtNode(self, node : int) -> None:
        self.visited[node] = True
        for edge in self.graph[node]:
            if self.visited[edge.to]:
                continue
            if self.MinIndexedDHeap.contains(edge.to):
                self.MinIndexedDHeap.decrease(edge.to,edge)
            else:
                self.MinIndexedDHeap.insert(edge.to,edge)

    def createEmptyGraph(self) -> list[list[Edge]]:
        return [[] for _ in range(self.n)]

    def addDirectedEdge(self, graph : list[list[Edge]], from_ : int, to : int, cost : int) -> None:
        graph[from_].append(self.Edge(cost,from_,to))


    def addUndirectedEdge(self, graph : list[list[Edge]], from_ : int, to : int, cost : int) -> None:
        self.addDirectedEdge(graph,from_,to,cost)
        self.addDirectedEdge(graph,to,from_,cost)