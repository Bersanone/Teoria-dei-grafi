'''
Dato un grafo pesato completo di N nodi, dobbiamo trovare il ciclo Hamiltoniano a minor costo (un tour che visita ogni nodo esattemente una volta sola e ritorna al nodo di partenza)

Questo approccio iterativo (bottom-up) costruisce soluzioni per incrementare la taglia del subset, per ogni subset di 5 nodi visitati e ogni endpoint node i size computiamo il costo minimoper raggiungere i avendo visistato i nodi in Size

    memo[next][S | (1 << next)] = min over end in S of
        memo[end][S] + distance[end][next]

Dopo aver riempito le tabelle chiudiamo il tour connettendoci indietro al nodo di partenza ed esegue un backtrack attreverso la tabella per ricostruire il path ottimale

 Time:  O(n^2 * 2^n)
 Space: O(n * 2^n)


'''



class TSPIterative:

    #Dichiarazione del costruttore

    def __init__(self,start : int, distance : list[list[float]]):

        self.n = len(distance)

        #Check dei nodi

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


    

    #Ritorna una lista di tour ottimali per il TSP
    
    #Restituiamo una lista ordinata di indici dei nodi  formando il tour ottimale (inizia e finisce con il nodo di partenza)
    def getTour(self) -> list[int]:
        if not self.runSolver:
            self.solve()
        return self.tour
    

    #Restituisce il costo minimo del tour

    #Restituisce il costyo totale del ciclo hamiltoniano
    

    def getTourCost(self) -> float:
        if not self.runSolver:
            self.solve()
        return self.minTourCost



    def combinations(self,r : int,n : int) -> list[int]:
        subsets = []
        self.__combination(0,0,r,n,subsets)
        return subsets
    
    #Funzione di solver

    #Solve TSP ed esegue il chacing dei risultati, chiamate subseguenti sono no-ops


    #Fase 1: riempiamo la tabella DP bottom-up per subset di 2..N
    #Fase 2: Chiudiamo il tour connetetndo l'ultimo nodo indietro all'inzio
    #Fase 3: Eseguiamo il backtrack attraverso la tabella per ricostruire il tour

    def solve(self) -> None:
        if self.runSolver:
            return
        
        END_STATE = (1 << self.n) - 1
        #1 << start → crea una maschera con un solo bit acceso nella posizione di start partendo da sinistra (es. start=2 → 0b0100 , notiamo come l'1 è stato inserito dopo 2 zeri partendo da destra) 
        memo = [[None] * (1 << self.n) for _ in range(self.n)]

        #Fase 1a: riempiamo la tabella memmo con gli edges diretti dal nodo di partenza

        for end in range(self.n):
            if end == self.start:
                continue
            #memo[end][{start, end}] = distanza da start ad end

            memo[end][(1<<self.start) | (1<<end)] = self.distance[self.start][end]


        #Fase 1b: Costruiamo soluzioni per subset di taglia incrementale (3..N)
        #Per ogni subset proviamo ad estendere il path ad ogni nodo nel subset

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

        #Chiudiamo il tour - trovando il modo più conveniente per ritornare allo start

        for i in range(self.n):
            if i == self.start:
                continue
            tourCost = memo[i][END_STATE] + self.distance[i][self.start]
            if tourCost < self.minTourCost:
                self.minTourCost = tourCost


        #Fase 3 ricostruiamo il tour eseguendo il backtrack attraverso la tabella memo 

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

    #Genera tutte le bitmask di n bits dove esattamente r bits sono impostati

    #Utilizzato per enumera subset di una data size


    #@param r - numero di bits da impostare
    #@param n - numero totale di bits
    #@return - lista di interi bitmask 

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



    #Restituisce True se i bit dell'elemento dato non è nel subset bitmask


    def __notIn(self,elem : int,subset : int) -> bool:
        return ((1 << elem) & subset) == 0


    #-------------------------MAIN-------------------------


def main() -> None:

        n = 6

        #Assegnamo 10000 come placeholedr

        distanceMatrix =[ [10000] * n for _ in range(n)]

        
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


p = main()


