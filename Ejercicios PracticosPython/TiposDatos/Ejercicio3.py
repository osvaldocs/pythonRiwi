#4. Escribe una función que reciba un string y devuelva True si puede convertirse a número y False si no.
def siConvierte(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False

print(siConvierte("3"))
print(siConvierte("Hola"))