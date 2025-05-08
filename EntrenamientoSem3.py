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

añadirProducto("Manzana", 3000, 40)

def ingresarDatosProducto():

    while True:
        nombreProducto = input("Ingrese el nombre del producto: ").strip()
        if re.fullmatch(r"[A-Za-záéíóúÁÉÍÓÚñÑ]+", nombreProducto):
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

def actualizarPrecios(producto, NuevoPrecio):
    busca = consultarProductos(buscarProducto)
    #if busca

def pedirNuevoPrecio():
    while True:
        try:
            nuevoPrecio = float(input("Ingrese el precio nuevo del producto: "))
            return nuevoPrecio
            break
        except ValueError:
            print("Ingrese un precio válido")

def eliminarProducto():
    pass


opcion = input("Bienvenido a LibreMercado. Por favor ingrese una opción para continuar:\n"
               "1: Para añadir un producto\n"
               "2: Para buscar un producto\n"
               "3: Para eliminar un producto\n"
               "4: Para actualirzar el precio de un producto\n"
               "5: Para calcular el valor del inventario\n")

match opcion:
    case "1":
        ingresarDatosProducto()

    case "2":
        buscarProductos = pedirNombreProducto()
        consultarProductos(buscarProductos)

    case "3":
        pass

    case "4":
        pass
