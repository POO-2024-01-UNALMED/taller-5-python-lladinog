from zooAnimales.animal import Animal

class Ave(Animal):
    totalAves = 0
    aguilas = 0
    halcones = 0

    def __init__(self, nombre="", edad=0, habitat="", genero="", colorPlumas=""):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPlumas = colorPlumas
        Ave.totalAves += 1

    @staticmethod
    def crearHalcon(nombre, edad, genero):
        Ave.halcones += 1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso")

    @staticmethod
    def crearAguila(nombre, edad, genero):
        Ave.aguilas += 1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")

    @staticmethod
    def cantidadAves():
        return Ave.totalAves

    def movimiento(self):
        return "volar"

    def getColorPlumas(self):
        return self.colorPlumas

