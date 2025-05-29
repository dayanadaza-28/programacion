def crearResultado(Y, Z, X):
    numeros = [Y, Z, X]

    if Y == Z == X:
        print("Los tres números son iguales.")
    elif Y == Z or Y == X or Z == X:
        print("Dos de los números son iguales.")
       
        numeros.sort()
        print("Número menor:", numeros[0])
        print("Número medio:", numeros[1])
        print("Número mayor:", numeros[2])
    else:
       
        numeros.sort()
        print("Número menor:", numeros[0])
        print("Número medio:", numeros[1])
        print("Número mayor:", numeros[2])


try:
    num1 = input("Ingrese el primer número: ")
    num2 = input("Ingrese el segundo número: ")
    num3 = input("Ingrese el tercer número: ")

    crearResultado(num1, num2, num3)
except ValueError:
    print("Por favor, ingrese solo valores numéricos.")