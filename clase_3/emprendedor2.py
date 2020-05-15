

import sys

precio_venta = int(sys.argv[1])
num_usuarios_utilidades = int(sys.argv[2])
num_usuarios_premium = int(sys.argv[3])
num_usuarios_gratuitos = int(sys.argv[4])
gastos = int(sys.argv[5])
utilidad = precio_venta * (num_usuarios_premium * 2) - gastos
if utilidad > 0:
    utilidad = utilidad * 0.75
print("Las utilidades son: US$ " + str(utilidad))