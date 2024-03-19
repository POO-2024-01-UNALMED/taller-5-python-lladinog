from .animal import Animal

class Pez(Animal):
    totalPeces = 0
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre="", edad=0, habitat="", genero="", colorEscamas="", cantidadAletas=0):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.cantidadAletas = cantidadAletas
        Pez.totalPeces += 1

    @staticmethod
    def crearBacalao(nombre, edad, genero):
        Pez.bacalaos += 1
        return Pez(nombre, edad, "oceano", genero, "gris", 6)

    @staticmethod
    def crearSalmon(nombre, edad, genero):
        Pez.salmones += 1
        return Pez(nombre, edad, "oceano", genero, "rojo", 6)

    @staticmethod
    def cantidadPeces():
        return Pez.totalPeces

    def movimiento(self):
        return "nadar"

    def getColorEscamas(self):
        return self.colorEscamas

    def getCantidadAletas(self):
        return self.cantidadAletas

