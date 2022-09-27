from zooAnimales.animal import Animal


class Reptil(Animal):
    listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, n, e, hab, g, col, lar):
        super().__init__(n, e, hab, g)
        self.colorEscamas = col
        self.largoCola = lar
        Reptil.listado.append(self)

    def movimiento():
        return "reptar"

    def cantidadReptiles(self):
        return len(Reptil.listado)

    def crearIguana(
        self,
        n,
        e,
        g,
    ):
        nuevo = Reptil(n, e, "humedal", g, "verde", 3)
        Reptil.iguanas += 1
        return nuevo

    def crearSerpiente(
        self,
        n,
        e,
        g,
    ):
        nuevo = Reptil(n, e, "jungla", g, "blanco", 1)
        Reptil.serpientes += 1
        return nuevo
