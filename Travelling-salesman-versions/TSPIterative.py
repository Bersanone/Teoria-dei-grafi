class TSPIterative:

    def __init__(self,start : int, distance : list[list[float]]):

        self.n = len(distance)

        if self.n <= 2:
            raise ValueError("Il numero dei nodi deve essere maggiore di 2.")
        
        if self.n != len(distance[0]):
            raise ValueError("La matrice deve essere quadrata: (N x N)")
        
        if start < 0 or start >= self.n:
            raise ValueError("Il nodo di partenza deve essere compreso tra 0 e N-1.")
        if self.n > 32:
            raise ValueError("La matrice è troppo grande, per un TSP DP con complessità temporale di O(n^2*2^n) servirebbe troppa computazione per qualsiasi computer domestico")



        self.start = start
        self.distance = distance
        self.tour = []
        self.minTourCost = float("inf")
        self.runSolver = False


    
    def getTour(self) -> list[int]:
        if not self.runSolver:
            self.solve()
        return self.tour
    

    def getTourCost(self) -> float:
        if not self.runSolver:
            self.solve()
        return self.minTourCost



    def combinations(self,r : int,n : int) -> list[int]:
        subsets = []
        self.__combination(0,0,r,n,subsets)
        return subsets
    
    #Funzione di solver

    def solve(self) -> None:
        if self.runSolver:
            return
        
        END_STATE = (1 << self.n) - 1
        #1 << start → crea una maschera con un solo bit acceso nella posizione di start partendo da sinistra (es. start=2 → 0b0100 , notiamo come l'1 è stato inserito dopo 2 zeri partendo da destra) 
        memo = [[None] * (1 << self.n) for _ in range(self.n)]

        #Fase 1

        for end in range(self.n):
            if end == self.start:
                continue
            memo[end][(1<<self.start) | (1<<end)] = self.distance[self.start][end]


        #Fase 1a

        for r in range(3,self.n + 1):
            for subset in self.combinations(r, self.n):
                if self.__notIn(self.start, subset):
                    continue
                for next in range(self.n):
                    if next == self.start or self.__notIn(next, subset):
                        continue
                    #Consideriamo tutti i possibili nodi precdenti
                    subsetWithoutNext = subset ^ (1 << next)
                    MinDist = float("inf")
                    for end in range (self.n):
                        if end == self.start or end == next or self.__notIn(end,subset):
                            continue
                        newDistance = memo[end][subsetWithoutNext] + self.distance[end][next]
                        if newDistance < MinDist:
                            MinDist = newDistance
                        
                    memo[next][subset] = MinDist

        #Fase 2

        for i in range(self.n):
            if i == self.start:
                continue
            tourCost = memo[i][END_STATE] + self.distance[i][self.start]
            if tourCost < self.minTourCost:
                self.minTourCost = tourCost


        #Fase 3

        lastIndex = self.start
        state = END_STATE
        self.tour.append(self.start)

        for i in range(1,self.n):
            bestIndex = -1
            bestDist = float("inf")

            for j in range(self.n):
                if j == self.start or self.__notIn(j,state):
                    continue
                newDist = memo[j][state] + self.distance[j][lastIndex]
                if newDist < bestDist:
                    bestIndex = j
                    bestDist = newDist
                
                self.tour.append(bestIndex)
                state = state ^ (1 << bestIndex)
                lastIndex = bestIndex

            self.tour.append(self.start)
            self.tour.reverse()

            self.runSolver = True
    











    #Private helpers

    #Costruisce recursivamente le combinazione, decidendo se includer eogni posizione di bit, arretra quando non ci sono abbastanza combinazioni 

    def __combination(self, set : int,at : int,r : int,n : int,subset : list[int]) -> None:

        elementsLeftToPick = n - at

        if elementsLeftToPick < r:
            return
        
        if r == 0:
            subset.append(set)
        else:
            for i in range(at,n):
                #Usiamo l'operatore XOR per provare ad aggiungere il bit i-esimo al set
                #se il bit i di et era 0 → diventa 1
                #se il bit i di et era 1 → diventa 0
                set ^= (1 << i)
                self.__combination(set, i + 1, r - 1,n,subset)

                #Eseguiamo un backtrack e proviamo l'istanza senza il bit i-esimo
                set ^= (1 << i)


    def __notIn(self,elem : int,subset : int) -> bool:
        return ((1 << elem) & subset) == 0


    #-------------------------MAIN-------------------------


def main() -> None:

        n = 0
        distanceMatrix = [[] for _ in range(n)]
        for row in distanceMatrix:
            row.append(10000)
        
        distanceMatrix[5][0] = 10
        distanceMatrix[1][5] = 12
        distanceMatrix[4][1] = 2
        distanceMatrix[2][4] = 4
        distanceMatrix[3][2] = 6
        distanceMatrix[0][3] = 8

        startNode = 0

        solver = TSPIterative(startNode, distanceMatrix)

        print("Tour ottimale:", solver.getTour())

        print("Costo del tour ottimale:", solver.getTourCost())


