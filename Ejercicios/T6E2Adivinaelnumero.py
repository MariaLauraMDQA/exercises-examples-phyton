# Adivinar el número
def mensaje(numero):
    Mensaje = ""

    if numero == "4":
        Mensaje = "¡Has ganado! El número es correcto."
    elif numero == "1":
        Mensaje = "Lo siento, perdiste. El número correcto es el 4."
    elif numero == "2":
        Mensaje = "Lo siento, perdiste. El número correcto es el 4."
    elif numero == "3":
        Mensaje = "Lo siento, perdiste. El número correcto es el 4."
    elif numero == "5":
        Mensaje = "Lo siento, perdiste. El número correcto es el 4."
    elif numero == "6":
        Mensaje = "Lo siento, perdiste. El número correcto es el 4."
    elif numero == "7":
        Mensaje = "Lo siento, perdiste. El número correcto es el 4."
    elif numero == "8":
        Mensaje = "Lo siento, perdiste. El número correcto es el 4."
    elif numero == "9":
        Mensaje = "Lo siento, perdiste. El número correcto es el 4."
    elif numero == "10":
        Mensaje ="Lo siento, perdiste. El número correcto es el 4."
    else:
        Mensaje = "Elige un número del 1 al 10"
    
    return Mensaje


# Pedimo al usuario que introduzca el número
numero = input("Introduce un numero: ")
print(numero)

#Ponemos el número 
resultado = mensaje(numero)
print(resultado)   