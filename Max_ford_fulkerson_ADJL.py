
#    Implementazione del metodo ford-fulkerson (FF) con una DFS per inccrementare i paths.
#    FF ci permette di trovare il flusso massimo che può passare attraverso un grafo diretto.
#    ecco un esempio visivo:

# ---------------------------------------------------------------------------
# Ford-Fulkerson (max flow)
#
# Rete di flusso: ogni arco ha una capacità massima. Si cerca il flusso
# massimo da S (sorgente) a T (pozzo).
#
# Grafo iniziale (numero = capacità dell'arco):
#
#         ┌──── 10 ────►(A)──── 10 ────┐
#         │              │             │
#         │              │             ▼
#        (S)             │ 1          (T)
#         │              │             ▲
#         │              ▼             │
#         └──── 10 ────►(B)──── 10 ────┘
#
# Algoritmo:
#   1. Parti con flusso 0 su ogni arco.
#   2. Cerca un cammino S → T nel grafo residuo (DFS/BFS) con capacità
#      residua > 0 su ogni arco.
#   3. Spingi lungo il cammino il bottleneck (minimo delle residue).
#   4. Aggiorna: residua(u→v) = cap - flusso, residua(v→u) = flusso.
#   5. Ripeti finché non esiste più un cammino. Il flusso totale è il massimo.
#
# Cammini aumentanti dell'esempio (scelti apposta per usare l'arco A → B):
#   1) S → A → B → T   bottleneck = 1   totale = 1
#   2) S → A → T       bottleneck = 9   totale = 10
#   3) S → B → T       bottleneck = 9   totale = 19
#   4) S → B → A → T   bottleneck = 1   totale = 20
#      B → A è l'arco residuo inverso: annulla il flusso 1 messo su A → B
#      al passo 1. Questo "ripensamento" è ciò che rende l'algoritmo corretto.
#
# Stato finale (flusso/capacità), flusso massimo = 20:
#
#         ┌─── 10/10 ──►(A)─── 10/10 ──┐
#         │              │             │
#         │              │             ▼
#        (S)             │ 0/1        (T)
#         │              │             ▲
#         │              ▼             │
#         └─── 10/10 ──►(B)─── 10/10 ──┘
#
# Taglio minimo = {A → T, B → T} = 10 + 10 = 20 (max-flow min-cut theorem).
#
# Complessità temporale:
#   - Ford-Fulkerson con DFS: O(fV^2), dove f è il flusso massimo
# ---------------------------------------------------------------------------

import sys


class FordFulkersonDFSAdjacencyMatrix:

    def __init__(self,caps : list[list[int]], source : int, sink : int):

        self.visitedToken : int = 1
        self.n : int = caps.length
        self.visited : list[int] = [0] * self.n
        self.minCut : list[bool] = [False] * self.n

        maxFlow : int = 0 
        while True:
            #Assegnamo sys.maxsize (infinito) al parametro flow come flusso 

            flow : int = self.dfs(caps,self.visited,source,sink,sys.maxsize)
            visitedToken += 1

            maxFlow += flow
            if flow == 0:
                return maxFlow


    def dfs(self,caps : list[list[int]], visited : list[int], node : int, sink : int, flow : int ) -> int:

        #Trova il sink node, restituisce il flow attuale

        if node == sink:
            return flow

        #Cap sta per capacità, ovvero quanto flow può essre spinto ancora dentro

        cap : list[int] = caps[node]
        visited[node] = self.visitedToken

        for i in range(len(cap)):
            if visited[i] != self.visitedToken and cap[i] > 0:
                if cap[i] < flow:
                    flow = cap[i]

                dfsFlow : int = self.dfs(caps,visited,i,sink,flow)

                if dfsFlow > 0:
                    caps[node][i] -= dfsFlow
                    caps[i][node] += dfsFlow
                    return dfsFlow

        return 0








