# Clasificación según rangos
"""
Es normal estar en situaciones donde nos pidan clasificar algún elemento según un rango.
Por ejemplo, supongamos que tenemos una palabra y queremos clasificarla en corta, mediana o larga:
4 letras o menos será corta.
5 a 10 letras será mediana.
Más de 10 letras será larga.
"""

"""
palabra = input('Ingresa una palabra : ')
n = len(palabra)

if n <=4:
    print('la palabra {} es corta'.format(palabra))
elif n > 10:
    print('la palabra {} es larga'.format(palabra))
else:
    print('la palabra {} es mediana'.format(palabra))
"""

"""
palabra = input("Ingrese una palabra : ")
largo = len(palabra)

if largo <= 4:
    print("Pequeña")
elif largo <= 10:
    print("Mediana")
else:
    print("Larga")
"""

#Ejercicio
"""
Modifica el código anterior para poder 
distinguir palabras muy largas,
cuando tengan 15 o más caracteres.
"""

palabra = input('Ingresa una palabra : ')
n = len(palabra)
print(n)

if n <=4:
    print('la palabra {} es corta'.format(palabra))
elif n <=10:
    print('la palabra {} es mediana'.format(palabra))
elif n < 15:
    print('la palabra {} es larga'.format(palabra))
else:
    print('la palabra {} es muy larga'.format(palabra))

