import random
import time

print("Vamos a jugar a los dados. Pulsa enter para continuar")
input()

#Global Variables
puntos_banca = 0
puntos_jugador = 0

#Se define el juego que se ejecuta en bucle
def juego():#Salen dos numeros aleatorios entre el 1 y el 6

    print("Preparate!!")
    time.sleep(1)
    print("La banca va a jugar...")
    time.sleep(2)
    dado_1 = random.randint(1,6)
    print ("Sale un " + str(dado_1))
    time.sleep(2)
    print("Es tu turno. Pulsa enter cuando estes listo")
    input()

    dado_2 = random.randint(1, 6)
    print("Sale un...")
    time.sleep(2)
    print(str(dado_2) + "!!")
    time.sleep(1)
   
    #Se usa global para referirse a la funcion que esta fuera de def()
    #ya que los puntos cambian en cada ronda
    global puntos_banca
    global puntos_jugador

    #Comprobacion de quien gana
    if dado_1 > dado_2:
        print("Lo siento, has perdido...")
        puntos_banca = puntos_banca + 1
        time.sleep(1)
        print("Vas " + str(puntos_jugador) + " a " + str(puntos_banca))
                
    elif dado_1 < dado_2:
        print("Has ganado!!")
        puntos_jugador = puntos_jugador + 1
        time.sleep(1)
        print("Vas " + str(puntos_jugador) + " a " + str(puntos_banca))
    
    elif dado_1 == dado_2:
        print("Es un empate!!")
        time.sleep(1)
        print("Vas " + str(puntos_jugador) + " a " + str(puntos_banca))
           

#Mientras se pulse y antes de finalizar, el juego seguirá ejecutandose
replay = "Y"
while replay == "y" or replay == "Y":

    juego()
    print("Quieres jugar otra vez? (Y/N)")
    replay = input()

#Si replay != "y" se muestra el resultado final y se decide quien es el ganador
else:
    print("El resultado final es de " + str(puntos_jugador) + " a " + str(puntos_banca))

    if puntos_jugador > puntos_banca:
        time.sleep(1)
        print("Eres el ganador!!")

    elif puntos_jugador < puntos_banca:
        time.sleep(1)
        print("Otra vez será...")

    elif puntos_jugador == puntos_banca:
        time.sleep(1)
        print("Empate")

##FIN##