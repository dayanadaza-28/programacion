# Juego de adivinanza
import random

def juego_adivinanza():
    print("\nJuego de Adivinanza:")
    numero_aleatorio = random.randint(1, 100)
    adivinanza = -1
    while adivinanza != numero_aleatorio:
        adivinanza = int(input("Adivina el número (entre 1 y 100): "))
        if adivinanza < numero_aleatorio:
            print("Mayor...")
        elif adivinanza > numero_aleatorio:
            print("Menor...")
        else:
            print("¡Correcto! Adivinaste el número.")