class tspBrute:

    def tsp (self,matrix : list[list[float]]) -> list[int]:

        n = len(matrix)

        permutation = [[0] for _ in range(n)]

        for i in range(n):
            permutation[i] = i

        bestTour = permutation.copy()

        bestTourCost = float("inf")

        while True:

            tourCost = self.computeTourCost(permutation, matrix)

            if tourCost < bestTourCost:

                bestTourCost = tourCost
                bestTour = permutation.copy()
            
            if not self.nextPermutation(permutation):
                break


        return bestTour





    def nextPermutation(self, sequence : list[int]) -> bool:

        first = self.getFirst(sequence)

        if first == -1:
            return False
        
        toSwap = len(sequence) -1

        while sequence[first] >= sequence[toSwap]:
            toSwap -= 1

        self.swap(sequence,first,toSwap)
        first+=1
        toSwap = len(sequence) - 1 

        while first < toSwap:
            self.swap(sequence, first,toSwap)
            first += 1
            toSwap -= 1


        return True
    





    def computeTourCost(self, tour : list[int], matrix : list[list[float]]) -> float:

        cost = 0

        for i in range(1,len(matrix)):
            from_ = tour[i -1]
            to = tour[i]
            cost += matrix[from_][to]


        last = tour[len(matrix) - 1]

        first = tour[0]

        return cost + matrix[last][first]
    






    #Funzione di main


    def main(self) -> None:

        n = 10

        matrix = [[n] * n for _ in range(n)]


        edgeCost = 5

        optimalTour = [2, 7, 6, 1, 9, 8, 5, 3, 4, 0, 2]

        for i in range(1,len(optimalTour)):
            matrix[optimalTour[i - 1]][optimalTour[i]] = edgeCost


        bestTour : list[int]  = self.tsp(matrix)

        print(bestTour)


        tourCost = self.computeTourCost(bestTour,matrix)

        print(f"Tour cost: {tourCost}")












    #Private functions

    def swap(self,sequence : list[int], i : int, j : int) -> None:

        tmp = sequence[i]

        sequence[i] = sequence[j]

        sequence[j] = tmp



    def getFirst(self, sequence : list[int]) -> int:

        #Impostiamo gli iteratori direttamente all'interno del range
        #il primo -1 indica di fermarsi quando arriva a 0
        #Mentre il secondo indica di quanto deve decrementare il numero

        for i in range(len(sequence) -2,-1,-1):
            if sequence[i] < sequence[i + 1]:
                return i
            
        return -1
    





p = tspBrute()

p.main()










    
