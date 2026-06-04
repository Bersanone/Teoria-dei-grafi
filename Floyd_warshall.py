#L'algoritmo di Floyd-Warshall è un algoritmo di programmazione dinamica che risolve il problema del percorso più breve tra tutte le coppie di nodi in un grafo pesato.
# anche con pesi negativi, questa versione implementa pure la gestione dei cicli negativi.
#L'algoritmo utilizza una matrice memo per memorizzare le distanze minime tra i nodi e una matrice per ricostruire i percorsi più brevi.
#La complessità temporale dell'algoritmo è O(n^3), dove n è il numero di nodi nel grafo.

#In parole povere segna prima un arco tra start ed end esempio (2,8) con un peso w, poi segna un arco tra start e k (2,5) con peso w1 e infine segna un arco tra k ed end (5,8) con peso w2. Se w1 + w2 < w allora aggiorna il peso dell'arco tra start ed end a w1 + w2. ù
#Ripeti questo processo per ogni coppia di nodi e per ogni nodo intermedio k. 
# Alla fine avrai la matrice delle distanze minime tra tutte le coppie di nodi.





class floydWarshall:

    def __init__(self, matrix : list[list[float]]):
        #Check se la matrice è vuota o None
        if matrix is None or len(matrix) == 0:
            raise ValueError("Matrix must be non-empty")
        
        #Inizializzazione della matrice di distanza e della matrice di ricostruzione del percorso
        
        self.n = len(matrix)
        #Matrice di distanze
        self.dp = [[float('inf')] * self.n for _ in range(self.n)]
        #Matrice per ricostruire i percorsi più brevi
        self.next = [[-1] * self.n for _ in range(self.n)]
        self.solved = False

        #Inizializzazione della matrice di distanza e della matrice di ricostruzione del percorso con i valori iniziali della matrice di input
  
        for i in range(self.n):
            for j in range(self.n):
                #Se c'è un arco tra i e j, inizializza la distanza e il percorso
                if matrix[i][j] != float("inf"):
                    self.next[i][j] = j
                    self.dp[i][j] = matrix[i][j]


    
    #Esecuzione del algoritmo di Floyd-Warshall

    def solve(self) -> None:
        #Se l'algoritmo è già stato risolto, non eseguirlo di nuovo
        if self.solved:
            return
        
        #Itera su ogni nodo intermedio k, su ogni coppia di nodi i e j
        
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    #Se la distanza da i a k e da k a j è minore della distanza da i a j, aggiorna la distanza e il percorso
                    if self.dp[i][k] + self.dp[k][j] < self.dp[i][j]:
                        self.dp[i][j] = self.dp[i][k] + self.dp[k][j]
                        #Aggiorna il percorso da i a j passando per k
                        self.next[i][j] = self.next[i][k]

        #Dopo avere controllato le distanze verifichiamo la presenza di cicli negativi

        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    #Se la distanza da i a k è diversa da inf e la distanza da k a j è diversa da inf e la distanza da k a k è negativa, allora c'è un ciclo negativo
                    if self.dp[i][k] != float('inf') and self.dp[k][j] != float("inf") and self.dp[k][k] < 0:
                        #Se c'è un ciclo negativo, imposta la distanza da i a j a -inf e il percorso a -1
                        self.dp[i][j] = float("-inf")
                        self.next[i][j] = -1

        self.solved = True



    #Funzione per ottenere la matrice ASPS (All Pairs Shortest Path)
    #Esegue floyd-warshall per calclare la distanza minima tra tuute le coppie di nodi


    def getAspsMatrix(self) -> list[list[float]]:
        self.solve()
        return self.dp



    #Funzione per ricostruire il percorso più breve tra due nodi


    def rwconstructPath(self, start : int, end : int) -> list[int]:
        #Istanziamo solve ed una lista di path
        self.solve()
        path : list[int] = []
        #Se la distanza da start a end è inf, non c'è un percorso, quindi restituisci una lista vuota
        if self.dp[start][end] == float('inf'):
            return path
        
        #Iniziamo a ricostruire il percorso
        at : int = start 

        #Seguiamo la matrice next fino a raggiungere la destinazione

        while at != end:
            at = self.next[at][end]
            #Se at è -1, significa che non c'è un percorso da start a end, quindi restituisci None
            if at == -1:
                return None
            
        path.append(end)
        return path
    

    #Creiamo una matrice di adiacenza inizializzata con +inf e 0 diagonali

    def createGraph(self, n : int) -> list[list[float]]:
        matrix : list[list[float]] = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            #La distanza da un nodo a se stesso è 0
            matrix[i][i] = 0

        return matrix
    


    #Utility per formattare il path

    def formatPath(self, path : list[int], start : int, end :  int) -> str:
        if path is None:
            return "NEGATIVE CYCLE"
        if len(path) == 0:
            return f"NO PATH FROM {start} TO {end}"
        
        return "->".join(str(node) for node in path)
    


    #Funzione di prova dell'algoritmo di Floyd-Warshall con cicli negativi

    def exampleWithNegativeCycles(self) -> None:
        n : int = 4
        m : list[list[float]] = self.createGraph(n)
        m[0][1] = 4
        m[1][2] = 1
        m[2][3] = 2
        m[3][2] = -5

        solver : floydWarshall = floydWarshall(m)
        dist : list[list[float]] = solver.getAspsMatrix()

        print("=== Example 1: Negative cycle ===")
        print(f"Dist 0,1 {dist[0][1]}")
        print(f"Dist 0,2 {dist[0][2]}")
        print(f"path 0,1 {self.formatPath(solver.rwconstructPath(0,2),0,2)}")
        print(f"path 0,1 {self.formatPath(solver.rwconstructPath(0,1),0,1)}")




    def exampleSimpleGraph(self) -> None:
        n : int = 4
        m : list[list[float]] = self.createGraph(n)
        m[0][1] = 1
        m[1][2] = 3
        m[1][3] = 10
        m[2][3] = 2

        solver : floydWarshall = floydWarshall(m)
        dist : list[list[float]] = solver.getAspsMatrix()

        print("=== Example 2: Simple Graph ===")
        print(f"dist 0,3 {dist[0][3]}")
        print(f"path 0,3 {self.formatPath(solver.rwconstructPath(0,3),0,3)}")
        print(f"path 3,0 {self.formatPath(solver.rwconstructPath(3,0),3,0)}")



    #Funzione di main

    def main(self) -> None:
        self.exampleWithNegativeCycles()
        self.exampleSimpleGraph()






p = floydWarshall([[0]])
p.main()


