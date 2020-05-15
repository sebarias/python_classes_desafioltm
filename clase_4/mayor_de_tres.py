import sys

# primero, si los argumentos no son los necesarios, el programa no sigue.
# Obtener el numero mayor de los numeros ingresados entre tres
#comparamos el primero con el segundo, 
#comparamos el primero con el tercero
#condicion de borde, si son iguales todos o entre dos.
if(len(sys.argv) == 4):
    numeroUno = int(sys.argv[1])
    numeroDos = int(sys.argv[2])
    numeroTres = int(sys.argv[3])
    mayor = 0

    if(numeroUno == numeroDos == numeroTres):
        print("no hay mayores")
    else:
        if(numeroUno > numeroDos):
            mayor = numeroUno
        elif(numeroUno > numeroTres):
            mayor = numeroUno
        elif(numeroDos > numeroTres):
            mayor = numeroDos
        else:
            mayor = numeroTres
        print("el numero mayor de todos es: {}".format(str(mayor)))
else:
    print("sonamos, hay un problema con los argumentos ingresados")



