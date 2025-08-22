### Juego ###

while True:
    import random
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Elegido = random.choice(my_list)
    print ("elige tu dificultad: facil, medio o dificil")
    dificultad = input ().lower()
    if dificultad == "facil" or "fasil" or "f":
            intentos = 3
    elif dificultad == "medio" or "m" or "med":
            intentos = 2
    elif dificultad == "dificil" or "d" or "dif":
            intentos = 1
    for i in range (intentos):
                    intento = int(input("elige un numero del 1 al 10:"))
                    if intento == Elegido:
                        print ("¡Ganaste!")
                        break

                    else:
                        print ("uff buen intento te quedan", intentos - 1 - i, "intentos")
                    if intento < Elegido:
                        print ("El numero es mas alto")
                    else:
                        print ("El numero es mas bajo")
    else:
                    print ("Perdiste, el numero correcto era", Elegido)

    while True:
                Jugar_denuevo = input("¿Te gustaria volver a jugar?\nSi o nel?:")
                if Jugar_denuevo.lower() == "si":
                    break
                elif Jugar_denuevo.lower() == "nel":
                    print ("Gracias por jugar Culero 😎")
                    break
                else:
                    print ("Joa pon ""si"" o ""no"" pendejo")
    if Jugar_denuevo.lower() != "si":
                break