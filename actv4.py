# Imprimir un mensaje
print("¡Hola, bienvenidos al laboratorio de Python!")

# Declarar variables
entero = 10
decimal = 3.14
cadena = "Python"

# Operaciones matemáticas simples
suma = entero + decimal
resta= decimal - entero
multiplicacion= entero * 2
divicion = decimal / 2

# Concatenar cadenas
nombre = input("¿Cuál es tu nombre? ")
print("Hola, " + nombre + "! Bienvenido al laboratorio.")

# Condicionales: Determinar si un número es par o impar
numero = int(input("Introduce un número: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# Bucle for: Iterar sobre una lista e imprimir los cuadrados de los números
numeros = [1, 2, 3, 4, 5]
for n in numeros:
    print(f"El cuadrado de {n} es {n**2}")

# Bucle while: Solicitar repetidamente la entrada hasta que el usuario introduzca '0'
entrada = ""
while entrada != "0":
    entrada = input("Introduce un número (0 para salir): ")
    print(f"Has introducido: {entrada}")

# Lista de nombres de estudiantes
estudiantes = ["Juan", "Ana", "Luis"]
for estudiante in estudiantes:
    print(f"Estudiante: {estudiante}")

# Diccionario de información de contacto
contactos = {
    "Juan": "juan@example.com",
    "Ana": "ana@example.com"
}
for clave, valor in contactos.items():
    print(f"Nombre: {clave}, Correo: {valor}")

# Script para agregar elementos a una lista o actualizar un diccionario
nuevo_estudiante = input("Introduce el nombre de un nuevo estudiante: ")
estudiantes.append(nuevo_estudiante)
print("Lista actualizada de estudiantes:", estudiantes)

nuevo_contacto = input("Introduce un nombre para actualizar/agregar: ")
nuevo_correo = input("Introduce el correo de este contacto: ")
contactos[nuevo_contacto] = nuevo_correo
print("Contactos actualizados:", contactos)



