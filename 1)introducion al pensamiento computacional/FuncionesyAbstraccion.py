opc=0
print('''
-------------MENU-------------
Seleccione un metodo para obeter la raiz 
1.-Aproximacion de objetivo
2.-Busqueda binaria
3.-Enumeracion enteros

''')
def aproximacion(objetivo):
    objetivo= objetivo
    epsilon=0.01
    paso= epsilon**2
    respuesta=0.0

    while abs (respuesta**2 -objetivo)>= epsilon and respuesta<=objetivo:
        #  print(abs(respuesta**2 -objetivo),respuesta)
         respuesta +=paso
    if abs(respuesta**2- objetivo)>=epsilon:
         print(f'Nose encontro la raiz cuadrada de {objetivo}')
    else :
        print(f'La raiz cuadrada aproximada de {objetivo} es {respuesta}')
def binario(objetivo):
    objetivo= objetivo
    epsilon= 0.001
    bajo= 0.0
    alto=max(1.0, objetivo)
    respuesta=(alto+bajo)/2
    while abs(respuesta**2- objetivo)>=epsilon:
        #print(f'bajo={bajo},  alto={alto}, respuesta={respuesta}')
        if respuesta**2 <objetivo:
         bajo=respuesta
        else:
         alto=respuesta
    
        respuesta=(alto+bajo)/2

    print(f'la raiz de {objetivo} es {respuesta}')
def entero(objetivo):
    objetivo= objetivo

    respuesta=0
    while respuesta **2<objetivo:
        respuesta +=1
    if respuesta**2== objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print (f'{objetivo} no tiene raiz cuadrada exacta')
while opc<5:
    opc=int(input('Escoja una opcion'))   
    if opc==1:
        objetivo=int(input('Escoge un numero'))
        aproximacion(objetivo)
    elif opc==2:
        objetivo=int(input('Escoge un numero'))
        binario(objetivo)
    elif opc==3:
        objetivo=int(input('Escoge un numero entero'))
        entero(objetivo)
    elif opc==4:
        print('ADIOS')
    else:
        print('opcion invalida')    


