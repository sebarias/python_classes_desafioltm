#  La función letra_i(n) , la cual al ser llamada, retornará una cadena de texto que al ser
# imprimida con print, dibujará una letra "i" según el ejemplo

def letra_i(n):
    linea = "*" * n
    columna = ""
    for i in range(n-1):
        columna += (" " * int(n/2) )+ "*" + (" " * int(n/2) ) + "\n"
    return linea + "\n" + columna + linea

print(letra_i(5))