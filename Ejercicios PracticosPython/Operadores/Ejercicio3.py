#4. Escribe una fórmula que use al menos tres operadores diferentes y muestre el resultado.
num1, num2 = map(int, (input ("Ingrese 2 numeros separados por un espacio:").split()))
formula = (num1 + num2) * (num2 + 1) / num1
print(formula)