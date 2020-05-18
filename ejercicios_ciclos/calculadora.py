#generar un menu iterando sobre input con las opciones de sumar, restar, multiplicar y dividir
#agregar las opciones de argumento 1 y argumento 2 para realizar las operaciones
#la opcion de salida sera la palabra "exit"

opcion = ""

while opcion != "salir":
    print("Que operacion quiere realizar ?")
    print("1. Sumar dos numeros")
    print("2. Restar dos numeros")
    print("3. Multiplicar dos numeros")
    print("4. Dividir dos numeros")
    opcion = input()
    if opcion != "salir":
        numero1 = int(input("ingrese primer numero: "))
        numero2 = int(input("ingrese segundo numero: "))
        if opcion == "1":
            print("la suma es: {}".format(numero1 + numero2))
        elif opcion == "2":
            print("la resta es {}".format(numero1 - numero2))
        elif opcion == "3":
            print("la multiplicacion es {}".format(numero1 * numero2))
        elif opcion == "4":
            print("la divivsion es {}".format(numero1 / numero2))
        else:
            opcion = "salir"

print("Chau")