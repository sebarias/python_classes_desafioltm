import sys
import random

ancho = int(sys.argv[1])

#validamos que el valor ingresado sea mayor que el ancho minimo osea 10.
if(ancho < 10):
    ancho = 10

for i in range(10):
    #se genera un numero random para dibujar a copito en un luegar aleatorio
    random_number = random.randint(i, ancho) 
    print(" " * random_number + "*" + "\n")
    #creamos otro ciclo para dibujar a la lluvia
    for j in range(10):
        random_number_2 = random.randint(j, ancho)
        print(" " * random_number_2 + "/" + "\n")
