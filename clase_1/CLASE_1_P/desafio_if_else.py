"""
Crear un programa donde el usuario 
deba ingresar dos números. 
El programa debe imprimir el mayor de
ambos números.
"""

valor1 = int(input("Ingrese valor 1 = "))

valor2 = int(input("Ingrese valor 2 = "))

if valor1 >= valor2:
    print("valor1 {} es mayor".format(valor1))
else:
    print("valor2 {} es mayor".format(valor2))

"""
Desafíos propuestos

El usuario ingresa debe ingresar un password en la plataforma.
Si el password tiene menos de 6 letras, se debe mostrar un aviso.

"""

password=input("ingrese un password de 6 letras : ")

if len(password) < 6:
    print("El password ingresado tiene menos de 6 letras.")
    
"""
El usuario debe ingresar un password. Si el password es 12345, se debe informar que el password es
incorrecto.
"""

password=input("ingrese un password  : ")

if password==str(12345):
    print("El password ingresado es incorrecto.")

numero=int(input('ingrese un número mayor a 100'))

if numero <=100:
    print('El número no es válido')

