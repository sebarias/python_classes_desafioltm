#  La función letra_x(n) , la cual al ser llamada, retornará una cadena de texto que al ser
# imprimida con print, dibujará una letra "x" según el ejemplo

def letra_x(n):
    linea = ""
    decrement = n - 2
    for i in range(int(n/2)):
        linea += (" " * i) + "*" + (" " * decrement ) + "*" + "\n"        
        decrement -= 2
    linea += (" " * int(n /2)) + "*" + "\n"
    increment = 1
    for i in range(int(n/2),0,-1):
        print(i)
        linea += (" " * (i-1)) + "*" + (" " * increment ) + "*" + "\n"        
        increment += 2
    return linea
print(letra_x(10))