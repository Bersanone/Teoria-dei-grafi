from collections import deque, defaultdict

class TarjanSolverScc:
    def __init__(self, graph : list[list[int]]):
        if graph is None:
            raise ValueError("Graph cannot be None")
        
        self.n = len(graph)
        self.graph = graph
        self.solved = False
        self.id = 0
        self.sccount = 0
        self.onStack = [False] * self.n
        self.ids = [-1] * self.n
        self.low = [0] * self.n
        self.sccs = [0] * self.n
        self.stack = deque()
        self.unvisited = -1


   #Funzioni main

    def getSccs(self) -> list[int]:
        if not self.solved:
            self.solve()
        
        return self.sccs
    


    def sccCount(self) -> int:
        if not self.solved:
            self.solve()

        return self.sccount
    

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

        if self.solved:
            return 
        
        for i in range(self.n):
            if self.ids[i] == self.unvisited:
                self.dfs(i)
        
        self.solved = True






    #Definizione della DFS per Tarjan

    def dfs(self, at : int) -> None:

        self.id += 1

        self.ids[at] = self.low[at] = self.id

        self.stack.append(at)

        self.onStack[at] = True


        for to in self.graph[at]:

            if self.ids[to] == self.unvisited:
                self.dfs(to)
            if self.onStack[to]:
                self.low[at] = min(self.low[at], self.low[to])

        if self.ids[at] == self.low[at]:

             while True:
                    node = self.stack.pop()
                    self.onStack[node] = False
                    self.sccs[node] = self.sccount

                    if node == at:
                        break
                    

             self.sccount +=1



    def createGraph(self, n : int) -> list[list[int]]:

        graph = [[] for _ in range(n)]

        return graph
    

    def addEdge(self,graph : list[list[int]], from_node : int, to_node : int) -> None:
        graph[from_node].append(to_node)




p = TarjanSolverScc([[] for _ in range(8)])

p.main([])
