#1. Pide dos números e indica cuál es mayor o si son iguales.
num1, num2 = map(int, (input(f"Ingresa 2 numeros separados por un espacio:").split()))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif  num1 < num2:
    print(f"{num2} es mayor que {num1}")

else:
    print(f"{num2} es igual que {num1}")