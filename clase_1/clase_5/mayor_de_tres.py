import sys

numeroUno = int(sys.argv[1])
numeroDos = int(sys.argv[2])
numeroTres = int(sys.argv[3])
mayor = 0

if(numeroUno > numeroDos):
    mayor = numeroUno
elif(numeroUno > numeroTres):
    mayor = numeroUno
elif(numeroDos > numeroTres):
    mayor = numeroDos
else:
    mayor = numeroTres

print("el número mayor de todos es: {}".format(mayor))

