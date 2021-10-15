from primero_profundidad import main as p_profundidad
from primero_anchura import main as p_anchura
from a_asterisco import main as a_star
from copy import deepcopy
from time import sleep
import csv
 
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

if __name__ == '__main__': 
    tablero = cargarCsv('sudoku_ejemplo.csv')
    # tablero = cargarCsv('sudoku_hard.csv')

    print('\n\t***BUSQUEDA PRIMERO EN PROFUNDIDAD***\n')
    p_profundidad.resolver(deepcopy(tablero))
    # # sleep(1)

    print('\n\t***BUSQUEDA PRIMERO EN ANCHURA***\n')
    p_anchura.resolver(deepcopy(tablero))
    # sleep(1)

    print('\n\t***BUSQUEDA A - ASTERISCO***')
    a_star.resolver(deepcopy(tablero))