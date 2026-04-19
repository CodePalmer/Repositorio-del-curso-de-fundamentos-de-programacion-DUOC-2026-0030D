Numero_Secreto = 42
intentos = 0
respuesta_usuario = 0
while respuesta_usuario != Numero_Secreto:

    respuesta_usuario = int(input("adivina el numero: "))
    intentos = intentos + 1

    if respuesta_usuario < Numero_Secreto:
        print("TU NUMERO SECRETO ES MAS ALTO")
    elif respuesta_usuario > Numero_Secreto:
        print("Tu numero secreto es mas bajo")

print("Felicidades ganaste!")
print(f"Numero de veces intentados: {intentos}")
print("fin del programa")
                