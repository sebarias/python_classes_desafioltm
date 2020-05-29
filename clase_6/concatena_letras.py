# Crear una función llamada gen que reciba el número de letras a generar, y devuelva un string con
# todas las letras generadas concatendas.
import string

def gen(n):
    abc = string.ascii_lowercase
    return abc[:n]

print(gen(10))
