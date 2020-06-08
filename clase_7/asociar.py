import velocidad as vel
from functools import reduce


velocidad = [4, 4, 7, 7, 8, 9, 10, 10, 10,
11, 11, 12, 12, 12, 12, 13, 13,
13, 13, 14, 14, 14, 14, 15, 15,
15, 16, 16, 17, 17, 17, 18, 18,
18, 18, 19, 19, 19, 20, 20, 20,
20, 20, 22, 23, 24, 24, 24, 24, 25]
distancia = [2, 10, 4, 22, 16, 10, 18, 26, 34,
17, 28, 14, 20, 24, 28, 26, 34, 34,
46, 26, 36, 60, 80, 20, 26, 54, 32,
40, 32, 40, 50, 42, 56, 76, 84, 36,
46, 68, 32, 48, 52, 56, 64, 66, 54,
70, 92, 93, 120, 85]

velocidad_promedio = vel.promedio(velocidad)
distancia_promedio = vel.promedio(distancia)
velocidad_bajo_promedio = 0
velocidad_distancia_bajo_promedio = 0
velocidad_sobre_promedio = 0
velocidad_sobre_distancia_bajo_promedio = 0

for vel, dis in zip(velocidad, distancia):
    if vel < velocidad_promedio:
        velocidad_bajo_promedio += 1
    if vel < velocidad_promedio and dis < distancia_promedio:
        velocidad_distancia_bajo_promedio += 1
    if vel >= velocidad_promedio:
        velocidad_sobre_promedio += 1
    if vel >= velocidad_promedio and dis < distancia_promedio:
        velocidad_sobre_distancia_bajo_promedio += 1

#vel_bajo_promedio = reduce( lambda x, y: x + (1 if y < velocidad_promedio else 0), velocidad)
#vel_bajo_promedio = reduce( lambda x, y: x + y, zip(velocidad, distancia))

print("velocidad promedio = {}".format(velocidad_promedio))
print("Velocidad bajo el promedio = {}".format(velocidad_bajo_promedio))
print("Velocidad bajo el promedio y distancia sobre el promedio = {}".format(velocidad_distancia_bajo_promedio))
print("Velocidad sobre el promedio = {}".format(velocidad_sobre_promedio))
print("Velocidad sobre el promedio y distancia bajo el promedio = {}".format(velocidad_sobre_distancia_bajo_promedio))


