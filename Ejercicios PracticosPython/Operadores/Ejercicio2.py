#3. Calcula el residuo de dividir dos números dados por el usuario.
num1, num2 = map(int, (input(f"Ingresa 2 números separados por un espacio").split()))

residuo = num1 % num2
print(f"El residuo de la division de tus numeros es: {residuo}")