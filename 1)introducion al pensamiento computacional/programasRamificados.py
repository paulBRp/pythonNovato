#Exercise
objetivo = int(input('Escoge un entero: '))
respuesta = 0

while respuesta**2 < objetivo:
respuesta +=1

if respuesta**2 == objetivo:
print(f'la raiz cuadrad de {objetivo} es {respuesta}'')
else:
print(f' {objetivo} no tiene una raiz exacta')