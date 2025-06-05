from calculadora import calculadora
from adivinanza import juego_adivinanza

def main():
    print("¡Hola, bienvenidos al laboratorio de Python!")

    # Paso 1: Sintaxis Básica y Operaciones Simples
    entero = 10
    decimal = 3.14
    cadena = "Python"

    suma = entero + decimal
    resta = decimal - entero
    multiplicacion = entero * 2
    division = decimal / 2

    print("Suma:", suma)
    print("Resta:", resta)
    print("Multiplicación:", multiplicacion)
    print("División:", division)

    nombre = input("¿Cuál es tu nombre? ")
    print("Hola, " + nombre + "! Bienvenido al laboratorio.")

    # Paso 2: Condicionales y Bucles
    numero = int(input("Introduce un número: "))
    if numero % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")

    numeros = [1, 2, 3, 4, 5]
    for n in numeros:
        print(f"El cuadrado de {n} es {n**2}")

    entrada = ""
    while entrada != "0":
        entrada = input("Introduce un número (0 para salir): ")
        print(f"Has introducido: {entrada}")

    # Paso 3: Listas y Diccionarios
    estudiantes = ["Juan", "Ana", "Luis"]
    print("\nLista de estudiantes:")
    for estudiante in estudiantes:
        print(f"Estudiante: {estudiante}")

    contactos = {
        "Juan": "juan@example.com",
        "Ana": "ana@example.com"
    }
    print("\nInformación de contacto:")
    for nombre_contacto, correo in contactos.items():
        print(f"Nombre: {nombre_contacto}, Correo: {correo}")

    nuevo_estudiante = input("\nIntroduce el nombre de un nuevo estudiante: ")
    estudiantes.append(nuevo_estudiante)
    print("Lista actualizada de estudiantes:", estudiantes)

    nuevo_contacto = input("\nIntroduce un nombre para actualizar/agregar contacto: ")
    nuevo_correo = input("Introduce el correo de este contacto: ")
    contactos[nuevo_contacto] = nuevo_correo
    print("Contactos actualizados:", contactos)

    # Paso 4: Ejecutar calculadora y juego de adivinanza
    calculadora()
    juego_adivinanza()


if __name__ == "__main__":
    main()