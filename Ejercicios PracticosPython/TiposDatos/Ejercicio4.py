#1. Calcula el área de un rectángulo a partir de base y altura ingresadas por el usuario.
base, altura = map(int, (input(f"Ingresa la base y la altura del rectangulo separados por un espacio").split()))

area = base * altura
print(f" el area del rectangulo es: {area}")