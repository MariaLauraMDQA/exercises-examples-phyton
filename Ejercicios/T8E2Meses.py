def mostrar_meses():
    # Lista de meses
    meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

    # Pedimos al usuario que introduzca un número del 1 al 12
    mes_num = int(input("Introduce un número del 1 al 12 para mostrar un mes: "))

    # Comprobamos que esté dentro del rango
    if 1 <= mes_num <= 12:
        # Guardamos el mes elegido
        mes_elegido = meses[mes_num - 1]
        print("El mes correspondiente es:", mes_elegido)
        #Si el mes es junio, indicamos en el mensaje el mejor mes, sino mostramos el mes.
        if mes_elegido == "Junio":
            mensaje = mes_elegido + " EL MEJOR MES"
            print(mes_elegido, "EL MEJOR MES")
        else:
            mensaje = "El mes correspondiente es: " + mes_num
    else:
        print("Número fuera de rango. Debe ser entre 1 y 8.")

# Llamamos a la función
mostrar_meses()