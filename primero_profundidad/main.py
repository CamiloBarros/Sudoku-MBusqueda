from os import system
from primero_profundidad.tablero import Tablero
from time import sleep, time
import csv

""" 
    1. Creamos el grafo
    2. Buscamos una celda vacia y retornamos su posicion
    3. Creamos una lista de numeros del 1 - 9
    4. Filtramos esa lista de numeros con los que son invalidos
    5. Creamos ramificaciones o estados con cada uno de los numeros y las añadimos a la pila
"""

def cargarCsv(ruta):
    try:
        archivo = open(ruta)
        tablero = list(csv.reader(archivo))

        for row in range(len(tablero)): 
            tablero[row] = [0 if valor == '' else int(valor) for valor in tablero[row]]
        
        return tablero
    except:
        print('Error, no se pudo cargar el archivo..')
        exit(1)

def busqueda(tablero):
    inicio = tablero
    contador = 0
    numero_nodos = 0

    if inicio.sCompletado():
        return inicio, numero_nodos, contador

    pila = []
    pila.append(inicio)
    numero_nodos += 1

    while pila:
        
        grid = pila.pop()

        if grid.sCompletado():
            return grid, numero_nodos, contador

        aux = [Tablero(estado, grid.nivel+1) for estado in grid.getAdyacentes() ]
        pila.extend(aux)
        
        numero_nodos = numero_nodos + len(aux)
        contador +=1
    
    print('No se ha encontrado solución')
    sleep(5)
    return None, numero_nodos, contador
        

def resolver(tablero = None):

    # tablero = cargarCsv('sudoku_ejemplo.csv') # Cargar tablero, desde el archivo
    tablero_problema = Tablero(tablero) # Instanciar el Tablero
    print('\n- - - TABLERO PROBLEMA - - -')
    tablero_problema.mostrarTablero()

    tiempo_inicio = time()
    tablero_solucion, nNodos, iteraciones = busqueda(tablero_problema) # Resolver el tablero por busqueda, primero en profundidad
    tiempo_final = time()

    if tablero_solucion:
        print('\n- - - TABLERO SOLUCIÓN - - -')
        tablero_solucion.mostrarTablero()
        print(f'Tiempo: {tiempo_final - tiempo_inicio} ')
        print('Numeros de nodos: ', nNodos)
        print('Numero de iteraciones: ', iteraciones)
        print('Nivel del tablero solución: ', tablero_solucion.nivel)