'''
Implementazione di un algoritmo di Dijkstra utilizzando un D-Heap come struttura dati per la coda di priorità.

L'algoritmo di Dijkstra è un algoritmo di ricerca del percorso più breve in un grafo con pesi non negativi.

Possiamo trovare la strada migliore da un nodo di partenza ad uno di arrivo, solo quando esploriamo tutti i nodi vicini al nodo di arrivo



COMMENTARE IL CODICE PER SPIEGARE IL FUNZIONAMENTO DELL'ALGORITMO E DELLA STRUTTURA DATI UTILIZZATA
'''

from collections import deque





class dijkstraAlgorithmWithDHeap:


    #Definizione del costruttore

    def __init__(self):
        self.n = 0
        #Numero di edge per nodo
        self.edgeCount = 0
        #Distanza minima da start a ogni nodo
        self.dist =  []
        #Nodo precedente del nodo corrente, usato per ricostruire il percorso
        self.prev = []
        self.graph = []
    
    #Definizione delle classi interne per rappresentare edge e nodi
    class Edge:

        def __init__(self, fromNode : int, to : int, cost : float):
            self.fromNode = fromNode
            self.to = to
            self.cost = cost

    class Node:

        def __init__(self, id : int, value : float):
            self.id = id
            self.value = value

        #Il metodo __lt__ è utilizzato per confrontare due nodi in base al loro valore, che rappresenta la distanza minima da start a quel nodo. 
        #Lo istanziamo per dire a python come confrontare due nodi quando li inseriamo nella coda di priorità (D-Heap).
        #Questo è necessario per mantenere l'ordine corretto nella coda di priorità (D-Heap) durante l'esecuzione dell'algoritmo di Dijkstra.

        def __lt__(self, other):
            return self.value < other.value


    
    def DijkstrasShortestPathAdjacencyList(self,n : int) -> None:

        self.n = n
        #Aggiungiamo un array vuoto per ogni nodo
        self.graph = [[] for _ in range(n)]
        self.edgeCount = 0

    
    #Funzione per aggiungere un edge al grafo. Prende in input il nodo di partenza, il nodo di arrivo e il costo dell'edge.
    def addEdge(self, fromNode : int, to : int, cost : float) -> None:
        #Aggiungiamo l'edge alla lista di adiacenza del nodo di partenza. 
        #La lista di adiacenza è una lista di liste, dove ogni elemento rappresenta un nodo e contiene una lista di edge che partono da quel nodo.
        self.graph[fromNode].append(self.Edge(fromNode, to, cost))
        #AGgiorniamo il count degli edge
        self.edgeCount += 1

    #Funzione per restituire il grafo
    def getGraph(self) -> list[list[Edge]]:
        return self.graph
    

    def Dijkstra(self, start : int, end : int) -> float:

        #Impostiamo il grado del D-Heap in base al numero di edge per nodo, calcolato come edgeCount (edge totali) diviso n (numero di nodi).
        degree = self.edgeCount // self.n
        #Istanziamo la coda di priorità (D-Heap) utilizzata nell'algoritmo di Dijkstra
        ipq = self.DHeap()
        #Inizializziamo il D-heap con il grado calcolato e la dimensione massima pari al numero di nodi, per garantire che la struttura del D-Heap possa contenere tutti i nodi del grafo.
        ipq.MinIndex(degree, self.n)
        #Inseriamo il nodo di partenza nella coda di priorità (D-Heap) con un valore iniziale di 0, poiché la distanza da start a se stesso è sempre 0.
        ipq.insert(start, 0.0)

        #Inizializziamo l'array dist con valori infiniti per rappresentare la distanza minima da start a ogni nodo, tranne che per il nodo di partenza (start), che viene impostato a 0.
        self.dist = [float('inf')] * self.n
        self.dist[start] = 0


        #Inizalizziamo l'array visited con valori booleani per tenere traccia dei nodi già visitati durante l'esecuzione dell'algoritmo di Dijkstra, 
        #inizialmente impostati a False per tutti i nodi.
        visited = [False] * self.n

        #Inizializziamo l'array prev con valori None per tenere traccia del nodo precedente di ogni nodo durante l'esecuzione dell'algoritmo di Dijkstra,
        self.prev = [None] * self.n

        #Il ciclo while continua finché la coda di priorità (D-Heap) non è vuota, ovvero finché ci sono ancora nodi da esplorare.
        while ipq:

            #Prendiamo l'indice e il valore del nodo con la distanza minima da start (quindi start)
            nodeid = ipq.peekMinKeyIndex()

            minValue = ipq.poolMinValue()

            #Se il valore minimo estratto dalla coda di priorità è maggiore della distanza minima attualmente registrata per il nodo nodeid
            #significa che abbiamo già trovato un percorso più breve per quel nodo e possiamo saltare l'elaborazione di quel nodo.

            if minValue < self.dist[nodeid]:
                continue

            #Per ogni edge che parte dal nodo nodeid, controlliamo se il nodo di arrivo dell'edge è già stato visitato.

            for edge in self.graph[nodeid]:
                #In caso fosse già stato visitato, saltiamo l'elaborazione di quell'edge, poiché abbiamo già trovato un percorso più breve per quel nodo di arrivo.
                if visited[edge.to]:
                    continue
                #In caso contrario calcoliamo la nuova distanza da start al nodo di arrivo dell'edge (edge.to), 
                #sommando la distanza minima da start con il costo dell'edge (edge.cost).

                new_dist = self.dist[nodeid] + edge.cost

                #Se la nuova distanza calcolata è minore della distanza minima attualmente registrata per il nodo di arrivo dell'edge (edge.to),
                if new_dist < self.dist[edge.to]:
                    #Impostiamo il nodo precedente del nodo di arrivo dell'edge (edge.to) al nodo nodeid, poiché abbiamo trovato un percorso più breve da start a edge.to passando per nodeid.
                    self.prev[edge.to] = nodeid
                    #Aggiorniamo il valore della distanza minima
                    self.dist[edge.to] = new_dist
                    #Se il nodo di arrivo dell'edge (edge.to) è già presente nella coda di priorità (D-Heap), 
                    #aggiorniamo il suo valore con la nuova distanza più breve utilizzando il metodo decrease.
                    if ipq.contains(edge.to):
                        ipq.decrease(edge.to, new_dist)
                    else:
                        #Altrimenti inseriamo il nuovo edge con la relativa distanza
                        ipq.insert(edge.to, new_dist)

            #Se il nodo nodeid è uguale al nodo di arrivo (end) che stiamo cercando, 
            # possiamo restituire la distanza minima da start a end, poiché abbiamo trovato il percorso più breve da start a end.
            if nodeid == end:
                return self.dist[end]
        #Se il ciclo while termina senza trovare il nodo di arrivo (end), significa che non esiste un percorso da start a end, 
        #quindi restituiamo infinito per indicare che la distanza è illimitata.
        return float('inf')
    

    #Funzione per ricostruire il percorso più breve da start a end dopo aver eseguito l'algoritmo di Dijkstra. 
    #Restituisce una lista di nodi che rappresentano il percorso più breve, o una lista vuota se non esiste un percorso.

    def reconstructPath(self, start : int, end : int) -> list[int]:
        #Istanziamo l'algoritmo di Dijkstra per calcolare le distanze minime dal nodo di start a quello di end
        self.Dijkstra(start,end)
        #Istanziamo una deque per memorizzare il percorso più breve da start a end. 
        # Utilizziamo una deque (double Linked List) perché ci permette di aggiungere nodi sia all'inizio che alla fine della struttura, facilitando la ricostruzione del percorso in ordine corretto.
        path = deque()

        #Se la distanza minima da start a end è ancora infinita, significa che non esiste un percorso da start a end, quindi restituiamo una lista vuota.

        if self.dist[end] == float('inf'):
            return path
        
        #Impostiamo la variabile at al nodo di end
        at = end

        #Fino a che at non raggiunge il nodo di origine

        while at != start:
            #Aggiungiamo il nodo at all'inizio della deque path, poiché stiamo ricostruendo il percorso da end a start.
            path.appendleft(at)
            #avanziamo verso l'alto nella catena dei nodi precedenti, 
            #impostando at al nodo precedente di at (self.prev[at]), per continuare a ricostruire il percorso fino a raggiungere il nodo di origine (start).
            at = self.prev[at]
        
        #Terminiamo il ciclo quando at raggiunge start, quindi aggiungiamo start all'inizio della deque path per completare la ricostruzione del percorso da start a end.
        path.appendleft(start)

        #Restituiamo la lista

        return list(path)
    
    #Istanza della classe DHeap, che rappresenta la coda di priorità utilizzata nell'algoritmo di Dijkstra.
    
    class DHeap:

        def __init__(self):
            self.sz = 0
            #Numero di nodi nel D-Heap
            self.N = 0
            #Indica il grado del D-Heap, ovvero il numero di figli per ogni nodo
            self.D = 0
            #Array che mappa l'indici dei figli del node corrente, utilizzato per navigare verso il bassonella struttura del D-Heap.
            self.child = []
            #Array che mappa l'indice del genitore del nodo corrente, utilizzato per navigare verso l'alto nella struttura del D-Heap.
            self.parent = []
            #Istanza della position map, serve per mappare un indice di nodo al suo indice nella coda di priorità (D-Heap).
            self.pm = []
            #Istanza dell'inverse map, serve per mappare un indice nella coda di priorità (D-Heap) all'indice del nodo corrispondente.
            self.im = []
            #Array che memorizza i valori associati a ogni nodo nella coda di priorità (D-Heap), ovvero la distanza minima da start a quel nodo.
            self.values = []

        #Il metodo __bool__ è utilizzato per verificare se la coda di priorità è vuota o meno. 
        #Restituisce true se la coda di priorità contiene almeno un elemento, altrimenti false.
        #Utilizziamo questo metodo per semplificare la condizione di uscita del ciclo while nell'algoritmo di Dijkstra, che continua finché la coda di priorità non è vuota.
        def __bool__(self):
            return self.sz > 0
    
        #Metodo per inizializzare la coda di priorità (D-Heap) con un grado specifico e una dimensione massima.

        def MinIndex(self, degree: int, maxSize : int) -> None:
            #Controllo per evitare size negative o nulle
            if maxSize <= 0:
                raise ValueError("maxSize must be greater than 0")
            
            #Impostiamno i degree del D-Heap al massimo tra 2 e il degree passato come argomento, per garantire che il D-Heap abbia almeno 2 figli per nodo.
            self.D = max(2, degree)
            #Settiamo il numero massimo di nodi nella coda di priorità al massimo tra D+1 e maxSize, per garantire che la struttura del D-Heap possa contenere almeno D+1 nodi (ovvero un nodo con D figli).
            self.N = max(self.D + 1, maxSize)

            #Inizializziamo la inverse map e la position map con un placeholder moltiplicato per n

            self.im = [0] * self.N
            self.pm = [0] * self.N

            #Stessa cosa per child,parent e values

            self.child = [0] * self.N
            self.parent = [0] * self.N

            self.values = [0] * self.N

            #Per ogni nodo

            for i in range(self.N):
                #Impostiamo il genitore del nodo i al valore calcolato come (i-1) // D, che rappresenta l'indice del genitore nella struttura del D-Heap.
                # i-1 perché l'indice 0 è la radice del D-Heap e non ha genitore, quindi il primo nodo con genitore è l'indice 1.
                #Dividiamo per D perché ogni nodo ha D figli, quindi il genitore di un nodo i si trova a (i-1) // D nella struttura del D-Heap.
                self.parent[i] = (i-1) // self.D
                #Per calcolare l'indice del primo figlio del nodo i, utilizziamo la formula i * D + 1 (l'opposto di quella di prima), 
                #che rappresenta l'indice del primo figlio nella struttura del D-Heap.
                self.child[i] = i * self.D + 1
                #Inizializziamo la position map e l'inverse map con -1 per indicare che nessun nodo è attualmente presente nella coda di priorità (D-Heap).
                self.pm[i] = self.im[i] = -1
        
        #Helper che restituisce la size
        def size(self) -> int:
            return self.sz
        
        #Helper che restituisce true se la coda di priorità è vuota, altrimenti false
        
        def isEmpty(self) -> bool:
            return self.sz == 0
        
        #Helper per decrementare il valore associato a un nodo nella coda di priorità, mantenendo la proprietà del D-Heap e l'integrità delle mappe di posizione e inverse map.

        def decrease(self, k1 : int, value : object) -> None:
            if not self.contains(k1):
                raise ValueError("index does not exist in the heap")
            self.valueNotNull(value)
            #Se il valore passato è minore del valore attualmente associato all'indice k1 nella coda di priorità.
            if value < self.values[k1]:
                #Aggoiorniamo il valore associato all'indice k1 nella coda di priorità al nuovo valore più piccolo.
                self.values[k1] = value
                #Facciamo risalire il nodo k1 nella struttura del D-Heap, se necessario, per mantenere la proprietà del D-Heap.
                #La posizione del nodo k1 nella struttura del D-Heap è determinata dalla position map (self.pm[k1]).
                self.swim(self.pm[k1])
        
        #Helper per inserire un nodo nella coda di priorità, mantenendo la proprietà del D-Heap e l'integrità delle mappe di posizione e inverse map.

        def insert(self, ki : int, value : object ) -> None:
            #Se l'indice ki è già presente nella coda di priorità, solleviamo un'eccezione per evitare duplicati.
            if self.contains(ki):
                raise ValueError("index already exists in the heap")
            #Alziamo un eccezzione se il valore è null
            self.valueNotNull(value)
            #Impostiamo la position map per l'indice ki al valore della size attuale della coda di priorità, poiché stiamo per inserire un nuovo nodo alla fine della struttura del D-Heap.
            self.pm[ki] = self.sz
            #Impostiamo l'inverse map per la posizione della size attuale della coda di priorità al valore dell'indice ki, per mantenere l'integrità delle mappe di posizione e inverse map.
            self.im[self.sz] = ki
            #Impostiamo il valore associato all'indice ki nella coda di priorità al valore fornito come argomento.
            self.values[ki] = value
            #Aumentiamo la size della coda di priorità di 1, poiché abbiamo appena inserito un nuovo nodo
            self.sz += 1
            #Prendiamo l'ultimo nodo e se necessario lo facciamo risalire nella struttura del d-heap
            self.swim(self.sz - 1)

        

        #Helper per restituire l'indice più piccolo nella coda di priorità, ovvero l'indice del nodo con la distanza minima da start (se stesso).
        def peekMinKeyIndex(self) -> int:
            if self.isEmpty():
                raise ValueError("Priority queue underflow")
            return self.im[0]
        
        #Helper per restituire il valore più piccolo nella coda di priorità.
        def peekMinValue(self) -> object:
            if self.isEmpty():
                raise ValueError("Priority queue underflow")
            return self.values[self.im[0]]
        

        #Helper per rimuovere e restituire il valore più piccolo nella coda di priorità.
        def poolMinValue(self) -> object:
            if self.isEmpty():
                raise ValueError("Priority queue underflow")
            minValue = self.peekMinValue()
            self.delete(self.peekMinKeyIndex())
            return minValue
        
        #Helper per rimuovere e restituire l'indice più piccolo nella coda di priorità.
        def poolMInKeyIndex(self) -> int:
            if self.isEmpty():
                raise ValueError("Priority queue underflow")
            minkeyIndex = self(self.peekMinKeyIndex)
            self.delete(minkeyIndex)
            return minkeyIndex




        #Helpers per rimuovere un nodo dalla coda di priorità, mantenendo la proprietà del D-Heap e l'integrità delle mappe di posizione e inverse map.


        def delete(self, k1 : int) -> None:
            #Controlliamo se l'indice k1 è presente nella coda di priorità, altrimenti solleviamo un'eccezione.
            if not self.contains(k1):
                raise ValueError("index does not exist in the heap")
            #Impostiamo la variabile i al valore dell'indice k1 nella position map, quindi recuperiamo l'indice del nodo k1 nella struttura del D-Heap.
            i = self.pm[k1]
            #Impostiamo la variabile values al valore associato all'indice k1 nella cosa di priorità
            value = self.values[k1]
            
            #Decrementiamo la size della coda di priorità, poiché stiamo per rimuovere un elemento.
            self.sz -= 1

            #Scambiamo il  nodo da eliminare con l'ultimo nodo nella struttura del D-Heap

            self.swap(i, self.sz)

            #Spostiamo il nodo che è stato spostato al posto del nodo da eliminare verso il basso o verso l'alto nella struttura del D-Heap, a seconda del suo valore, per mantenere la proprietà del D-Heap.
            #Ricorda che con lo swap i ora contiene l'indice del valore che è stato spostato al posto del nodo da eliminare.
            self.sink(i)
            self.swim(i)


            #Eliminiamo il nodo dalla postion map e inverse map, impostando i valori corrispondenti a -1 per indicare che il nodo non è più presente nella coda di priorità.      
            self.pm[k1] = -1
            self.im[self.sz] = -1
            #Impostiamo il valore associato all'indice k1 a None per indicare che non è più presente nella coda di priorità.
            self.values[k1] = None
            
            #restituiamo il valore del nodo eliminato
            
            return value







        #Helper per verificare se un indice è presente nella coda di priorità. Restituisce true se l'indice è presente, altrimenti false.
        def contains(self, ki : int) -> bool:
            self.valueNotNull(ki)
            return self.pm[ki] != -1

        #Funzione per spostare un nodo verso il basso nella struttura del D-Heap, mantenendo la proprietà e l'integrità del D-heap.
        def sink(self, i : int) -> None:
            #Impostiamo j all'indice del figlio con il valore minore
            j = self.minChild(i)
            #Il ciclo continua finché j ha almeno un figlio (quindi che non sia un leaf node)
            while j != -1:
                #Se il nodo i ha un valore minore del nodo j, allora abbiamo trovato la posizione corretta per il nodo i e possiamo uscire dal ciclo.
                if self.less(i,j):
                    break
                #Altrimenti, se il nodo i ha un valore maggiore del nodo j, scambiamo i con j per mantenere la proprietà del D-Heap.
                self.swap(i, j)
                #impostiamo i a j per continuare l'iterazione se il nodo i deve essere spostato ulteriormente verso il basso nella struttura del D-Heap.
                i = j
                #impostiamo j al figlio con il valore minore del nodo i per continuare a verificare se il nodo i deve essere spostato ulteriormente verso il basso nella struttura del D-Heap.
                j = self.minChild(i)


        #Helper per spostare un nodo verso l'alto nella struttura del D-Heap, mantenendo la proprietà e l'integrità del D-heap.
        def swim(self, i : int) -> None:
            #Il ciclo continua finché i è maggiore di 0 (ovvero finché non raggiungiamo la radice del D-Heap) e il nodo i ha un valore minore del suo genitore (self.parent[i]).
            while i>0 and self.less(i, self.parent[i]):
                #Se il nodo i ha un valore minore del suo genitore, scambiamo i con il suo genitore per mantenere la proprietà del D-Heap.
                self.swap(i, self.parent[i])
                #Aggiorniamo i con l'indice del genitore per continuare l'iterazione se il nodo i deve essere spostato ulteriormente verso l'alto nella struttura del D-Heap.
                i = self.parent[i]


        
        #Helper per scambiare due nodi nella struttura del D-Heap, aggiornando le position map e inverse map di conseguenza per garantire integrità.
        def swap(self, i : int, j : int) -> None:
            #Dalla position map passiamo il valore del indice i e j nella inverse map che restituiranno l'indice nel D-heap
            #Aggiorniamo le meppe con i valori invertiti
            self.pm[self.im[j]] = i
            self.pm[self.im[i]] = j
            #Salviamno in una variabile temporanea il valore del nodo i
            tmp = self.im[i]
            #Aggiorniamo i valori dei nodi i e j nella inverse map con i valori invertiti
            self.im[i] = self.im[j]
            #Aggiorniamo il valore del nodo j nella inverse map con il valore salvato nella variabile temporanea
            self.im[j] = tmp 


        #Helper per trovare il figlio con il valore minimo tra i figli di un nodo i nella struttura del D-Heap. Restituisce l'indice del figlio con il valore minimo, o -1 se non ci sono figli.


        def minChild(self, i : int) -> int:
            #impostiamo l'indice del figlio a -1, che indica che non abbiamo ancora trovato un figlio con un valore minimo.
            index = -1
            #recuperiamo l'indice del primo figlio del nodo i dalla struttura del D-Heap utilizzando l'array child, che mappa l'indice di un nodo al suo primo figlio.
            from_ = self.child[i]
            #Selezioniamo il mimimo tra la size e la somma dell'indice del primo figlio e il grado del D-Heap. 
            #Evita di superare i limiti della struttura del D-Heap.
            to = min(self.sz, from_ + self.D)

            #Impostiamo la variabile j al valore dell'indice del primo figlio del nodo i
            j = from_

            #Iteriamo fino a che j è minore di to, ovvero fino a quando non abbiamo esaminato tutti i figli del nodo i nella struttura del D-Heap.

            while j < to:
                #Se l'indice del figlio j è -1 (ovvero siamo fermi al primo figlio) o se il nodo j ha un valore minore del nodo attualmente considerato come minimo (index), allora aggiorniamo index con j.
                if index == -1 or self.less(j, index):
                    index = j
                #Incrementiamo j per esaminare il prossimo figlio del nodo i nella struttura del D-Heap.
                j += 1
            #restituiamo l'indice del figlio con il valore minimo tra i figli di un nodo i nella struttura del D-Heap, o -1 se non ci sono figli.
            return index


        #Helper per controntare due nodi in base al valore.
        #Restituisce true se il nodo i ha un valore minore del nodo j, altrimenti false.
        def less(self, i : int, j : int) -> bool:
            return self.values[self.im[i]] < self.values[self.im[j]]
        
        #Helper per verificare che un valore non sia null, altrimenti solleva un'eccezione
        def valueNotNull(self, value : object) -> None:
            if value is None:
                raise ValueError("value cannot be null")
        

                


p = dijkstraAlgorithmWithDHeap()
p.DijkstrasShortestPathAdjacencyList(5)
p.addEdge(0, 1, 10)
p.addEdge(0, 2, 5)
p.addEdge(1, 2, 2)
p.addEdge(1, 3, 1)
p.addEdge(2, 1, 3)
p.addEdge(2, 3, 9)
p.addEdge(2, 4, 2)
p.addEdge(3, 4, 4)
p.addEdge(4, 3, 6)
print(p.Dijkstra(0, 4))
print(p.reconstructPath(0, 4))


        