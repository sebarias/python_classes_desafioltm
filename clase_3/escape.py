import sys
import math
gravedad = float(sys.argv[1])
radio = float(sys.argv[2]) * 1000

velocidad_escape = round(math.sqrt(2 * gravedad * radio),2)


print("velocidad de escape es {}".format(velocidad_escape))