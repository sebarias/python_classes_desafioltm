import sys

#primer le pedimos al usuario cuantos argumentos va a ingresar, lo hare con sys.argv
#luego permitimos que ingrese los n argumentos, y los sumamos para al final obtener el promedio.

argumentos = int(sys.argv[1])

i = 0
suma = 0

while i < argumentos:
    i += 1
    suma += int(input("ingrese argumento {}:".format(i)))

print("el promedio de los argumentos que ingresaste es: {}".format(suma / argumentos))
