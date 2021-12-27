# Clase  para definir lois vertices de las graficas
class Vertice:
    def __init__(self, i): # Metodo iniciador
        # Atributos
        self.id = i
        self.vecinos = [] # es una lista
        self.padre = None
        self.visitado = False
        self.distancia = float("inf")
    
    # v = vecino del vertice
    # p = peso de la arista 
    
    def agregarVecino(self, v, p):
        if v not in self.vecinos:# si v no se encuentra en la lista vecinos
            self.vecinos.append([v, p])# Agrego los valores de v y p a una lista llamada vecinos
  

# Clase  para definir los vertices de las graficas
class Grafica:
    def __init__(self): # Método iniciador
        self.vertices = {} # Creo un diccionario, donde almacenará los vertices
        
    def agregarVertice(self, id): # le pas0o como parametro un id que será el valor del vertice
        if id not in self.vertices:
            self.vertices[id] = Vertice(id)
    
    # a y b son los 2 vertices que conforman 1 arista
    # p es el peso de la arista
    
    def agregarArista(self, a, b, p):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregarVecino(b,p)
            self.vertices[b].agregarVecino(a,p)
            
    def imprimir(self):
        for v in self.vertices:
            print('La distancia del vertice ' + str(v) + ' es: ' + str(self.vertices[v].distancia) + ' llegando desde ' + str(self.vertices[v].padre))
            
    def camino(self, a, b):
        camino = []# declaro una lista para el camino
        actual = b
        while actual != None:
            camino.insert(0, actual)
            actual = self.vertices[actual].padre
        return [camino, self.vertices[b].distancia]    

# m = menor valor
# Funcion para encontrar al nodo con menor distancia       
    def minimo(self, lista): # la lista sera el conjunto de nodos no visitados
        if len(lista) > 0:# la lista tiene elementos?
            m = self.vertices[lista[0]].distancia
            v = lista[0]
            for e in lista:
                if m > self.vertices[e].distancia:
                    m = self.vertices[e].distancia
                    v = e
            
            return v
    
    # a es nodo donde iniciaremos el recorrido
    def dijkstra(self, a):
        if a in self.vertices: # El vertice a se encuentra en los vertices
            self.vertices[a].distancia = 0 # El valor a se inicia en 0
            actual = a # El valor mas actual es a
            aunNoVisitados = []# Creo una lista de vertices no visitados
            
            for v in self.vertices:
                if v != a: # Mientras no encontremos al vertice a
                    self.vertices[v].distancia = float("inf")# Se le asigna un valor inicial de distancia con valor infinito
                self.vertices[v].padre = None # Declaro el nodo padre con un valor vacio
                aunNoVisitados.append(v)# Agrego a los demás nodos a la lista de no visitados
            while len(aunNoVisitados) > 0:# Mientras la lista aunNoVisitados tenga elementos en el
                for vecino in self.vertices[actual].vecinos: # recorremos a todos los nodos vecinos del nodo actual
                    if self.vertices[vecino[0]].visitado == False: # si el vertice vecino no esta visitado
                        # Operaciones
                        if self.vertices[actual].distancia + vecino[1] < self.vertices[vecino[0]].distancia:
                            self.vertices[vecino[0]].distancia = self.vertices[actual].distancia + vecino[1]
                            self.vertices[vecino[0]].padre = actual
                
                self.vertices[actual].visitado = True # Se marca como visitado el nodo actual  
                aunNoVisitados.remove(actual)# en la lista se quita el valor que este en ese momento
                
                actual = self.minimo(aunNoVisitados)              
        else:
            return False
              
class main:
    g = Grafica()# asigno una variable a la funcion para poder agregar cada vertice y cada arista
    # Agrego los vertices
    g.agregarVertice(1)
    g.agregarVertice(2)
    g.agregarVertice(3)
    g.agregarVertice(4)
    g.agregarVertice(5)
    g.agregarVertice(6)
    
    # Agrego las aristas
    g.agregarArista(1, 6, 14) # (vertice 1, vertice 2, el valor de la arista)
    g.agregarArista(1, 2, 7)
    g.agregarArista(1, 3, 9)
    g.agregarArista(2, 3, 10)
    g.agregarArista(2, 4, 15)
    g.agregarArista(3, 4, 11)
    g.agregarArista(3, 6, 2)
    g.agregarArista(4, 5, 6)
    g.agregarArista(5, 6, 9)
    
    print('\n\n La ruta mas rapida por dijkstra junto con su costo es: ')
    g.dijkstra(1)
    print(g.camino(1, 6))
    
    print('\n Los valores finales de la grafica  son los siguientes: ')
    g.imprimir()
    
            
                        
        
        
    
    