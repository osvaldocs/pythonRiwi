#3. Escribe un programa que compare dos cadenas de texto e indique si son iguales o distintas.
str1, str2 = (input("Ingresa 2 palabras separadas por un espacio").split())

if str1 == str2:
    print("Las cadenas son iguales")
else:
    print("Las cadenas son diferentes")