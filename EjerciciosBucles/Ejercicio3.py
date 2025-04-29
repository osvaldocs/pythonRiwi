#3. Tabla de multiplicar

numero = int(input("Ingresa un numero positivo:"))

while numero < 0:
  numero = int(input("Ingresa un numero positivo:"))  

for i in range(1, 11):
    print(f"{numero} * i = (numero * i)")
