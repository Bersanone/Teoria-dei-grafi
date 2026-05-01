'''
Implementazione di un algoritmo di Dijkstra utilizzando un D-Heap come struttura dati per la coda di priorità.

L'algoritmo di Dijkstra è un algoritmo di ricerca del percorso più breve in un grafo con pesi non negativi.

Possiamo trovare la strada migliore da un nodo di partenza ad uno di arrivo, solo quando esploriamo tutti i nodi vicini al nodo di arrivo



COMMENTARE IL CODICE PER SPIEGARE IL FUNZIONAMENTO DELL'ALGORITMO E DELLA STRUTTURA DATI UTILIZZATA
'''

from collections import deque



class dijkstraAlgorithmWithDHeap:

    def __init__(self):
        self.n = 0
        self.edgeCount = 0
        self.dist =  []
        self.prev = []
        self.graph = []

    class Edge:

        def __init__(self, fromNode : int, to : int, cost : float):
            self.fromNode = fromNode
            self.to = to
            self.cost = cost

    class Node:

        def __init__(self, id : int, value : float):
            self.id = id
            self.value = value


        def __lt__(self, other):
            return self.value < other.value


    
    def DijkstrasShortestPathAdjacencyList(self,n : int) -> None:

        self.n = n
        self.graph = [[] for _ in range(n)]
        self.edgeCount = 0

    

    def addEdge(self, fromNode : int, to : int, cost : float) -> None:
        self.graph[fromNode].append(self.Edge(fromNode, to, cost))
        self.edgeCount += 1

    
    def getGraph(self) -> list[list[Edge]]:
        return self.graph
    

    def Dijkstra(self, start : int, end : int) -> float:


        degree = self.edgeCount // self.n
        ipq = self.DHeap()
        ipq.MinIndex(degree, self.n)
        ipq.insert(start, 0.0)


        self.dist = [float('inf')] * self.n
        self.dist[start] = 0



        visited = [False] * self.n
        self.prev = [None] * self.n


        while ipq:
            nodeid = ipq.peekMinKeyIndex()

            minValue = ipq.poolMinValue()

            if minValue < self.dist[nodeid]:
                continue

            for edge in self.graph[nodeid]:
                if visited[edge.to]:
                    continue

                new_dist = self.dist[nodeid] + edge.cost


                if new_dist < self.dist[edge.to]:
                    self.prev[edge.to] = nodeid
                    self.dist[edge.to] = new_dist
                    if ipq.contains(edge.to):
                        ipq.decrease(edge.to, new_dist)
                    else:
                        ipq.insert(edge.to, new_dist)


            if nodeid == end:
                return self.dist[end]
            
        return float('inf')
    


    def reconstructPath(self, start : int, end : int) -> list[int]:
        self.Dijkstra(start,end)
        path = deque()

        if self.dist[end] == float('inf'):
            return path
        
        at = end

        while at != start:
            path.appendleft(at)
            at = self.prev[at]
            
        path.appendleft(start)

        return list(path)
    
    class DHeap:

        def __init__(self):
            self.sz = 0
            self.N = 0
            self.D = 0
            self.child = []
            self.parent = []
            self.pm = []
            self.im = []
            self.values = []


        def __bool__(self):
            return self.sz > 0
    


        def MinIndex(self, degree: int, maxSize : int) -> None:
            if maxSize <= 0:
                raise ValueError("maxSize must be greater than 0")
            
            self.D = max(2, degree)
            self.N = max(self.D + 1, maxSize)

            self.im = [0] * self.N
            self.pm = [0] * self.N

            self.child = [0] * self.N
            self.parent = [0] * self.N

            self.values = [0] * self.N

            for i in range(self.N):
                self.parent[i] = (i-1) // self.D
                self.child[i] = i * self.D + 1
                self.pm[i] = self.im[i] = -1


        def size(self) -> int:
            return self.sz
        

        def isEmpty(self) -> bool:
            return self.sz == 0
        

        def decrease(self, k1 : int, value : object) -> None:
            if not self.contains(k1):
                raise ValueError("index does not exist in the heap")
            self.valueNotNull(value)
            if value < self.values[k1]:
                self.values[k1] = value
                self.swim(self.pm[k1])
        

        def insert(self, ki : int, value : object ) -> None:
            if self.contains(ki):
                raise ValueError("index already exists in the heap")
            self.valueNotNull(value)
            self.pm[ki] = self.sz
            self.im[self.sz] = ki
            self.values[ki] = value
            self.sz += 1
            self.swim(self.sz - 1)


        def peekMinKeyIndex(self) -> int:
            if self.isEmpty():
                raise ValueError("Priority queue underflow")
            return self.im[0]
        

        def peekMinValue(self) -> object:
            if self.isEmpty():
                raise ValueError("Priority queue underflow")
            return self.values[self.im[0]]
        

        def poolMinValue(self) -> object:
            if self.isEmpty():
                raise ValueError("Priority queue underflow")
            minValue = self.peekMinValue()
            self.delete(self.peekMinKeyIndex())
            return minValue
        
        def poolMInKeyIndex(self) -> int:
            if self.isEmpty():
                raise ValueError("Priority queue underflow")
            minkeyIndex = self(self.peekMinKeyIndex)
            self.delete(minkeyIndex)
            return minkeyIndex




        #Helpers


        def delete(self, k1 : int) -> None:
            if not self.contains(k1):
                raise ValueError("index does not exist in the heap")
            i = self.pm[k1]
            value = self.values[k1]

            self.sz -= 1

            self.swap(i, self.sz)

            self.sink(i)
            self.swim(i)


            
            self.pm[k1] = -1
            self.im[self.sz] = -1
            self.values[k1] = None
            
            
            return value








        def contains(self, ki : int) -> bool:
            self.valueNotNull(ki)
            return self.pm[ki] != -1


        def sink(self, i : int) -> None:
            j = self.minChild(i)
            while j != -1:
                if self.less(i,j):
                    break
                self.swap(i, j)
                i = j
                j = self.minChild(i)


        def swim(self, i : int) -> None:
            while i>0 and self.less(i, self.parent[i]):
                self.swap(i, self.parent[i])
                i = self.parent[i]

        def swap(self, i : int, j : int) -> None:
            self.pm[self.im[j]] = i
            self.pm[self.im[i]] = j
            tmp = self.im[i]
            self.im[i] = self.im[j]
            self.im[j] = tmp 


        def minChild(self, i : int) -> int:
            index = -1
            from_ = self.child[i]
            to = min(self.sz, from_ + self.D)

            j = from_

            while j < to:
                if index == -1 or self.less(j, index):
                    index = j
                j += 1
            return index



        def less(self, i : int, j : int) -> bool:
            return self.values[self.im[i]] < self.values[self.im[j]]
        

        def valueNotNull(self, value : object) -> None:
            if value is None:
                raise ValueError("value cannot be null")
        

                


p = dijkstraAlgorithmWithDHeap()
p.DijkstrasShortestPathAdjacencyList(5)
p.addEdge(0, 1, 10)
p.addEdge(0, 2, 5)
p.addEdge(1, 2, 2)
p.addEdge(1, 3, 1)
p.addEdge(2, 1, 3)
p.addEdge(2, 3, 9)
p.addEdge(2, 4, 2)
p.addEdge(3, 4, 4)
p.addEdge(4, 3, 6)
print(p.Dijkstra(0, 4))
print(p.reconstructPath(0, 4))


        