'''
Implementazione di un algoritmo di Dijkstra utilizzando un D-Heap come struttura dati per la coda di priorità.

L'algoritmo di Dijkstra è un algoritmo di ricerca del percorso più breve in un grafo con pesi non negativi.

Possiamo trovare la strada migliore da un nodo di partenza ad uno di arrivo, solo quando esploriamo tutti i nodi vicini al nodo di arrivo




Da finire di implementare ipq con D-Heap custom e commentare il codice






'''

import heapq
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

    

    def addEdge(self, fromNode : int, to : int, cost : float) -> None:
        self.graph[fromNode].append(self.Edge(fromNode, to, cost))

    
    def getGraph(self) -> list[list[Edge]]:
        return self.graph
    

    def Dijkstra(self, start : int, end : int) -> float:


        degree = self.edgeCount // self.n
        ipq = self.DHeap()
        ipq.MinIndex(degree, self.n)
        ipq.

        self.dist = [float('inf')] * self.n
        self.dist[start] = 0

        pq = []

        heapq.heappush(pq, self.Node(start, 0))

        visited = [False] * self.n
        self.prev = [None] * self.n


        while pq:
            node = heapq.heappop(pq)

            visited[node.id] = True

            if self.dist[node.id] < node.value:
                continue


            for edge in self.graph[node.id]:
                if visited[edge.to]:
                    continue

                new_dist = self.dist[node.id] + edge.cost

                if new_dist < self.dist[edge.to]:
                    self.prev[edge.to] = edge.fromNode
                    self.dist[edge.to] = new_dist
                    heapq.heappush(pq, self.Node(edge.to, self.dist[edge.to]))


            if node.id == end:
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

            for i in range(self.n):
                self.parent[i] = (i-1) // self.D
                self.child[i] = i * self.D + 1
                self.pm[i] = self.im[i] = -1


        def size(self) -> int:
            return self.sz
        

        def isEmpty(self) -> bool:
            return self.sz == 0
        

        def insert(self, )
        



        #Helpers


        def sink(self, i : int) -> None:
            j = self.minChild(i)
            while j != -1:
                self.swap(i, j)
                i = j
                j = self.minChild(i)


        def swim(self, i : int) -> None:
            while self.less(i, self.parent[i]):
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
            to = min(self.sz, self.from_ + self.D)

            j = from_

            while j < to:
                if self.less(j, index):
                    index = i = j
                    j += 1
                return index



        def less(self, i : int, j : int) -> bool:
            return self.values[self.im[i]] < self.values[self.im[j]]
        

        def valueNotNull(self, value : object) -> None:
            if value is None:
                raise ValueError("value cannot be null")
        

                




        