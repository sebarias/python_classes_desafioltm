import velocidad as vel
from functools import reduce



auto1 = ['Mazda RX4', 21.0, 6, False, 4]
auto2 = ['Merc 240D', 24.4, 4, True, 2]
auto3 = ['Merc 280', 19.2, 6, True, 4]
auto4 = ['Valiant', 18.1, 6, True, 1]
auto5 = ['Merc 450SL', 17.3, 8, False, 3]
auto6 = ['Toyota Corolla', 33.9, 4, True, 1]

autos = []
autos.append(auto1)
autos.append(auto2)
autos.append(auto3)
autos.append(auto4)
autos.append(auto5)
autos.append(auto6)

promedio_1 = vel.promedio([auto[1] for auto  in autos])
promedio_2 = vel.promedio([auto[2] for auto  in autos])
promedio_3 = vel.promedio([auto[4] for auto  in autos])

print("promedio 1: {}".format(promedio_1))
print("promedio 2: {}".format(promedio_2))
print("promedio 3: {}".format(promedio_3))