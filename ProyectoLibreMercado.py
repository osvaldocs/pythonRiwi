import math

print("Bienvenido a Libre Mercado")
print()


print("Ingrese el nombre del producto:")
producto = str(input())

print("Por favor ingrese el precio unitario:")
precio = int(input())
while precio < 1:
    print("INGRESE UN PRECIO REAL:")
    precio = int(input())

print("Por favor ingrese la cantidad de productos:")
cantidad = int(input())

while cantidad < 1:
    print("Ingrese una cantidad válida:")
    cantidad = int(input())

print("Por favor ingrese el porcentaje de descuento:")
descuento = int(input())

while descuento < 1 or descuento > 100:
    print("INGRESE UN DESCUENTO RAZONABLE:")
    descuento = int(input())


valorTotal = precio * cantidad
porDescuento = valorTotal * descuento /100
valorFinal = valorTotal - porDescuento

print(f"El precio total por  {cantidad}   {producto} es: {valorFinal}")

