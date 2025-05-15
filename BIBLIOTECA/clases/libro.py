from datetime import datetime


class Libro:
    def __init__(
        self, codigo, nombre, autor, tipo, fecha_de_publicacion
    ):
        self.codigo = codigo
        self.nombre = nombre
        self.autor = autor
        self.tipo = tipo
        self.fecha_de_publicacion = fecha_de_publicacion
        self.fecha_de_registro = datetime.now()
        self.estado = True

    def mostrar_informacion(self):
        estado_str =  "Disponible" if self.estado else "No disponioble"
        return f"ISBN: {self.codigo}, Nombre: {self.nombre}, Autor: {self.autor}, Tipo: {self.tipo}, Fecha de publicacion: {self.fecha_de_publicacion}, Estado: {estado_str}"

    def actualizar_estado(self):
        self.estado = not(self.estado)

