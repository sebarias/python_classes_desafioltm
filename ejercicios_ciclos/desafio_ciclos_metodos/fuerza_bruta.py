contrasenia = input("ingrese contraseña: ")
abecedario = "abcdefghijklmnopqrstuvwxyz"
intentos = 0
for i in contrasenia:
    for j in abecedario:
        intentos += 1
        if(i.lower() == j.lower()):
            break
        
print(intentos)