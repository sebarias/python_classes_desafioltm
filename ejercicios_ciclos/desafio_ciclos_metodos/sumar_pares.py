numero_usuario = int(input("Ingrese un numero: "))

sum = 0
for i in range(numero_usuario + 1):
    if(i % 2 == 0 and i != 0):
        sum += i

print(sum)