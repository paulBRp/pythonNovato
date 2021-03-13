nomb_1=input('Ingresa una nombre: ')
edad_1=int(input('Ingresa una edad: '))
nomb_2=input('Ingresa una nombre: ')
edad_2=int(input('Ingresa una edad: '))

if nomb_1>nomb_2:
    print(f'{nomb_1} es mayor')

elif nomb_1<nomb_2:
    print(f'{nomb_2} es mayor')
else :
    print(f'{nomb_1} y {nomb_2} tienen la misma edad')