'''
Implementazione del BreadthFirstSearch con liste adiacenti.
Esplora un grafo partendo da un nodo da cui punta ai nodi vicini fino ad esplorarli tutti, utilizzando una coda FIFO per l'ordine.
Serve per trovare la strada più breve in un unweighted graph

Time: O(V+E)
Space: O(V)
'''

from collections import deque


class BreadthFirstSearchAdjacencyList:

    class Edge:
        from_node = 0
        to = 0

        def __init__(self,from_node : int, to : int):
            self.from_node = from_node
            self.to = to


    def __init__(self,graph : list[list[Edge]] | None = None):
        if graph is None:
            graph = self.createEmptyGraph(8)

        self.n = len(graph)
        self.graph = graph


    prev = []

    
    def main(self) -> None:
        n : int = 8

        graph : list[list[self.Edge]] = self.createEmptyGraph(n)

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


        solver : BreadthFirstSearchAdjacencyList = BreadthFirstSearchAdjacencyList(graph=graph)

        print(f"{solver.reconstructPath(0,7)}")
        print(f"{solver.reconstructPath(3,5)}")
    

    def reconstructPath(self,start : int,end : int) -> list[int]:
        self.__bfs(start)
        path : deque[int] = deque()
        at = end
        while at is not None:
            path.appendleft(at)
            at = self.prev[at]

        if not path or path[0] != start:
            return []
        
        return path






    #Metodi privati



    def __bfs(self,start : int) -> None:
        self.prev = [None] * self.n
        visited : list[bool] = [False] * self.n
        queue = deque()


        queue.append(start)
        visited[start] = True

        while queue:
            node : int = queue.popleft()
            for edge in self.graph[node]:
                if not visited[edge.to]:
                    visited[edge.to] = True
                    self.prev[edge.to] = node
                    queue.append(edge.to)







    #Graph utils
    def createEmptyGraph(self,n:int) -> list[list[Edge]]:

        graph : list[list[self.Edge]] = [[] for _ in range(n)]

        return graph
    


    def addDirectedEdge(self, graph : list[list[Edge]], u : int, v : int) -> None:
        graph[u].append(self.Edge(u,v))



    def addUndirectedEdge(self,graph : list[list[Edge]], u : int, v : int) -> None:
        self.addDirectedEdge(graph, u, v)
        self.addDirectedEdge(graph, v, u)



p = BreadthFirstSearchAdjacencyList()

p.main()




