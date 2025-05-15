class Inventario:
    def __init__(self):
        self.lista_de_libros = []

    def agregar_libro(self, libro):
        self.lista_de_libros.append(libro)
    
    def actualizar_inventario(self, libro, estado):
        for lib in self. lista_de_libros:
            if lib.codigo == libro.codigo:
                libro.actualizar_estado(estado)
    