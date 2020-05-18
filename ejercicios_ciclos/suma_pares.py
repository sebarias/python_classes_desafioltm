#recorremos de 1 a 100 y con la funcion mod sumamos los pares

i = 0
sumaPares = 0

while i < 100:
    i += 1
    if i % 2 == 0:
        sumaPares += i

print("la suma de los primeros 100 pares es {}".format(sumaPares))