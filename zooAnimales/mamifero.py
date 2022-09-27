class Mamifero:
    listado = []
    caballos = 0
    leones = 0

    def __init__(self, n, e, hab, g, pel, pat):
        super.__init__(n, e, hab, g)
        self.pelaje = pel
        self.pat = pat
        Mamifero.listado.append(self)

    def cantidadMamiferos(self):
        return len(Mamifero.listado)

    def crearCaballo(
        self,
        n,
        e,
        g,
    ):
        nuevo = Mamifero(n, e, "pradera", g, True, 4)
        Mamifero.caballos += 1
        return nuevo

    def crearLeon(
        self,
        n,
        e,
        g,
    ):
        nuevo = Mamifero(n, e, "selva", g, True, 4)
        Mamifero.leones += 1
        return nuevo