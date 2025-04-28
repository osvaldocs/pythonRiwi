#2. Aprobado o reprobado

calificacion = int(input("Ingresa tu calificacion:"))

while calificacion not in range(0, 101):
    calificacion = int(input("Ingrese una calificacion correcta:"))

if calificacion < 60:
        print("Reprobaste")
else:
        print("Aprobaste")

