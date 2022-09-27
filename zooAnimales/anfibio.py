class Anfibio:
    listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, n, e, hab, g, col, ven):
        super().__init__(n, e, hab, g)
        self.colorPiel = col
        self.venenoso = ven
        Anfibio.listado.append(self)

    def movimiento():
        return "saltar"

    def cantidadAnfibio(self):
        return len(Anfibio.listado)

    def crearRana(
        self,
        n,
        e,
        g,
    ):
        nuevo = Anfibio(n, e, "selva", g, "rojo", True)
        Anfibio.ranas += 1
        return nuevo

    def crearSalamandra(
        self,
        n,
        e,
        g,
    ):
        nuevo = Anfibio(n, e, "selva", g, "negro y amarillo", False)
        Anfibio.salamandras += 1
        return nuevo
