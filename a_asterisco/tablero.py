from a_asterisco.celda import Celda
from copy import deepcopy
from functools import cmp_to_key

""" 
    Tablero((0, 0)) = 5

    Tablero((3, 2)) = 5

 """


class Tablero:
    def __init__(self, tablero, nivel=0, costo=0):
        self.tablero = tablero
        self.tamaño = len(tablero)
        self. nivel = nivel
        # self.costo = costo + 1

        self.lista_celdas = [] # Todas las celdas vacias que se encuentran en el tablero, ordenadas de menor a mayor en función de F(x)

        self.grafo = {}
        self.matriz_costo = [] 
        self.matriz_heuristica = []

        self.crearGrafo()
        self.crearMCosto(costo)
        self.crearFHeuristica()

        self.inicializarCeldas()

    def inicializarCeldas(self):
        for i in range(self.tamaño):
            for j in range(self.tamaño):
        
                valor = self.tablero[i][j]
                 
                if valor == 0:
                    posibles = range(1, self.tamaño+1) # Serie de numeros posibles
                    posibles = list(set(posibles) - set(self.grafo[(i, j)])) # Filtramos los posibles con los que no se pueden
                    g = self.matriz_costo[i][j]
                    # g = self.costo
                    h = self.matriz_heuristica[i][j]
                    self.lista_celdas.append(Celda(posibles, g, h, self, (i, j)))
        
        self.lista_celdas = sorted(self.lista_celdas, key=cmp_to_key(self.key))

    def crearGrafo(self, aux=False):
        lista_columna = []
        lista_fila = []
        lista_region = []

        for i in range(self.tamaño):
            for j in range(self.tamaño):
                adyacentes = []
                lista_columna = self.getColumna(self.tablero, (i, j))
                lista_fila = self.getFila(self.tablero, (i, j))
                lista_region = self.getRegion(self.tablero, (i, j))

                lista_final = set(lista_columna) | set(
                    lista_fila) | set(lista_region)
                lista_final = lista_final - set([0])

                adyacentes.extend(lista_final)

                if aux:
                    print(self.tablero[i][j])
                    print(adyacentes)

                self.grafo[(i, j)] = adyacentes

    def crearMCosto(self, costo = 0):
        for i in range(self.tamaño):
            self.matriz_costo.append([])  # Agregar fila
            for j in range(self.tamaño):
                if self.tablero[i][j] == 0:
                    # Serie de numeros posibles
                    posibles = range(1, self.tamaño+1)
                    # Filtramos los posibles con los que no se pueden
                    posibles = list(set(posibles) - set(self.grafo[(i, j)]))
                    self.matriz_costo[i].append(len(posibles)+costo)
                else:
                    self.matriz_costo[i].append(0)
        # self.getMatrizCosto()

    def crearFHeuristica(self):
        # Recorremos el tablero, y vamos calculando el valor de la función heurística de cada celda vacía que se vaya encontrando en el recorrido.
        for i in range(self.tamaño):
            # Añadimos una lista que representa una fila de la matriz
            self.matriz_heuristica.append([])
            for j in range(self.tamaño):

                if self.tablero[i][j] == 0:
                    # Obtenemos celdas vacias que se encuentran en fila, columna y region, para la posicion i, j

                    # Celdas_fila = [(0, 0), (0, 2), ....]
                    celdas_fila = self.getFila(self.tablero, (i, j), True)
                    celdas_columna = self.getColumna(
                        self.tablero, (i, j), True)
                    celdas_region = self.getRegion(self.tablero, (i, j), True)

                    # Como es posible que se repitan celdas, filtramos con operacion union de conjuntos
                    lista_celdas_vacias = list(set(celdas_fila) | set(
                        celdas_columna) | set(celdas_region))

                    # Teniendo la lista de celdas vacias, sin que se repitan celdas, ahora obtenemos el tamaño de esta, que representará el valor de la función heuristica para la celda en la posicion i, j
                    fHeuristica = len(lista_celdas_vacias)

                    # Agregamos el valor de fHeuristica a la matriz heuristica, en la posicion i, j
                    self.matriz_heuristica[i].append(fHeuristica)
                else:
                    self.matriz_heuristica[i].append(0)

        # Hay que tener en cuenta, que en la matriz heuristica donde se encuentren 0, es porque no es una celda vacía
        # self.getMatrizHeuristica()

    def getListaCelda(self):
        return self.lista_celdas

    def getFila(self, tablero, posicion, invertir=False):
        (x, y) = posicion
        l_elementos = []
        for columna in range(self.tamaño):
            if columna != y:
                if invertir:
                    if tablero[x][columna] == 0:
                        l_elementos.append((x, columna))
                else:
                    l_elementos.append(tablero[x][columna])
        return l_elementos

    def getColumna(self, tablero, posicion, invertir=False):
        (x, y) = posicion
        l_elementos = []
        for fila in range(self.tamaño):
            if fila != x:
                if invertir:
                    if tablero[fila][y] == 0:
                        l_elementos.append((fila, y))
                else:
                    l_elementos.append(tablero[fila][y])
        return l_elementos

    def getRegion(self, tablero, posicion, invertir=False):
        (x, y) = posicion
        x = int((x//3)*3) # Posición inicial X, de la region
        y = int((y//3)*3) # Posición inicial Y, de la region
        l_elementos = []

        for fila in range(0, 3):
            for columna in range(0, 3):
                if (fila + x) == posicion[0] and (columna + y) == posicion[1]:
                    pass
                else:
                    if invertir:
                        if tablero[fila + x][columna + y] == 0:
                            l_elementos.append((fila+x, columna+y))
                    else:
                        l_elementos.append(tablero[fila + x][columna + y])
        return l_elementos

    def celdaPop(self):
        return self.lista_celdas.pop(0)


    def getCeldaVacia(self, tablero): 
        for i in range(self.tamaño):
            for j in range(self.tamaño):
                if tablero[i][j] == 0:
                    return (i, j)
        return -1, -1

    def getAdyacentes(self): # Modificar, devolver objetos adyacentes *NO VALORES*
        celda = self.celdaPop()
        #fila, columna = self.getCeldaVacia(self.tablero) # Posicion de la celda vacia más proxima en la fila
        fila, columna = celda.posicion
       
        # posibles = range(1, self.tamaño+1) # Serie de numeros posibles
        # posibles = list(set(posibles) - set(self.grafo[(fila, columna)])) # Filtramos los posibles con los que no se pueden

        for valor in celda.posibles: 
            newTablero = deepcopy(self.tablero)
            newTablero[fila][columna] = valor
            yield newTablero

    def sCompletado(self):
        suma_total = sum(range(1, 10))

        for fila in self.tablero: # Comprobamos que la suma en las filas esté correcta
            if sum(fila) != suma_total:
                return False
        
        for fila in range(9): # Comprobamos que la suma de las columnas estén correctas
            total_columna = 0
            for columna in range(9):
                total_columna += self.tablero[columna][fila]
            
            if total_columna != suma_total:
                return False

        for fila in range(0, 9, 3): # Comprobamos que la suma de las regiones esté correcta
            for columna in range(0, 9, 3):
                total_region = 0

                for fila_region in range(0, 3):
                    for columna_region in range(0, 3):
                        total_region += self.tablero[fila + fila_region][columna + columna_region]
                
                if total_region != suma_total:
                    return False

        return True

    def mostrarTablero(self, time=0):
        for fila in range(self.tamaño):
            if fila % 3 == 0 and fila != 0:
                print("- - - - - - - - - - - - - ")

            for columna in range(self.tamaño):
                if columna % 3 == 0 and columna != 0:
                    print(" | ", end="")

                if columna == 8:
                    print(self.tablero[fila][columna])
                else:
                    print(str(self.tablero[fila][columna]) + " ", end="")


    def mostrarGrafo(self):
        if self.grafo:
            for key, value in self.grafo.items():
                print(f'{key} : {value} ')
        else:
            print('No existe un grafo para el tablero')

    def key(self, celda_a, celda_b):
        if celda_a.f > celda_b.f:
            return 1
        else: 
            if celda_a.f < celda_b.f:
                return -1
            else: # Si es igual
                if celda_a.g > celda_b.g:
                    return 1
                else: 
                    if celda_a.g < celda_b.g:
                        return -1
                    else:
                        return 0

        """ 
            A = 5
            B = 5

            G(x) = Costo
            H(x) = Heuristica
            F(x) = Función de costo
         """

    def mostrarCeldas(self): # Muestra la lista de celdas
        for celda in self.lista_celdas:
            print(f'[({celda.f}, {celda.g})]', end='')