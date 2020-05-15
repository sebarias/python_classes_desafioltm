# comparacion de dos codigos 
mayor_de_edad=True
zurdo = False


"""
# sin refactozar
if mayor_de_edad is True:
    if zurdo is True:
        print('Mayor de edad y zurdo')
    else:
        print('Mayor de edad y diestro')
else: 
    if zurdo is True:
        print('Menor de edad y zurdo')
    else:
        print('Menor de edad y diestro')

"""

"""
# refactorizado
if mayor_de_edad is True and zurdo is True:
    print('Mayor de edad y zurdo')
elif mayor_de_edad is True and zurdo is False:
    print('Mayor de edad y diestro')
elif mayor_de_edad is False and zurdo is True:
    print('Menor de edad y zurdo')
else: 
    print('Menor de edad y diestro')
"""

# refactorizando usando la condición boleana

if mayor_de_edad and zurdo :
    print('Mayor de edad y zurdo')
elif mayor_de_edad and   ~ zurdo:
    print('Mayor de edad y diestro')
elif  not mayor_de_edad and zurdo:
    print('Menor de edad y zurdo')
else: 
    print('Menor de edad y diestro')

# la negaciòn de una variable boleana puede ser not o ~.
