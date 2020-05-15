palabra = input("Ingrese una palabra : ")
largo = len(palabra)

"""
if largo <= 4:
    print("Pequeña")
elif largo <= 10:
    print("Mediana")
else:
    print("Larga")

# se usa if , elif cuando las condiciones 
# que se quieren evaluar son excluyentes,si se cumple una conción
# se entra en una linea de código y no en las siguientes.

"""

# notar la diferencia 
# ingresar la palabra amapola, gato


if largo <= 4:
    print("Pequeña")
if largo <= 10:
    print("Mediana")
else:
    print("Larga")

# se usa if independiente cuando se quiera
#  evaluar más de una condición a la vez,
#  se recorren todas las condiciones.


