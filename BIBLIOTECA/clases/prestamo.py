from datetime import datetime

class Prestamo:
    def __init__(self, usuario, lista_de_libros):
        self.usuario = usuario
        self.lista_de_libros = lista_de_libros
        self.fecha = datetime.now()

    def registrar_prestamo(self):
        self.usuario.registrar_prestamo(self)
        return f"Prestamo registrado: {self.mostrar_informacion()}"

    def mostrar_informacion(self):
        libros = ", ".join({libro.nombre for libro in self.lista_de_libros})
        return f"Usuario: {self.usuario.nombre}, Libros: {libros}"