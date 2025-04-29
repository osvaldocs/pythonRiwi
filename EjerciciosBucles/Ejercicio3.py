import random
#5. Adivina el numero

numRandom = random.randint(1, 4)

numero = int(input("Ingrese un numero del 1 al 10"))

intento = 0

if numero < numRandom:
