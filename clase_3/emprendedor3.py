
import sys

precio_venta = int(sys.argv[1])
num_usuarios_totales = int(sys.argv[2])
gastos = int(sys.argv[3])

utilidad_actual = precio_venta *  num_usuarios_totales - gastos
# 
if utilidad_actual > 0:
    utilidad_actual = utilidad_actual * 0.75

if sys.argv.count > 4:
    utilidades_anterior_periodo = int(sys.argv[4])
else:
    utilidades_anterior_periodo = 1000

razon = utilidad_actual / utilidades_anterior_periodo

print("Las razon entre las utilidades es del " + str(razon) + "%") 