from zooAnimales.animal import Animal
class Zona:
    
    def __init__(self, nombre="", zoo=None):
        self.nombre = nombre
        self.zoo = zoo
        self.animales =[]

    def agregarAnimales(self, animal):
        self.animales.append(animal)        

    def cantidadAnimales(self):
        return len(self.animales)

    def getNombre(self):
        return self.nombre

    def getZoo(self):
        return self.zoo

