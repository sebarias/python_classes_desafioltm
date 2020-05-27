
def multiplicame_estos_dos_numeros(x, y):
    print("multiplicando estos numeros, me da: {}".format(x * y))

x = int(input("Ingresa un puto numero charly: "))
y = int(input("Ingresa otro numbero charly: "))

multiplicame_estos_dos_numeros(x, y)

def multiplica_estos_dos_numeros_pero_uno_es_opcional(x, y = 1):
    #por defecto, y tendrá el valor de 1
    return(x * y)

print("al multiplicar {} y nada, me da: {}".format(456,multiplica_estos_dos_numeros_pero_uno_es_opcional(456)))