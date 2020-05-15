
import sys

precio_venta = int(sys.argv[1])
num_ususarios = int(sys.argv[2])
gastos = int(sys.argv[3])
utilidad = precio_venta * num_ususarios - gastos
if utilidad > 0:
    utilidad = utilidad * 0.75
print("Las utilidades son: US$ " + str(utilidad))