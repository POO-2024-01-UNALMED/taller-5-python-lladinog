from zooAnimales.animal import Animal

class Anfibio(Animal):
    totalAnfibios = 0
    ranas = 0
    salamandras = 0

    def __init__(self, nombre="", edad=0, habitat="", genero="", colorPiel="", venenoso=False):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPiel = colorPiel
        self.venenoso = venenoso
        Anfibio.totalAnfibios += 1

    @staticmethod
    def crearRana(nombre, edad, genero):
        Anfibio.ranas += 1
        return Anfibio(nombre, edad, "selva", genero, "rojo", True)

    @staticmethod
    def crearSalamandra(nombre, edad, genero):
        Anfibio.salamandras += 1
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)

    @staticmethod
    def cantidadAnfibios():
        return Anfibio.totalAnfibios

    def movimiento(self):
        return "saltar"

    def getColorPiel(self):
        return self.colorPiel

    def isVenenoso(self):
        return self.venenoso

