
from zooAnimales.mamifero import Mamifero
from zooAnimales.anfibio import Anfibio
from zooAnimales.ave import Ave
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil
from gestion.zona import Zona

class Animal:
    totalAnimales = 0
    listado=[]

    def __init__(self, nombre="", edad=0, habitat="", genero="",zona=None):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.zona = zona
        Animal.totalAnimales += 1
        Animal.listado.append(self)

    @staticmethod
    def getTotalAnimales():
        return Animal.totalAnimales

    @staticmethod
    def getZona():
        return Animal.zona

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getHabitat(self):
        return self.habitat

    def getGenero(self):
        return self.genero

    def movimiento(self):
        return "desplazarse"

    @staticmethod
    def totalPorTipo():
        return (f"Mamiferos : {Mamifero.caballos + Mamifero.leones}\n"
                f"Aves : {Ave.aguilas + Ave.halcones}\n"
                f"Reptiles : {Reptil.iguanas + Reptil.serpientes}\n"
                f"Peces : {Pez.salmones + Pez.bacalaos}\n"
                f"Anfibios : {Anfibio.ranas + Anfibio.salamandras}")

    def __str__(self):
        info = (f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, "
                f"habito en {self.habitat} y mi genero es {self.genero}")
        if Animal.zona:
            info += (f", la zona en la que me ubico es {self.zona.getNombre()}, "
                     f"en el {self.zona.getZoo().getNombre()}")
        return info

