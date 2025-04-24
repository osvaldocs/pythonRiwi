#2. Dado un precio y un porcentaje de descuento, muestra el valor final a pagar.
precio, descuento = map(int, (input(f"Ingresa el precio y el descuento separados por un espacio").split()))

valorFinal = precio - ((precio * descuento)/100)
print(f"El precio final del producto es: {valorFinal}")