from .animal import Animal

class Reptil(Animal):
    totalReptiles = 0
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre="", edad=0, habitat="", genero="", colorEscamas="", largoCola=0):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.largoCola = largoCola
        Reptil.totalReptiles += 1

    @staticmethod
    def crearIguana(nombre, edad, genero):
        Reptil.iguanas += 1
        return Reptil(nombre, edad, "humedad", genero, "verde", 3)

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        Reptil.serpientes += 1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1)

    @staticmethod
    def cantidadReptiles():
        return Reptil.totalReptiles

    def movimiento(self):
        return "reptar"

    def getColorEscamas(self):
        return self.colorEscamas

    def getLargoCola(self):
        return self.largoCola


