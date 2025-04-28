import random

# 5. Adivina el numero

numRandom = random.randint(1, 10)

intento = 3

while intento >= 1:
    numero = int(input("Ingrese un numero del 1 al 10"))
    if numero < numRandom:
        print("El numero es mayor")
    elif numero > numRandom:
        print("El numero es menor")
    else:
        print(f"Adivinaste el numero correcto es: {numRandom}")
        break

    intento -= 1
    if intento == 0:
        print(f"Se acabaron los intentos, el numero era: {numRandom}")


