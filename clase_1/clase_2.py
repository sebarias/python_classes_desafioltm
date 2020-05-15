""" uso de import sys """

import sys

""" a = sys.argv
print(a)
print(len(a))
print(type(a)) 

ejecucion python clase_2.py 4 "hola" 1231.8 True  
imprime
18.0
12.8062484749
False
<type 'float'>
<type 'float'>
<type 'bool'>
 """

a = int(sys.argv[1])
b = int(sys.argv[2])
print(a + b)
# ejecución python clase_2.py 4 14 // muestra resultado 18