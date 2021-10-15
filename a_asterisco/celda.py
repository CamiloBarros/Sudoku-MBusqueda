class Celda:
    def __init__(self, posibles, g, h, padre, posicion):
        self.posibles = posibles

        self.g = g
        self.h = h
        self.f = g + h

        self.posicion = posicion      
        self.padre = padre 

    def __gt__(self, celda):
        return self.f > celda.f
