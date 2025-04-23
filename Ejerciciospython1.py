#1) Ingrese datos por consola
from operator import truediv, ifloordiv

nombre = input("ingrese su nombre")
edad = int(input("Ingrese su edad"))

print(f"¡Hola {nombre}, veo que tenés {edad} años.")

comidaFavorita = input("¿Cúal es tu comida favorita?")
colorFavorito = input("¿Y tu color favorito?")

print(f"mmm {comidaFavorita}, que delicia, para acompañarlo con un jugo detox {colorFavorito}")

numero = int(input("Ingresá un número"))
doble = numero * 2
triple = numero * 3

print(f"El doble es {doble}, y el triple {triple}")

#2) Tipos de datos en Python

numerito = 2
flotantito = 2.1
cadenita = "3"
booleanito = True

suma = int(cadenita) + 4
multi = float(input("Ingresa un numero")) * 2
print(multi)

def siConvierte(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False

print(siConvierte("3"))
print(siConvierte("Hola"))

# Operadores en Python

base, altura = map(int, (input(f"Ingresa la base y la altura del rectangulo separados por un espacio").split()))

area = base * altura
print(area)

precio, descuento = map(int, (input(f"Ingresa el precio y el descuento separados por un espacio").split()))

valorFinal = precio - (precio * descuento)

num1, num2 = map(int, (input(f"Ingresa 2 números separados por un espacio").split()))

residuo = num1 % num2

num1, num2 = map(int, (input ("Ingrese 2 numeros separados por espacio:").split()))
formula = (num1 + num2) * (num2 + 1) / num1
print(formula)

num1, num2 = map(int, (input(f"Ingresa 2 numeros separados por un espacio:").split()))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
         else if:
else:
    print(f"{num2} es igual que {num1}")