class Zona:
    def __init__(self, nombre, zoo) -> None:
        self.nombre = nombre
        self.zoo = zoo
        self.animales = []

    def agregarAnimales(self, a):
        self.animales.append(a)

    def cantidadAnimales(self):
        return len(self.animales)
