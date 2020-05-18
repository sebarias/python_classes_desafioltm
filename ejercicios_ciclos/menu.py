import math
import random
import sys

opcion = ""

while opcion != "saqueme":
    print("1. la raiz cuadrada de 9")
    print("2. dime quien es el mas pulento")
    print("3. dame un numero aleatorio")
    print("si quiere salir escriba, saqueme")

    opcion = input()

    if opcion == "1":
        print(str(math.sqrt(9)))
    elif opcion == "2":
        print(" vo mismo ")
    elif opcion == "3":
        print(str(random.randint(1, 100)))
    else:
        print("ingrese una opcion valida")
print("saliendo... Chau")