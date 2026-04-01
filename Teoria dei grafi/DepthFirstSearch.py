'''
Il DepthFirstSearch è un algoritmo per traversare recursivamente dei nodi,
Questa versione usa le liste di adiacenza list[list[int] per rappresentare le connessioni tra nodi.
Partiamo da un nodo e iniziamo a visitare tutti i suoi vicini, un nodo non può essere ripercorso più di una volta
Se incontriamo un nodo già visitato dobbiamo fare marcia indietro in modo recursivo per provare strade diverse e trovare nodi mai percorsi

Time: O(V+E)
Space: O(V)
'''



class DepthFirstSearch:

    def __init__(self):
        pass


    def main(self) -> None:

        n : int = 7
        graph : list[int] = self.__craetegraph(n)

        self.__addDirectedEdge(graph,0,1)
        self.__addDirectedEdge(graph,0,2)
        self.__addDirectedEdge(graph,1,3)
        self.__addDirectedEdge(graph,1,4)
        self.__addDirectedEdge(graph,4,5)


        print(f"DFS from 0 : {self.dfs(0,graph)} Nodes")
        print(f"DFS from 6 : {self.dfs(6,graph)} Nodes")



    def dfs(self,start, graph:list[list[int]]) -> int:
        return self.__dfs(at = start, visited = [False]*len(graph), graph = graph)




    def __dfs(self,at: int, visited: list[bool], graph: list[list[int]]) -> int:

        #Se visitato restituiamo 0

        if visited[at]:
            return 0
        
        #Impostiamo il nodo come visitato
        
        visited[at] = True

        # set del counter ad 1

        count = 1

        #Chiamata ricorsiva della funzione su tutti i nodi del grafo
        for i in graph[at]:
            count += self.__dfs(i,visited,graph)
        return count
    




    def __craetegraph(self,n : int) -> list[list[int]]:
        #Creiamo una nuova lista e assegnamo size numero di nodi
        graph : list[list[int]] = [[] for _ in range(n)]

        return graph
    

    def __addDirectedEdge(self, graph : list[list[int]], from_node: int, to : int) -> None:

        #Creiamo gli archi ai nodi

        graph[from_node].append(to)


    

        

p = DepthFirstSearch() 

p.main() 

'''
DFS from 0 : 6 Nodes
DFS from 6 : 1 Nodes
'''