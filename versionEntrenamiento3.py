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


def consultarProductos(buscarProducto):
    for producto in listaProductos:
        if producto["nombre"].lower() == buscarProducto.lower():
            print(producto)
            return producto
            break
    else:
        print("No existe el producto")



def actualizarPrecios(productoNombre, nuevoPrecio):
    producto = consultarProductos()


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

def calcularValorInventario():
    pass

opcion = input("Bienvenido a LibreMercado. Por favor ingrese una opción para continuar:\n"
               "1: Para añadir un producto\n"
               "2: Para buscar un producto\n"
               "3: Para eliminar un producto\n"
               "4: Para actualirzar el precio de un producto\n"
               "5: Para calcular el valor del inventario\n")
match opcion:
    case "1":
        while True:
            nombreProducto = input("Ingrese el nombre del producto: ")
            if re.fullmatch(r"[A-Za-záéíóúÁÉÍÓÚñÑ]+", nombreProducto):
                break
            else:
                print("El nombre solo puede contener letras y espacios, sin números ni símbolos.")

        while True:
            try:
                precioProducto = float(input("Ingrese el precio del producto"))
                break
            except ValueError:
                print("Ingrese valor válido")

        while True:
            try:
                cantidadProducto = int(input("Ingrese la cantidad del producto"))
                print("\nProducto agregado de forma correcta")
                break

            except ValueError:
                print("Ingrese un numero entero")

        añadirProducto(nombreProducto, precioProducto, cantidadProducto)

    case "2":
        buscarProducto = input("Ingrese el nombre del producto que quieres buscar: ")

        consultarProductos(buscarProducto)