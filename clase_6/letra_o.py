# La función letra_o(n) , la cual al ser llamada, retornará una cadena de texto que al ser
# imprimida con print, dibujará una letra "o" según el ejemplo

def letra_o(n):
    linea = "*" * n
    columna = ""
    for i in range(n-2):
        columna += "*" + ((n-2) * " ") + "*" + "\n"
    return linea + "\n" + columna + linea

print(letra_o(8))   