class Zoologico:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = []

    def agregarZonas(self, z):
        self.zonas.append(z)

    def cantidadTotalAnimales(self):
        a = [x.cantidadAnimales() for x in self.zonas]
        return len(a)

    def getNombre(self):
        return self.nombre
