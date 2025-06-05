# Calculadora básica
def calculadora():
    print("\nCalculadora básica:")
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    operacion = input("Elige una operación (+, -, *, /): ")

    if operacion == "+":
        print(f"Resultado: {num1 + num2}")
    elif operacion == "-":
        print(f"Resultado: {num1 - num2}")
    elif operacion == "*":
        print(f"Resultado: {num1 * num2}")
    elif operacion == "/":
        if num2 != 0:
            print(f"Resultado: {num1 / num2}")
        else:
            print("Error: División por cero.")
    else:
        print("Operación no válida.")
