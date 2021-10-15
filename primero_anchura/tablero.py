from time import sleep
from copy import deepcopy

class Tablero:
    def __init__(self, tablero, nivel=0):
        self.tablero = tablero
        self.tamaño = len(tablero)
        self.nivel = nivel

        self.grafo = {}
        self.crearGrafo()

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



                lista_final = set(lista_columna) | set(lista_fila) | set(lista_region)
                lista_final = lista_final - set([0])

                adyacentes.extend(lista_final)
                # adyacente = [  ]
                # lista_final = [1, 2, 3, 4]
                # adyacente = [ [1, 2, 3, 4] ]
                # adyacente = [1, 2, 3, 4]
                if aux:
                    print(self.tablero[i][j])
                    print(adyacentes)
                    sleep(5)

                self.grafo[(i, j)] = adyacentes

    def setValor(self, valor, posicion):
        (x, y) = posicion
        self.tablero[x][y] = valor

    def getFila(self, tablero, posicion):
        (x, y) = posicion
        l_elementos = []
        for columna in range(self.tamaño):
            if columna != y:
                l_elementos.append(tablero[x][columna])
        return l_elementos

    def getColumna(self, tablero, posicion):
        (x, y) = posicion
        l_elementos = []
        for fila in range(self.tamaño):
            if fila != x:
                l_elementos.append(tablero[fila][y])
        return l_elementos

    def getRegion(self, tablero, posicion):
        (x, y) = posicion
        x = int((x//3)*3) # Posición inicial X, de la region
        y = int((y//3)*3) # Posición inicial Y, de la region
        l_elementos = []

        for fila in range(0, 3):
            for columna in range(0, 3):
                if (fila + x) == posicion[0] and (columna + y) == posicion[1]:
                    pass
                else:
                    l_elementos.append(tablero[fila + x][columna + y])
        return l_elementos

    def getCeldaVacia(self, tablero):
        for i in range(self.tamaño):
            for j in range(self.tamaño):
                if tablero[i][j] == 0:
                    return (i, j)
        return -1, -1

    def getAdyacentes(self):
        fila, columna = self.getCeldaVacia(self.tablero) # Posicion de la celda vacia más proxima en la fila
        posibles = range(1, self.tamaño+1) # Serie de numeros posibles
        posibles = list(set(posibles) - set(self.grafo[(fila, columna)])) # Filtramos los posibles con los que no se pueden

        for valor in posibles: 
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
        sleep(time)

    def mostrarGrafo(self):
        if self.grafo:
            for key, value in self.grafo.items():
                print(f'{key} : {value} ')
        else:
            print('No existe un grafo para el tablero')