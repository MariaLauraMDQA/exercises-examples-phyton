def premio_colores():

    #Premio 
    premio = False
    
    #Pedir al usuario que introduzca 5 colores
    for i in range(5):
        color = input("Introduce el color: ")
        #Si introduce el color azul, la persona ha ganado 
        if color == "azul":
            premio = True

  #Cuando termina de introducir los colores, se muestra si ha ganado o perdido
    if(premio):
        print("¡Ha ganado!")
    else:
        print("Lo siento, ha perdido, ¡inténtelo de nuevo!")

premio_colores()
