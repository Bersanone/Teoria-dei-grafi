'''
Questo file contiene un implementazione ricursiva del TSP, utilizzando la programmazione dinamica

L'idea principale è essendo che dobbiamo eseguire n! permutazioni di tutti i nodi per trovare la soluzione ottimale possiamo introdurre del caching per migliorare le performance

Per esempio, se una permutazione è '...DABC' successivamente dovremmo computare il valore della permutazione '...EBAC' dovremmo avere cachato il risultato per il sotto grafo contennete i nodi {A,B,C}


Complessità temporale: O(n^2 * 2^n)

Complessità spaziale: O(n * 2^n)



'''




class TSPRecursive:

    def __init__(self, startNode : int, distance : list[list[float]]):




        self.distance = distance
        self.n = len(distance)
        self.start_node = startNode

        #Caching

        self.minTourCost = float("inf")

        self.tour = []

        self.ranSolver = False

        #Controllo della matrice

        if self.n <= 2:
            raise TypeError("Eseguire TSP sotto i 3 nodi non ha senso")
        
        if self.n != len(distance[0]):
            raise TypeError("Matrice deve essere quadrata: (N x N)")
        if self.start_node < 0 or self.start_node >= self.n:
            raise TypeError("Starting node must be: 0 <= startNode < N")
        
        if self.n > 32:
            raise TypeError("La matrice è troppo grande, per un TSP DP con complessita temporale di O(n^2*2^n) servirebbe troppa computazione per qualsiasi computer domestico")
        
        #Salviamo l'indice finale dei nodi

        #La maschera finale di stato ha tutti i bit impostati ad 1

        self.finished_state = (1 << self.n) -1



    #Helpers


    #Ritorna il tour ottimale per TSP

    def getTour(self) -> list[int]:
        if not self.ranSolver:
            self.solver()
        return self.tour
    


    #Ritorna il costo minimo


    def getTourCost(self) -> float:

        if not self.ranSolver:
            self.solver()
        return self.minTourCost



    
    #Solver


    def solver(self) -> None:

        #Salviamo la mask con l'index dello start

        state = 1 << self.start_node

        #Prepariamo le matrici di caching

        memo = [[None] * (1 << self.n) for _ in range(self.n)]

        prev = [[None] * (1 << self.n) for _ in range(self.n)]

        #Eseguiamo recursivamente il tsp

        self.minTourCost = self.tsp(self.start_node,state,memo,prev)

        #Puntatore al nodo corrente, parte da start_node

        index = self.start_node

        while True:

            #Salviamo l'index nel tour

            self.tour.append(index)

            #Salviamo il prossimo index

            nextIndex = prev[index][state]

            if nextIndex is None:
                break

            #Aggiornamento della mask

            nextState = state | (1 << nextIndex)

            state = nextState

            #Cambiamo l'index

            index = nextIndex

        #Chiudiamo con il nodo di start

        self.tour.append(self.start_node)
        self.ranSolver = True

        




    #Algoritmo TSP

    def tsp(self, i : int, state : int, memo : list[list[float]], prev : list[list[int]]) -> float:

        #Se il tour è stato eseguito ritorna il costo di ritornare allo starting node

        if state == self.finished_state:
            return self.distance[i][self.start_node]
        
        #Restituiamo le risposte cachate se presenti
        
        if memo[i][state] != None:
            return memo[i][state]
        

        minCost = float("inf")

        index = -1

        for next_node in range(self.n):
            #Skippiamo se il nodo è già stato visitato
            if (state & (1 << next_node) )!= 0:
                continue

            #Aggiornamento della mask

            nextSTate = state | (1 << next_node)

            #Aggiorniamo le distanze

            newCost = self.distance[i][next_node] + self.tsp(next_node, nextSTate, memo, prev)

            #Aggiorniamo il costo minimo se presente

            if newCost < minCost:
                minCost = newCost
                index = next_node


        prev[i][state] = index
        res = memo[i][state] = minCost
        return res
    




    #Funzione di main


if __name__ == "__main__":

        n = 6
        distanceMatrix = [[float("inf")] * n for _ in range(n)]

        distanceMatrix[1][4] = distanceMatrix[4][1] = 2
        distanceMatrix[4][2] = distanceMatrix[2][4] = 4
        distanceMatrix[2][3] = distanceMatrix[3][2] = 6
        distanceMatrix[3][0] = distanceMatrix[0][3] = 8
        distanceMatrix[0][5] = distanceMatrix[5][0] = 10
        distanceMatrix[5][1] = distanceMatrix[1][5] = 12


        solver2 = TSPRecursive(0,distanceMatrix)

        print(f"Tour {solver2.getTour()}")
        print(f"Tour cost {solver2.getTourCost()}")



