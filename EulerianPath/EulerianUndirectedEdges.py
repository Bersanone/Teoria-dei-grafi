#Implementazione per trovare un eulerian path su n undirected graph

import collections

class EulerianPathUndirectedEdge:

    class Edge:

        def __init__(self, from_node : int, to : int, weight : int):

            self.from_node = from_node
            self.to = to
            self.weight = weight

    class EulerianUndirectedEdge:

        def __init__(self, u:int , v:int, cost:float):
            self.u = u
            self.v = v
            self.cost = cost
            self.used = False


        def __str__(self):
            return f"{self.u} , {self.v} , {self.used}, {self.cost}"


        def createEmptyGraph(self, n : int) -> list[list[Edge]]:

            g = []

            for i in n:
                g.add[[]]

            return g


        def addEulerianUndirectedEdge(self, g : list[list[list]], u : int, v : int, cost : None) -> None:

            edge = Edge(u,v,cost)

            g[u].add(edge)
            g[v].add(edge)


    def __init__(self, graph : list[list[EulerianUndirectedEdge]]):

        if graph == None:
            raise ValueError("Graph cannot be null")

        self.n = graph.size()
        self.graph = graph
        self.path = collections.deque
        self.edgeCount = 0
        self.degree =list[int]


    def getEulerianPath(self) -> list[EulerianUndirectedEdge]:

        self.setup()

        if not self.graphHasEulerianPath:
            print("graph has no Eulerian Path")
            return None
        self.dfs(self.findStartNode())

        soln = []

        for i in self.path:
            soln.append(self.path.pop)

        return soln

    def resetUsed(self, g:list[list[EulerianUndirectedEdge]]) -> None:
        from_ = 0
        for i in self.n:
            from_ += 1 
            for e in self.graph[from_]:
                e.used = False


    def setup(self) -> None:

        self.degree = [[] for _ in self.n]
        self.edgeCount = 0
        from_ = 0

        for i in self.n:
            from_ += 1

            for e in self.graph[from_]:
                if e.used:
                    continue
                self.degree[e.u] += 1
                e.used = True
                self.edgeCount+=1

        self.resetUsed(self.graph)


    def graphHasEulerianPath(self) -> bool:
        oddNodes = 0
        for i in self.n:
            if self.degree[i] % 2 != 0:

                oddNodes += 1

        return oddNodes == 0 or oddNodes == 2


    def findStartNode(self) -> None:
        start = 0

        for i in self.n:
            if self.degree[i] % 2 != 0:
                return i

        return start


    def dfs(self, at:int) -> None:

        while self.out[at] != 0:
            outDect = self.out[at]
            outDect -= 1
            nextEdge = self.graph[at][outDect]

            self.dfs(nextEdge.to)

            self.path.appendleft(nextEdge)




    

        
