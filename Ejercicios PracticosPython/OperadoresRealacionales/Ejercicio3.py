#1. Pide al usuario su edad y si tiene licencia de conducción. Solo si ambas condiciones se cumplen, imprime que puede conducir.
edad = int(input("Ingrese su edad"))
tieneLicencia = False
licencia = input("Si tiene licencia de conducir ingrese 'si' En caso contrario ingrese 'no'")

if licencia == "si":
    tieneLicencia = True


if tieneLicencia & edad > 16:
    print("Perfecto puedes conducir")
else:
    print("No cumplis los requisitos para manejar")
