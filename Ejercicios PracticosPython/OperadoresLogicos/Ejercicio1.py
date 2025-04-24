#2. Solicita si una persona tiene experiencia laboral y título universitario. Usa operadores lógicos para decidir si puede aplicar a una oferta de trabajo.
experiencia = input("Cuentas con experiencia laboral? ingresa 'si' en caso afirmativo, o 'no' en caso negativo")
titulo = input("¿Cuentas con titulo Universitario? ingresa 'si' en caso afirmativo, o 'no' en caso negativo")

if experiencia or titulo == "si":
    print("Podes empezar un periodo de prueba")
elif experiencia  and titulo == "si":
    print("Estas contratado")