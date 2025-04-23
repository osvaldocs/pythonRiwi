import math

print("*" * 40)
print("Bienvenido a Libre Mercado")
print("*" * 40)
print()

# Pedimos al usuario que complete los datos requeridos como nombre del producto, precio, etc.
producto = str(input("Ingrese el nombre del producto:"))

precio = int(input("Por favor ingrese el precio unitario:"))

#Condicionamos el valor ingresado a un valor válido con el bucle while
while precio < 1:
    precio = int(input("INGRESE UN PRECIO REAL:"))

cantidad = int(input("Por favor ingrese la cantidad de productos:"))

while cantidad < 1:
    cantidad = int(input("Ingrese una cantidad válida:"))


descuento = int(input("Por favor ingrese el porcentaje de descuento:"))

while descuento < 1 or descuento > 100:
    descuento = int(input("INGRESE UN DESCUENTO RAZONABLE:"))

#Creamos variables y realizamos los cálculos necesarios
valorTotal = precio * cantidad
porDescuento = valorTotal * descuento /100
valorFinal = valorTotal - porDescuento

#Se imprime el nombre, valor del ítem y el porcentaje de descuento
print(f"El precio total por  {cantidad}   {producto} es: {valorFinal}")
