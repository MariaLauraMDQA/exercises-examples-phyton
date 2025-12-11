# Elegir tu color favorito
def Mensaje(color):
    mensaje = ""

    if color == "Rojo":
        Mensaje = "El rojo es el color de la pasión y la energía. ¡Hoy será un día lleno de acción y emoción! No temas a los desafíos, saldrás victorioso."
    elif color == "Verde":
        Mensaje = "El verde representa la esperanza y el crecimiento. Algo nuevo y positivo está por florecer en tu vida. Confía en los pequeños cambios que te acercan a tus metas."
    elif color == "Azul":
        Mensaje = "El azul simboliza la calma y la serenidad. Hoy estarás rodeado de tranquilidad y equilibrio. Aprovecha este momento para reflexionar y renovar tu energía."
    elif color == "Amarillo":
        Mensaje = "El amarillo es el color de la felicidad y el optimismo. ¡Prepárate para un día lleno de alegría y buenas noticias! Alguien cercano te sorprenderá de forma positiva."
    elif color == "Morado":
        Mensaje = "El morado evoca la sabiduría y la creatividad. Hoy te sentirás inspirado y lleno de ideas. Es el momento ideal para djar volar tu imaginación y tomar grandes decisiones."
    else:
        Mensaje = "Elige otro color: Rojo, verde, azul, amarillo o morado"
    return Mensaje

def Color():
    color = input("Elige tu color favorito (Rojo, Verde, Azul, Amarillo, Morado): ")

# Pedimo al usuario que introduzca el color
color = input("Introduce tu color favorito: ")
print(color)

#Ponemos el color 
Mensaje = Mensaje(color)
print(Mensaje)   

