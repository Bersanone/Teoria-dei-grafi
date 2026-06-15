class TSPRecursive:

    def __init__(self, startNode : int, distance : list[list[float]]):

        self.distance = distance
        self.n = len(distance)
        self.start_node = startNode

        self.minTourCost = float("inf")

        self.tour = []

        self.ranSolver = False

        if self.n <= 2:
            raise TypeError("Eseguire TSP sotto i 3 nodi non ha senso")
        
        if self.n != len(distance[0]):
            raise TypeError("Matrice deve essere quadrata: (N x N)")
        if self.start_node < 0 or self.start_node >= self.n:
            raise TypeError("Starting node must be: 0 <= startNode < N")
        
        if self.n > 32:
            raise TypeError("La matrice è troppo grande, per un TSP DP con complessita temporale di O(n^2*2^n) servirebbe troppa computazione per qualsiasi computer domestico")

        self.finished_state = (1 << self.n) -1



    #Helpers

    def getTour(self) -> list[int]:
        if not self.ranSolver:
            self.solver()
        return self.tour
    



    def getTourCost(self) -> float:

        if not self.ranSolver:
            self.solver()
        return self.minTourCost



    
    #Solver


    def solver(self) -> None:

        state = 1 << self.start_node

        memo = [[None] * (1 << self.n) for _ in range(self.n)]

        prev = [[None] * (1 << self.n) for _ in range(self.n)]

        self.minTourCost = self.tsp(self.start_node,state,memo,prev)

        index = self.start_node

        while True:

            self.tour.append(index)

            nextIndex = prev[index][state]

            if nextIndex is None:
                break

            nextState = state | (1 << nextIndex)

            state = nextState

            index = nextIndex

        self.tour.append(self.start_node)
        self.ranSolver = True

        




    #Algoritmo TSP

    def tsp(self, i : int, state : int, memo : list[list[float]], prev : list[list[int]]) -> float:

        if state == self.finished_state:
            return self.distance[i][self.start_node]
        
        if memo[i][state] is not None:
            return memo[i][state]
        

        minCost = float("inf")

        index = -1

        for next_node in range(self.n):
            if (state & (1 << next_node) )!= 0:
                continue

            nextSTate = state | (1 << next_node)

            newCost = self.distance[i][next_node] + self.tsp(next_node, nextSTate, memo, prev)

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




