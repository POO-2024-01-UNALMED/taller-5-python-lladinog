from zooAnimales.animal import Animal

class Mamifero(Animal):
    totalMamiferos = 0
    caballos = 0
    leones = 0

    def __init__(self, nombre="", edad=0, habitat="", genero="", pelaje=False, patas=0):
        super().__init__(nombre, edad, habitat, genero)
        self.pelaje = pelaje
        self.patas = patas
        Mamifero.totalMamiferos += 1

    @staticmethod
    def crearCaballo(nombre, edad, genero):
        Mamifero.caballos += 1
        return Mamifero(nombre, edad, "pradera", genero, True, 4)

    @staticmethod
    def crearLeon(nombre, edad, genero):
        Mamifero.leones += 1
        return Mamifero(nombre, edad, "selva", genero, True, 4)

    @staticmethod
    def cantidadMamiferos():
        return Mamifero.totalMamiferos

    def movimiento(self):
        return "desplazarse"

    def isPelaje(self):
        return self.pelaje

    def getPatas(self):
        return self.patas