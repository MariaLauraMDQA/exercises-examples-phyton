def mostrar_planetas():
    # Lista de planetas
    planetas = ("Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno")

    # Pedimos al usuario que introduzca un número del 1 al 8
    planeta_num = int(input("Introduce un número del 1 al 8 para mostrar un planeta: "))

    # Comprobamos que esté dentro del rango
    if 1 <= planeta_num <= 8:
        # Guardamos el planeta elegido
        planeta_elegido = planetas[planeta_num - 1]
        print("El planeta correspondiente es:", planeta_elegido)
    else:
        print("Número fuera de rango. Debe ser entre 1 y 8.")

# Llamamos a la función
mostrar_planetas()


