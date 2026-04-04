#Implementazione di un algoritmo di topological sort utilizzando DFS su liste adiacenti di un grafico diretto aciclico.

#Possiamo utilizzare questo algoritmo per definire gerarchie o dipendenze

#Restituiamo un array con gli indici dei nodi in un ordine topologico, per ogni direcetd edge u -> v, u viene prima di v nell'ordine

#Includiamo anche un metodo per trovare il shortest path nel DAG utilizzando l'ordinamento topologico



class topologicalSortAdjacencyList:

    class Edge:

        from_node = 0
        to = 0
        weight = 0


        def __init__(self, from_node : int,to : int,weight : int):

            self.from_node = from_node
            self.to = to
            self.weight = weight


    def main(self):

        n : int = 7

        graph : dict[int, list[Edge]] = {}

        for i in n:
            graph[i] = []


        graph[0].append(self.Edge(0,1,3))
        graph[0].append(self.Edge(0,2,2))
        graph[0].append(self.Edge(0,5,3))
        graph[1].append(self.Edge(1,3,1))
        graph[1].append(self.Edge(1,2,6))
        graph[2].append(self.Edge(2,3,1))
        graph[2].append(self.Edge(2,4,10))
        graph[3].append(self.Edge(3,4,5))
        graph[5].append(self.Edge(5,4,7))


        ordering : list[int] = self.topologicalsort(graph, n)
        print(str(ordering))


        dists : list[int] = self.dagShortestPath(graph,0,n)

        print(dists[4])
        print(dists[6])























    #Funzioni pubbliche


    def topologicalsort(self, graph : dict[int, list[Edge]], numNodes : int) -> list[int]:

        self.ordering : list[int] = [0] * numNodes
        self.visited : list[bool] = [False] * numNodes


        i : int = numNodes - 1

        for at in numNodes:
            if not self.visited[at]:
                i = self.__dfs(i, at, self.visited, self.ordering, graph)

        return self.ordering


    #Metodo privato

    def __dfs(self,i : int, at : int, visited : list[bool], ordering : list[int], graph : dict[int, list[Edge]]) -> int:

        self.visited[at] = True
        

        edges: list[self.Edge] = graph[at]


        if edges is not None:
            for e in edges:
                if not visited[e.to]:
                    i = self.__dfs(i, e.to, visited, ordering, graph)


        ordering[i] = at
        return i - 1
    

    #Funzione per trovare il shortestpath

    def dagShortestPath(self, graph : dict[int, list[Edge]], start : int, numNodes : int) -> list[int]:

        topsort : list[int] = self.topologicalsort(graph, numNodes)
        dist : list[int] = [0] * numNodes

        dist[start] = 0

        for i in numNodes:
            nodeIndex : int = topsort[i] 

            if dist[nodeIndex] is None:
                continue

            for edge in graph.get(nodeIndex, []):
                newDist : int = dist[nodeIndex] + edge.weight

                if dist[edge.to] is None or newDist < dist[edge.to]:

                    dist[edge.to] = newDist

        return dist
    









    