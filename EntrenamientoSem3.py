
# -*- coding: utf-8 -*-

import re

#EntrenamientoSem3

listaProductos = []


def añadirProducto(nombre, precio, cantidad):

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    listaProductos.append(producto)

añadirProducto("Manzana", 1600, 40)
añadirProducto("Pera",1500,44)

def ingresarDatosProducto():

    while True:
        nombreProducto = input("Ingrese el nombre del producto: ").strip()
        if re.fullmatch(r"[A-Za-záéíóúÁÉÍÓÚñÑ ]+", nombreProducto):
            break
        else:
            print("El nombre solo puede contener letras y espacios, sin números ni símbolos.")

    while True:
        try:
            precioProducto = float(input("Ingrese el precio del producto"))
            if precioProducto < 0:
                print("El precio no puede ser menor a 0")
                continue
            break
        except ValueError:
            print("Ingrese valor válido")

    while True:
        try:
            cantidadProducto = int(input("Ingrese la cantidad del producto"))
            if cantidadProducto >= 0:
                print("\nProducto agregado de forma correcta")
                break
            else:
                print("La cantidad no puede ser menor a 0")

        except ValueError:
            print("Ingrese un numero entero")

    añadirProducto(nombreProducto, precioProducto, cantidadProducto)

def pedirNombreProducto():
    while True:
        nombreProductoBuscar = input("Ingresa el nombre del producto a buscar: ")
        if re.fullmatch(r"[A-Za-záéíóúÁÉÍÓÚñÑ ]+", nombreProductoBuscar):
            return nombreProductoBuscar
        else:
            print("El nombre solo puede contener letras y espacios, sin números ni símbolos.")


def consultarProductos(buscarProducto):
    for producto in listaProductos:
        if producto["nombre"].lower() == buscarProducto.lower():
            print(producto)
            return producto

    else:
        print("No existe el producto")
        return None




def calcularValorInventario():
    pass

def actualizarPrecios(nombre, NuevoPrecio):
    producto = consultarProductos(nombre)
    if producto:
        producto["precio"] = NuevoPrecio
        print(f"Precio actualizado correctamente. el nuevo precio de {producto['nombre']} es {producto['precio']} ")
    else:
        print("No existe el producto")


def pedirNuevoPrecio():
    while True:
        try:
            nuevoPrecio = float(input("Ingrese el precio nuevo del producto: "))
            return nuevoPrecio
            break
        except ValueError:
            print("Ingrese un precio válido")

def eliminarProducto(nombreProductoEliminar):
    producto = consultarProductos(nombreProductoEliminar)
    if producto:
         listaProductos.remove(producto)
         print("Producto eliminado correctamente")
    else:
        print("No existe el producto")

def menu():
    while True:
        opcion = input("Bienvenido a LibreMercado. Por favor ingrese una opción para continuar:\n"
                       "1: Para añadir un producto\n"
                       "2: Para buscar un producto\n"
                       "3: Para eliminar un producto\n"
                       "4: Para actualizar el precio de un producto\n"
                       "5: Para calcular el valor del inventario\n"
                       "6: Para salir\n")

        match opcion:
            case "1":
                ingresarDatosProducto()
            case "2":
                buscarProductos = pedirNombreProducto()
                consultarProductos(buscarProductos)
            case "3":
                nombreEliminar = pedirNombreProducto()
                eliminarProducto(nombreEliminar)
            case "4":
                nombre = pedirNombreProducto()
                nuevoPrecio = pedirNuevoPrecio()
                actualizarPrecios(nombre, nuevoPrecio)
            case "5":
                pass
            case "6":
                print("Saliendo del programa.")
                break
            case _:
                print("Opcion inválida. intente nuevamente")
