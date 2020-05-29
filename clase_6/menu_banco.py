saldo_global = 0

def mostrar_menu(saldo = 0):
    saldo_global = saldo
    print('¡Bienvenido al Banco Amigo!. Escoja una opción:')
    print('-' * 20)
    print('1) Consultar saldo')
    print('2) Hacer depósito')
    print('3) Realizar giro')
    print('4) Salir')
    print()

def depositar(saldo, cantidad):
    return saldo + cantidad

def girar(saldo, cantidad):
    if(cantidad > saldo):
        return False
    else:
        return saldo - cantidad
    
opt_menu = ""

while opt_menu != '4':
    mostrar_menu() # Se llama a la función
    
    opt_menu = input()

    if opt_menu == '1':
        print('tu saldo es: {}\n'.format(saldo_global))
    elif opt_menu == '2':
        monto_deposito = int(input("Ingrese monto deposito: \n"))
        saldo_global = depositar(saldo_global, monto_deposito)
        print('tu nuevo saldo es: {}\n'.format(saldo_global))
    elif opt_menu == '3':
        monto_giro = int(input("ingrese monto de giro: \n"))
        if(girar(saldo_global, monto_giro) != False):
            saldo_global = girar(saldo_global, monto_giro)
            print('Se ha realizado el giro. Nuevo saldo es: {}\n'.format(saldo_global))
        else:
            print("no es posible realizar el giro, no hay fondos suficientes.\n")
        
    elif opt_menu == '4':
        print('Saliendo')
    else:
        print('Opción inválida\n')
print()