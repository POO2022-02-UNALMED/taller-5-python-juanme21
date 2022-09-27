from zooAnimales.ave import Ave
from zooAnimales.mamifero import Mamifero
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil
from zooAnimales.anfibio import Anfibio


class Animal:
    totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero) -> None:
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genera = genero

    def movimiento():
        return "desplazarse"

    def totalPorTipo(self):
        str = (
            "Mamiferos: "
            + Mamifero.cantidadMamiferos()
            + "\n"
            + "Aves: "
            + Ave.cantidadAves()
            + "\n"
            + "Reptiles: "
            + Reptil.cantidadReptiles()
            + "\n"
            + "Peces: "
            + Pez.cantidadPeces()
            + "\n"
            + "Anfibios: "
            + Anfibio.cantidadAnfibios()
        )
        return str

    def toString(self) -> str:
        stri = "Mi nombre es {}, tengo una edad de {}, habito en {} y mi genero es {}".format(
            self.nombre, self.edad, self.habitat, self.genero
        )
        return stri

    def getNombre(self):
        return self.nombre
