palabra = input('Ingresa una palabra : ')
n = len(palabra)
print(n)

if n <=4:
    print('la palabra {} es corta'.format(palabra))
elif n <=10:
    print('la palabra {} es mediana'.format(palabra))
elif n < 15:
    print('la palabra {} es larga'.format(palabra))
else:
    print('la palabra {} es muy larga'.format(palabra))
