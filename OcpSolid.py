# Sin OCP Solid
def saludar(nombre, idioma):
    if idioma == "es":
        return f"Hola, {nombre}"
    elif idioma == "en":
        return f"Hello, {nombre}"
    else:
        return f"Idioma no soportado"

print(saludar("Elbio", "es"))
print(saludar("Elbio", "en"))

# Con OCP Solid

class Saludo:
    def saludar(self, nombre):
        pass

class SaludoEspañol(Saludo):
    def saludar(self, nombre):
        return f"Hola, {nombre}"

class SaludoIngles(Saludo):
    def saludar(self, nombre):
        return f"Hello, {nombre}"

# Uso:
saludos = [SaludoEspañol(), SaludoIngles()]

for saludo in saludos:
    print(saludo.saludar("Elbio"))
