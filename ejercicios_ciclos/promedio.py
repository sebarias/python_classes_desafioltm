#desafio que permita sumar todos los numeros de uno a n donde n es un valor ingresado por el usario
#el resultado de la suma se divide por n y se muestra al usuario

import sys

numbersSize = int(sys.argv[1])
i = 0
suma = 0
div = 0

while i < numbersSize:
    i += 1
    suma += i
div = suma / numbersSize
print("el total es {}".format(round(div,2))) #format me muestra solo la parte entera, why ?

