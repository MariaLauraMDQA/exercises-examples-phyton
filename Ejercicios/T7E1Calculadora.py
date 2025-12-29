def calcular_nota_media():
    # Notas que va a introducir el usuario
    numero_notas = int(input("Introduce el número de notas: "))
    
    # Suma de notas 
    suma = 0

    # Pedimos al usuario que introduzca cada nota
    for i in range(numero_notas):
        # Cada vez que se introduzca, guardamos la nota
        nota = float(input("Introduce la nota: "))
        # Se suma para conocer el total
        suma += nota

    # Calculamos la media
    nota_media = suma / numero_notas
    print("La nota media es:", nota_media)

calcular_nota_media()