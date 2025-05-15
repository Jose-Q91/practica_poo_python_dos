class Usuario:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.historial_de_prestamos = []

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Direccion: {self.direccion}, Telefono: {self.telefono}"

    def registrar_prestamo(self, prestamo):
        self.historial_de_prestamos.append(prestamo)

    def devolucion_prestamo(self):
        for prestamo in self.historial_de_prestamos:
            for libro in prestamo.lista_de_libros:
                libro.actualizar_estado()
        self.historial_de_prestamos.clear()
        print("Registro de devolucion ha sido realizado exitosamente")

