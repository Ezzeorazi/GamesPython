import random

def adivina_el_numero_computadora(x):

    print("===============")
    print(" ¡Bienvenido al Juego! ")
    print("===============")
    print(f"Selecciona un numero de entre 1 y {x} para que la compu intente adivinar...")

    limite_superior = 1
    limite_inferior = x

    respuesta = ""
    while respuesta != "c":
    
        # Generar prediccion
        if limite_inferior != limite_inferior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior
    
    # Obtener respuesta del usuario
        respuesta = input(f"Mi prediccion es {prediccion}. Si es muy alta, ingresa(A), Si es muy baja, ingresa (B). Si es correcta, ingresa (C): ").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1
    print(f"¡Siii! La compu adivino tu numero correctamente: {prediccion} ")


adivina_el_numero_computadora(10)




        


