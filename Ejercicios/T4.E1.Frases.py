# Pedir al usuario que continue una frase
frase = input("Continua la frase: ")

#Unimos dos cadenas
frase1 = "Hola, me llamo: " + frase

#Obtenemos la longitud de la frase
longitud = len(frase1)

#Poner la cadena en mayusculas
frase1mayusculas = frase1.upper()

#Poner la cadena en minusculas
frase1minisculas = frase1.lower()

print(frase1)
print("Longitud", longitud)
print(frase1mayusculas)
print(frase1minisculas)