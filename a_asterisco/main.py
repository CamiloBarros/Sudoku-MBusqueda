from a_asterisco.tablero import Tablero
from time import sleep, time
from os import system

""" A*: 
Cola de prioridad = [( valor_f, index, celda(objeto) )]
1. Obtener la celda vaciá más cercanada (Estado inicial)
2. Añadir la celda a la cola de prioridad
3. Mientras que la cola de prioridad esté llena
    3.1 Obtener la celda con menor valor de F
    3.2 Añadir la celda a la lista cerrada, para no visitarla dos veces
    3.3 Comprobamos si el tablero está lleno y es valido
    3.4 Obtenemos números posibles para la celda actual
    3.5 Para cada numero posible harémos,
        3.5.1 Crearemos un tablero 
        3.5.2 Evaluamos la función 
        3.5.3 Obtenemos la celda(objeto) con menor valor de F
        3.5.4 Agregamos la celda(objeto) a la cola de prioridad
 """

def busqueda(tablero):
    estado_inicial = tablero
    count = 0
    numero_nodos = 0
    solucion = tuple()

    if estado_inicial.sCompletado():
        return estado_inicial, count, numero_nodos

    # Obtenemos celda vacia con menor costo de F
    celda_actual = estado_inicial.lista_celdas[0]
    # Cola = [( valor_f, index, celda(objeto) )]
    cola = []
    cola.append((celda_actual.f, count, celda_actual))
    numero_nodos += 1

    lista_cerrada = set()

    while cola:
        count += 1
        # COLA = [CELDA1(6), CELDA(5), CELDA3(7), CELDA4(5)]

        cola = sorted(cola, key=lambda x: x[0]) # Ordenamos la cola en funcion de F, para asegurar la filosofia de cola de prioridad, siempre saldrá el de menor valor en su funcion de costo.

        if not solucion:
            (f, c, celda) = cola.pop(0)
        else:
            if cola:
                if solucion[1] > cola[0][0]: # Cola = (funcion_costo, contador_iteraciones, objeto_celda)
                    (f, c, celda) = cola.pop(0)
                else: 
                    return solucion[0], count, numero_nodos
            else:
                return solucion[0], count, numero_nodos
                
        lista_cerrada.add(celda)

        candidatos = [Tablero(estado, celda.padre.nivel+1, celda.g) for estado in celda.padre.getAdyacentes()]
        
        for candidato in sorted(candidatos, key=lambda x: x.lista_celdas[0].f if x.lista_celdas else False, reverse=True):
            # Comprobamos si el tablero está completo
            if candidato.sCompletado():
                solucion = (candidato, celda.f)
                
                if cola:
                    
                    if cola[0][0] > celda.f:  # Cola = (funcion_costo, contador_iteraciones, objeto_celda)
                        return solucion[0], count, numero_nodos
                else:
                    return solucion[0], count, numero_nodos
                # return candidato, count, numero_nodos
                continue

            numero_nodos += 1
            
            cell = candidato.lista_celdas[0]

            cola.insert(0, (cell.f, count, cell))

    return None, count, numero_nodos

def resolver(tablero = None):

    tablero_problema = Tablero(tablero)
    print('\n- - - TABLERO PROBLEMA - - -')
    tablero_problema.mostrarTablero()
    
    tiempo_inicial = time()
    solucion, iteraciones, nNodos = busqueda(tablero_problema)
    tiempo_final = time()
    
    if solucion:
        print('\n- - - TABLERO SOLUCIÓN - - -')
        solucion.mostrarTablero()
        print('Tiempo: ', tiempo_final - tiempo_inicial)
        print('Numero de nodos: ', nNodos)
        print('Numero de iteraciones: ', iteraciones)
        print('Nivel del tablero solución: ', solucion.nivel)
    else:
        print('No se encontró una solución')