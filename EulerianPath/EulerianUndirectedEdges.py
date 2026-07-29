#Implementazione per trovare un eulerian path su n undirected graph

import collections

class EulerianPathUndirectedEdge:


    class EulerianUndirectedEdge:

        def __init__(self, u:int , v:int, cost:float):
            self.u = u
            self.v = v
            self.cost = cost
            self.used = False

        #__repr__ definisce la rappresentazione "ufficiale" di un oggetto, pensata per essere non ambigua e, idealmente, utile per debugging o per ricostruire l'oggetto stesso. Viene chiamato da repr(obj), dalla console interattiva, e come fallback da print()/str() se __str__ non è definito.

        def __repr__(self):
            return f"({self.u}-{self.v} ,cost = {self.cost}, used = {self.used})"



    def __init__(self, graph : list[list[EulerianUndirectedEdge]]):

        if graph is None:
            raise ValueError("Graph cannot be null")

        self.n = len(graph)
        self.graph = graph
        self.path = collections.deque()
        self.edgeCount = 0
        self.degree = [0] * self.n
        self.edgeIndex = [0] * self.n

    #@staticmethod marca un metodo che non riceve né self (istanza) né cls (classe) come primo parametro implicito


    @staticmethod
    def createEmptyGraph(n : int) -> list[list[EulerianUndirectedEdge]]:

            return [[] for _ in range(n)]

    @staticmethod
    def addEulerianUndirectedEdge(g : list[list[list]], u : int, v : int, cost : float) -> None:

            edge = EulerianPathUndirectedEdge.EulerianUndirectedEdge(u,v,cost)

            g[u].append(edge)
            g[v].append(edge)


    def getEulerianPath(self) -> list[EulerianUndirectedEdge]:


        self.setup()

        if not self.graphHasEulerianPath():
            print("graph has no Eulerian Path")
            return None
        self.dfs(self.findStartNode())

        if len(self.path) != self.edgeCount:
            return None

        return list(self.path)
    

    def resetUsed(self, g:list[list[EulerianUndirectedEdge]]) -> None:
        for from_ in range(self.n):
            for e in self.graph[from_]:
                e.used = False

    #Funzione di setup per ciclare sui nodi e mappa degree ed edge count, chiamiamo resetUsed perchè sennò la dfs salterebbe tutti i nodi


    def setup(self) -> None:

        self.degree = [0] * self.n
        self.edgeCount = 0
        self.path = collections.deque()
        self.edgeIndex = [0] * self.n


        for from_ in range(self.n):

            for e in self.graph[from_]:
                if e.used:
                    continue
                self.degree[e.u] += 1
                self.degree[e.v] += 1
                e.used = True
                self.edgeCount+=1

        self.resetUsed(self.graph)


    def graphHasEulerianPath(self) -> bool:

        if self.edgeCount == 0:
            return False
        
        oddNodes = 0
        for i in range(self.n):
            if self.degree[i] % 2 != 0:

                oddNodes += 1

        return oddNodes == 0 or oddNodes == 2


    def findStartNode(self) -> int:
        start = 0

        for i in range(self.n):
            if self.degree[i] % 2 != 0:
                return i

            if self.degree[i] > 0:
                start = i
        

        return start

    #Creiamo una dfs che itera e conteggia gli edge sui nodi False



    def dfs(self, at:int) -> None:

        while self.edgeIndex[at] < len(self.graph[at]):
            e = self.graph[at][self.edgeIndex[at]]
            self.edgeIndex[at] += 1

            if e.used:
                continue
            e.used = True
            #Il prossimo nodo è la destinazione se il nodo sorgente è a at altrimenti sarà il nodo sorgente
            nextNode = e.v if e.u == at else e.u

            self.dfs(nextNode)

            self.path.appendleft(e)













n = 7
g = EulerianPathUndirectedEdge.createEmptyGraph(n)

EulerianPathUndirectedEdge.addEulerianUndirectedEdge(g, 1, 2, 1.0)
EulerianPathUndirectedEdge.addEulerianUndirectedEdge(g, 2, 2, 1.0)   
EulerianPathUndirectedEdge.addEulerianUndirectedEdge(g, 2, 4, 1.0)
EulerianPathUndirectedEdge.addEulerianUndirectedEdge(g, 2, 4, 1.0)


solver = EulerianPathUndirectedEdge(g)

path = solver.getEulerianPath()

print(path)
    

        
