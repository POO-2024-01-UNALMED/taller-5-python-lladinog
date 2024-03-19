from gestion.zona import Zona

class Zoologico:
    def __init__(self, nombre=None, ubicacion=None):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = []

    def agregarZonas(self, zona):
        self.zonas.append(zona)

    def getZona(self):
        return self.zonas

    def cantidadTotalAnimales(self):
        totalAnimales = 0
        for zona in self.zonas:
            totalAnimales += zona.cantidadAnimales()
        return totalAnimales

    def getNombre(self):
        return self.nombre

    def getUbicacion(self):
        return self.ubicacion

