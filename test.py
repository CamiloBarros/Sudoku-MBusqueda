from primero_profundidad import main as p_profundidad
from primero_anchura import main as p_anchura
from a_asterisco import main as a_star
from copy import deepcopy
from os import system

if __name__ == '__main__':
    tablero_1 = [  # No es posible la solución
        [0, 0, 9, 0, 7, 0, 0, 0, 5],
        [0, 0, 2, 1, 0, 0, 9, 0, 0],
        [1, 0, 0, 0, 2, 8, 0, 0, 0],
        [0, 7, 0, 0, 0, 5, 0, 0, 1],
        [0, 0, 8, 5, 1, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 6],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 1, 0, 0, 0, 0, 0, 8, 7]
    ]

    tablero_2 = [
        [0, 0, 0, 8, 4, 0, 6, 5, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 5, 2, 0, 1],
        [0, 3, 4, 0, 7, 0, 5, 0, 6],
        [0, 6, 0, 2, 5, 1, 0, 3, 0],
        [5, 0, 9, 0, 6, 0, 7, 2, 0],
        [1, 0, 8, 5, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 5, 2, 0, 8, 6, 0, 0, 0]
    ]

    tablero_3 = [
        [9, 7, 4, 2, 3, 6, 1, 5, 8],
        [6, 3, 8, 5, 9, 1, 7, 4, 2],
        [1, 2, 5, 4, 8, 7, 9, 3, 6],
        [3, 1, 6, 7, 5, 4, 2, 8, 9],
        [7, 4, 2, 9, 1, 8, 5, 6, 3],
        [5, 8, 9, 3, 6, 2, 4, 1, 7],
        [8, 6, 7, 1, 2, 5, 3, 9, 4],
        [2, 5, 3, 6, 4, 9, 8, 7, 1],
        [4, 9, 1, 8, 7, 3, 6, 2, 5]
    ]

    tablero_4 = [  # No es posible la solución
        [0, 9, 0, 3, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 8, 0, 0, 4, 6],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [4, 0, 5, 0, 6, 0, 0, 3, 0],
        [0, 0, 3, 2, 7, 5, 6, 0, 0],
        [0, 6, 0, 0, 1, 0, 9, 0, 4],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [5, 8, 0, 0, 2, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 7, 0, 6, 0]
    ]

    tablero_5 = [
        [0, 3, 9, 0, 0, 0, 1, 2, 0],
        [0, 0, 0, 9, 0, 7, 0, 0, 0],
        [8, 0, 0, 4, 0, 1, 0, 0, 6],
        [0, 4, 2, 0, 0, 0, 7, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 1, 0, 0, 0, 5, 4, 0],
        [5, 0, 0, 1, 0, 9, 0, 0, 3],
        [0, 0, 0, 8, 0, 5, 0, 0, 0],
        [0, 1, 4, 0, 0, 0, 8, 7, 0]
    ]

    tablero_6 = [ # Colocado en trabajo de implementación
        [0, 6, 0, 7, 0, 8, 1, 9, 2],
        [1, 0, 5, 2, 0, 0, 0, 0, 7],
        [0, 2, 0, 0, 0, 6, 0, 0, 0],
        [0, 5, 0, 9, 3, 0, 0, 4, 0],
        [0, 0, 6, 5, 0, 2, 7, 8, 0],
        [9, 7, 0, 0, 0, 0, 3, 2, 5],
        [0, 0, 7, 4, 0, 0, 8, 0, 6],
        [8, 9, 4, 0, 7, 0, 0, 0, 0],
        [0, 1, 0, 3, 0, 0, 0, 7, 4]
    ]

    index = 1
    lista_tableros = [tablero_1, tablero_2, tablero_3, tablero_4, tablero_5, tablero_6]

    for tablero in lista_tableros:
        system('cls')
        print(f'\n\t\t*** TABLERO - {index} ***:\n')

        print('\n\t***BUSQUEDA PRIMERO EN PROFUNDIDAD***\n')
        p_profundidad.resolver(deepcopy(tablero))

        print('\n\t***BUSQUEDA PRIMERO EN ANCHURA***\n')
        p_anchura.resolver(deepcopy(tablero))

        print('\n\t***BUSQUEDA A - ASTERISCO***')
        a_star.resolver(deepcopy(tablero))

        input('\n\t- - - Presione ENTER para continuar - - -')

        index += 1

