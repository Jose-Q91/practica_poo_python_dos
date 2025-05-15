
from clases.inventario import Inventario
from clases.prestamo import Prestamo
from clases.usuario import Usuario
from clases.libro import Libro


def registrar_libro():
    codigo = input("Ingres el codigo del libro: ")
    nombre = input("Ingrese el nombre del libro: ")
    autor = input("Ingres el autor del libro: ")
    tipo = input("Ingrese le tipo de libro: ")
    fecha_de_publicacion = input("Ingrese la fecha de publicacio: ")

    libro = Libro(codigo, nombre, autor, tipo, fecha_de_publicacion)
    return libro


def registrar_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    direccion = input("Ingrese la direccion del usuario: ")
    telefono = input("Ingrese el telefono del usuario: ")

    usuario = Usuario(nombre, direccion, telefono)
    return usuario


def registrar_prestamo(usuarios, inventario):
    nombre_usuario = input("Nombre del usuario: ")
    usuario = next((u for u in usuarios if u.nombre == nombre_usuario), None)
    if not usuario:
        print("Usuario no registrado")
        return
    libros = []

    while True:
        codigo_libro = input(
            "Ingrese el codigo del libro (Deje vacio para finalizar): "
        )
        if not codigo_libro:
            break
        libro = next(
            (lib for lib in inventario.lista_de_libros if lib.codigo == codigo_libro and lib.estado),
            None,
        )
        if libro:
            libro.actualizar_estado()
            libros.append(libro)
        else:
            print("Libro no disponible")
    if libros:
        prestamo = Prestamo(usuario, libros)
        prestamo.registrar_prestamo()
        print("El prestamose ha realizado con exito")
    else:
        print("No se han registrado prestamos")

def registrar_devolucion(usuarios):
    nombre_usuario = input("Nombre del usuario: ")
    usuario = next((u for u in usuarios if u.nombre == nombre_usuario), None)
    if not usuario:
        print("Usuario no registrado")
        return
    usuario.devolucion_prestamo()

def mostrar_menu():
    print("\n---Menu de gestion de la biblioteca buenos caminos ---")
    print("1. Registrar Libro")
    print("2. Registrar Usuario")
    print("3. Registrar Prestamo")
    print("4. Registrar Devolucion")
    print("5. Mostrar estado del libro")
    print("6. Salir")


def main():
    usuarios = []
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            libro = registrar_libro()
            if libro:
                inventario.agregar_libro(libro)
                print("Libro registrado exitosamente")
        elif opcion == "2":
            usuario = registrar_usuario()
            if usuario:
                usuarios.append(usuario)
                print("usuario Registrado exitosamente")
        elif opcion == "3":
            registrar_prestamo(usuarios, inventario)
        elif opcion == "4":
            registrar_devolucion(usuarios)
        elif opcion == "5":
            for lib in inventario.lista_de_libros:
                print(lib.mostrar_informacion())
        elif opcion == "6":
             break
        else:
            print("Opcion no velida intente nuevamente")



if __name__ == "__main__":
    main()


        
        